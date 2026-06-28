# -----------------------------------
#   Main Coding
# -----------------------------------

"""
    Time: O(d * n^2)
"""
from abc import ABC, abstractmethod
from datetime import date


class Item:
    def __init__(self, item_id: str, name: str, price: float):
        self.item_id = item_id
        self.name = name
        self.price = price
        
class Cart:
    def __init__(self, customer_id: str, items: list[Item] | None = None, coupon_code: str | None = None):
        self.customer_id = customer_id
        self.items = items or []
        self.coupon_code = coupon_code
        
    @property
    def total_price(self) -> float:
        return sum(item.price for item in self.items)
    
class Discount(ABC):
    """A discount reports how much it saves on a single item, or 0 if it
    doesn't apply.
    
        Reporting 'dollars saved on one item' lets every discount type
        compete on the same axis, so we can always pick the biggest per item
    """
    
    @abstractmethod
    def saving_for(self, item: Item, cart: Cart) -> float:
        ...
        
class CustomerPercentageDiscount(Discount):
    """Type 1: fixed % off for a favoured customer"""
    
    def __init__(self, customer_id: str, percent: float):
        self._customer_id = customer_id
        self._percent = percent
        
    def saving_for(self, item: Item, cart: Cart) -> float:
        if cart.customer_id != self._customer_id:
            return 0.0
        return item.price * self._percent / 100

class CouponDiscount(Discount):
    """Type 3: single-use coupon, % off, with an expiry date"""
    
    def __init__(self, code: str, percent: float, expiry: date):
        self._code = code
        self._percent = percent
        self._expiry = expiry
        
    def saving_for(self, item: Item, cart: Cart) -> float:
        if cart.coupon_code != self._code:
            return 0.0
        if date.today() > self._expiry:
            return 0.0
        
        return item.price * self._percent / 100
    
class OrderTotalDiscount(Discount):
    """Type 5: % off every item once the order total hits a threshold"""
    
    def __init__(self, min_total: float, percent: float):
        self._min_total = min_total
        self._percent = percent
        
    def saving_for(self, item: Item, cart: Cart) -> float:
        if cart.total_price < self._min_total:
            return 0.0
        return item.price * self._percent / 100
    
class DiscountEngine:
    """Applies the single biggest discount to each item"""
    
    def __init__(self, discounts: list[Discount]):
        self._discounts = discounts
        
    def total_savings(self, cart: Cart) -> float:
        total = 0.0
        for item in cart.items:
            # one discount per item: take the biggest, default 0 if none
            # apply
            total += max(
                (discount.saving_for(item, cart) for discount in self._discounts), default=0.0
            )
            
        return total

if __name__ == "__main__":
    pen = Item("pen", "Pen", 10.0)
    cart = Cart("alice", [pen])
    engine = DiscountEngine([
        OrderTotalDiscount(min_total=5, percent=5),
        CustomerPercentageDiscount("alice", percent=20)
    ])
    assert engine.total_savings(cart) == 2.0
    
    no_coupon = Cart("bob", [Item("pen", "Pen", 10.0)])
    coupon_engine = DiscountEngine([CouponDiscount("SAVE10", 10, date(2030, 1, 1))])
    assert coupon_engine.total_savings(no_coupon) == 0.0

    print("All checks passed")

# -----------------------------------
#   Follow-up 1: 종류 추가
# -----------------------------------

class Item:
    def __init__(self, item_id: str, name: str, price: float):
        self.item_id = item_id
        self.name = name
        self.price = price


class Cart:
    def __init__(self, customer_id: str, items: list[Item] | None = None, coupon_code: str | None = None):
        self.customer_id = customer_id
        self.items = items or []
        self.coupon_code = coupon_code

    @property
    def total_price(self) -> float:
        return sum(item.price for item in self.items)


class Discount(ABC):
    """A discount reports how much it saves on a single item, or 0 if it doesn't apply.

    Reporting 'dollars saved on one item' lets every discount type compete
    on the same axis, so we can always pick the biggest per item.
    """

    @abstractmethod
    def saving_for(self, item: Item, cart: Cart) -> float:
        ...


class CustomerPercentageDiscount(Discount):
    """Type 1: fixed % off for a favoured customer."""

    def __init__(self, customer_id: str, percent: float):
        self._customer_id = customer_id
        self._percent = percent

    def saving_for(self, item: Item, cart: Cart) -> float:
        if cart.customer_id != self._customer_id:
            return 0.0
        return item.price * self._percent / 100


