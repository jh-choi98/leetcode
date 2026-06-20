"""
Time complexity: O(n)
    I go through the list of houses exactly once, and each house takes
    constant work, so the time complexity is O(n), where n is the number
    of houses
Space complexity: O(1)
    I'm not using a full DP array. I only keep two variables, so the
    extra space complexity if O(1)
"""
def max_stolen_gold(gold: list[int]) -> int:
    """
        This is a DP problem because at each house, my decision affects
        whether I can steal from the next house.
        
        For each house, I have two choices: either steal from this house
        and add it to the best result from two houses back, or skip this
        house and keep the best result from the previous house 
    """
    prev_two = 0 # Best value up to two houses before
    prev_one = 0 # Best value up to the previous house
    
    for amount in gold:
        """
            If I steal from the current house, I cannot use the previous
            house, so I add the current amount to prev_two
        """
        steal_current = prev_two + amount
        
        # If I skip the current house, then the best value stays as
        # prev_one
        skip_current = prev_one
        
        # The best answer up to this house is the better of those two
        # choices
        current = max(steal_current, skip_current)
        
        # Now I roll the two DP values forward for the next iteration
        prev_two = prev_one
        prev_one = current
        
    """
        After processing all houses, prev_one stores the maximum amount
        we can steal without taking from adjacent houses
    """
    return prev_one

print(max_stolen_gold([2, 7, 9, 3, 1]))
# 12
# Steal from houses with values 2, 9, and 1.

print(max_stolen_gold([5, 1, 1, 5]))
# 10
# Steal from the first and last house.
