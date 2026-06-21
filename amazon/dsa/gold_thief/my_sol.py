def max_stolen_gold(gold: list[int]) -> int:
    prev_one = 0
    prev_two = 0
    
    for amount in gold:
        steal_current = prev_two + amount
        skip_current = prev_one
        current = max(steal_current, skip_current)
        
        prev_two = prev_one
        prev_one = current
        
    return prev_one

print(max_stolen_gold([2, 7, 9, 3, 1]))
# 12
# Steal from houses with values 2, 9, and 1.

print(max_stolen_gold([5, 1, 1, 5]))
# 10
# Steal from the first and last house.