class QuantityPercentageDiscount(Discount):
    """Type 2: % off a product when buying at least N of it."""

    def __init__(self, item_id: str, min_quantity: int, percent: float):
        self._item_id = item_id
        self._min_quantity = min_quantity
        self._percent = percent

    def saving_for(self, item: Item, cart: Cart) -> float:
        if item.item_id != self._item_id:
            return 0.0
        count = sum(1 for i in cart.items if i.item_id == self._item_id)
        if count < self._min_quantity:
            return 0.0
        return item.price * self._percent / 100


class CouponDiscount(Discount):
    """Type 3: single-use coupon, % off, with an expiry date."""

    def __init__(self, code: str, percent: float, expiry: date):
        self._code = code
        self._percent = percent
        self._expiry = expiry

    def saving_for(self, item: Item, cart: Cart) -> float:
        if cart.coupon_code != self._code:
            return 0.0
        if date.today() > self._expiry:
            return 0.0
        return item.price * self._percent / 100


class OrderTotalDiscount(Discount):
    """Type 5: % off every item once the order total hits a threshold."""

    def __init__(self, min_total: float, percent: float):
        self._min_total = min_total
        self._percent = percent

    def saving_for(self, item: Item, cart: Cart) -> float:
        if cart.total_price < self._min_total:
            return 0.0
        return item.price * self._percent / 100


class FreeGift:
    """Type 4: buy a required set of items, get a gift free.

    Handled apart from per-item discounts because it adds a free item
    rather than reducing the price of one already in the cart.
    """

    def __init__(self, required_item_ids: set[str], gift: Item):
        self._required_item_ids = required_item_ids
        self._gift = gift

    def gift_value(self, cart: Cart) -> float:
        item_ids = {item.item_id for item in cart.items}
        return self._gift.price if self._required_item_ids.issubset(item_ids) else 0.0


class DiscountEngine:
    """Applies the single biggest discount to each item, plus any free gifts."""

    def __init__(self, discounts: list[Discount], gifts: list[FreeGift] | None = None):
        self._discounts = discounts
        self._gifts = gifts or []

    def total_savings(self, cart: Cart) -> float:
        total = 0.0
        for item in cart.items:
            # one discount per item: take the biggest, default 0 if none apply
            total += max(
                (discount.saving_for(item, cart) for discount in self._discounts),
                default=0.0,
            )
        for gift in self._gifts:
            total += gift.gift_value(cart)
        return total


# --- quick checks ---
if __name__ == "__main__":
    pen = Item("pen", "Pen", 10.0)
    cart = Cart("alice", [pen])
    engine = DiscountEngine([
        OrderTotalDiscount(min_total=5, percent=5),       # 0.50
        CustomerPercentageDiscount("alice", percent=20),  # 2.00
    ])
    assert engine.total_savings(cart) == 2.0  # biggest discount wins

    three_pens = Cart("carol", [pen, pen, pen])
    qty_engine = DiscountEngine([QuantityPercentageDiscount("pen", 3, percent=10)])
    assert qty_engine.total_savings(three_pens) == 3.0  # 3 pens qualify → 1.0 each

    paper = Item("paper", "Paper", 5.0)
    sharpener = Item("sharpener", "Sharpener", 3.0)
    gift_cart = Cart("dave", [pen, paper])
    gift_engine = DiscountEngine([], gifts=[FreeGift({"pen", "paper"}, sharpener)])
    assert gift_engine.total_savings(gift_cart) == 3.0  # gift value

    print("All checks passed.")

# -----------------------------------
#   Follow-up 2: Complexity 개선
# -----------------------------------
"""
    Time: O(d * n)
"""
from collections import Counter


class Item:
    def __init__(self, item_id: str, name: str, price: float):
        self.item_id = item_id
        self.name = name
        self.price = price


class CartSummary:
    """Cart aggregates computed once, so each discount check is O(1).

    Without this, quantity/total discounts re-scan the cart on every call,
    pushing the engine to O(d * n^2). Precomputing keeps it at O(n * d).
    """

    def __init__(self, customer_id: str, coupon_code: str | None,
                 total_price: float, item_counts: Counter):
        self.customer_id = customer_id
        self.coupon_code = coupon_code
        self.total_price = total_price
        self.item_counts = item_counts  # item_id -> how many are in the cart


class Cart:
    def __init__(self, customer_id: str, items: list[Item] | None = None, coupon_code: str | None = None):
        self.customer_id = customer_id
        self.items = items or []
        self.coupon_code = coupon_code

    @property
    def total_price(self) -> float:
        return sum(item.price for item in self.items)

    def summarize(self) -> CartSummary:
        """Scan the cart once to build the aggregates discounts need."""
        return CartSummary(
            customer_id=self.customer_id,
            coupon_code=self.coupon_code,
            total_price=self.total_price,
            item_counts=Counter(item.item_id for item in self.items),
        )


