# Weighted Random Sampling Without Replacement

from collections import defaultdict
import random

"""
    T = number of transactions
    C = number of unique eligible customers
    K = number of winners
    
    Time: O(T + K * C):
        Aggregating transactions takes O(T).
        Then for each winner, we compute the total weight and scan the eligible customers
        to find the selected customer. That costs O(C) per winner.
        Doing that K times gives O(K * C).

    Space: O(C):
        We store total spending for each customer and keep a list of eligible customers.
        The output list stores K winners, so if we count the output, space is O(C + K).
"""
def select_raffle_winners(
    transactions: list[tuple[str, float]],
    k: int
) -> list[str]:
    if k < 0:
        raise ValueError("k cannot be negative")
    
    if k == 0:
        return []
    
    """
        First, I'll aggregate spending by customer because one customer
        can have multiple transactions during the promotional period
    """
    spending_by_customer: dict[str, float] = defaultdict(float)
    
    for customer_id, amount in transactions:
        spending_by_customer[customer_id] += amount
        
    """
        Only customers with positive total spending should be eligible.
        A customer with zero or negative spending should not have raffle weight.
    """
    eligible_customers = []
    
    for customer_id, total_spending in spending_by_customer.items():
        if total_spending > 0:
            eligible_customers.append((customer_id, total_spending))
            
    if k > len(eligible_customers):
        raise ValueError("Not enough eligible customers to select k unique winners")
    
    winners = []
    
    """
        I'll repeatedly pick one weighted random winner.
        After picking a winner, I'll remove that customer so winners
        stay unique.
    """
    for _ in range(k):
        total_weight = 0
        
        for _, spending in eligible_customers:
            total_weight += spending
            
        """
            I'll generate a random number between 0 and total weight.
            Then I'll scan the cumulative weights to find the selected customer
        """
        random_value = random.random() * total_weight
        
        cumulative_weight = 0
        
        for index, (customer_id, spending) in enumerate(eligible_customers):
            cumulative_weight += spending
            
            if cumulative_weight >= random_value:
                winners.append(customer_id)
            
                """
                    Removing the selected customer ensures the same
                    customer cannot win more than once
                """
                eligible_customers.pop(index)
                break
    return winners


transactions: list[tuple[str, float]] = [
    ("A", 50),
    ("B", 10),
    ("C", 20),
    ("A", 25),
]

print(select_raffle_winners(transactions, 2))



# Follow-up Mention: If Scale Is Huge

"""
    The current solution is simple and good for moderate input sizes, but it does O(C) work for each winner. If the customer list is huge, I would store the weights in a Fenwick tree or segment tree. Then I can find the customer corresponding to a random prefix sum in O(log C), and after selecting them, update their weight to 0 in O(log C). That gives O(T + C + K log C) time.
"""
