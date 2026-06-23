from collections import defaultdict
import random


def select_raffle_winners(
    transactions: list[tuple[str, float]],
    k: int
) -> list[str]:
    if k < 0:
        raise ValueError("k cannot be negative")
    
    if k == 0:
        return []
    
    spending_by_customers: dict[str, float] = defaultdict(float)
    
    for customer_id, spending in transactions:
        spending_by_customers[customer_id] += spending
        
    eligible_customers = []
    
    for customer_id, total_spending in spending_by_customers.items():
        if total_spending > 0:
            eligible_customers.append((customer_id, total_spending))
            
    if k > len(eligible_customers):
        raise ValueError("Not enough eligible customers to select k unique winners")
    
    winners = []
    
    for _ in range(k):
        total_weights = 0
        
        for _, spending in eligible_customers:
            total_weights += spending
            
        random_value = random.random() * total_weights
        cumulative_weight = 0
        
        for index, (customer_id, spending) in enumerate(eligible_customers):
            cumulative_weight += spending

            if cumulative_weight >= random_value:
                winners.append(customer_id)
                eligible_customers.pop(index)
                break
    
    return winners
    
    