class Discount(ABC):
    """Reports how much it saves on a single item, or 0 if it doesn't apply.

    Takes a precomputed CartSummary so every check is O(1).
    """

    @abstractmethod
    def saving_for(self, item: Item, summary: CartSummary) -> float:
        ...


class CustomerPercentageDiscount(Discount):
    """Type 1: fixed % off for a favoured customer."""

    def __init__(self, customer_id: str, percent: float):
        self._customer_id = customer_id
        self._percent = percent

    def saving_for(self, item: Item, summary: CartSummary) -> float:
        if summary.customer_id != self._customer_id:
            return 0.0
        return item.price * self._percent / 100


class QuantityPercentageDiscount(Discount):
    """Type 2: % off a product when buying at least N of it."""

    def __init__(self, item_id: str, min_quantity: int, percent: float):
        self._item_id = item_id
        self._min_quantity = min_quantity
        self._percent = percent

    def saving_for(self, item: Item, summary: CartSummary) -> float:
        if item.item_id != self._item_id:
            return 0.0
        if summary.item_counts[self._item_id] < self._min_quantity:  # O(1) lookup
            return 0.0
        return item.price * self._percent / 100


class CouponDiscount(Discount):
    """Type 3: single-use coupon, % off, with an expiry date."""

    def __init__(self, code: str, percent: float, expiry: date):
        self._code = code
        self._percent = percent
        self._expiry = expiry

    def saving_for(self, item: Item, summary: CartSummary) -> float:
        if summary.coupon_code != self._code:
            return 0.0
        if date.today() > self._expiry:
            return 0.0
        return item.price * self._percent / 100


class OrderTotalDiscount(Discount):
    """Type 5: % off every item once the order total hits a threshold."""

    def __init__(self, min_total: float, percent: float):
        self._min_total = min_total
        self._percent = percent

    def saving_for(self, item: Item, summary: CartSummary) -> float:
        if summary.total_price < self._min_total:  # precomputed, O(1)
            return 0.0
        return item.price * self._percent / 100


class FreeGift:
    """Type 4: buy a required set of items, get a gift free.

    Handled apart from per-item discounts because it adds a free item
    rather than reducing the price of one already in the cart.
    """

    def __init__(self, required_item_ids: set[str], gift: Item):
        self._required_item_ids = required_item_ids
        self._gift = gift

    def gift_value(self, summary: CartSummary) -> float:
        if self._required_item_ids <= summary.item_counts.keys():
            return self._gift.price
        return 0.0


class DiscountEngine:
    """Applies the single biggest discount to each item, plus any free gifts.

    Computes cart aggregates once, then each per-item check is O(1),
    giving O(n * d) overall (n items, d discounts).
    """

    def __init__(self, discounts: list[Discount], gifts: list[FreeGift] | None = None):
        self._discounts = discounts
        self._gifts = gifts or []

    def total_savings(self, cart: Cart) -> float:
        summary = cart.summarize()  # one O(n) scan up front
        total = 0.0
        for item in cart.items:
            # one discount per item: take the biggest, default 0 if none apply
            total += max(
                (discount.saving_for(item, summary) for discount in self._discounts),
                default=0.0,
            )
        for gift in self._gifts:
            total += gift.gift_value(summary)
        return total


# --- quick checks ---
if __name__ == "__main__":
    pen = Item("pen", "Pen", 10.0)
    cart = Cart("alice", [pen])
    engine = DiscountEngine([
        OrderTotalDiscount(min_total=5, percent=5),       # 0.50
        CustomerPercentageDiscount("alice", percent=20),  # 2.00
    ])
    assert engine.total_savings(cart) == 2.0  # biggest discount wins

    three_pens = Cart("carol", [pen, pen, pen])
    qty_engine = DiscountEngine([QuantityPercentageDiscount("pen", 3, percent=10)])
    assert qty_engine.total_savings(three_pens) == 3.0  # 3 pens qualify → 1.0 each

    no_coupon = Cart("bob", [Item("pen", "Pen", 10.0)])
    coupon_engine = DiscountEngine([CouponDiscount("SAVE10", 10, date(2030, 1, 1))])
    assert coupon_engine.total_savings(no_coupon) == 0.0  # not attached → ignored

    print("All checks passed.")
