# What is Kadane's Algorithm

Kadane's Algorithm is an efficient Dynamic Programming approach used to
find the maximum sum contiguous subarray in an array

- Time Complexity: O(n)
- Space Complexity: O(1)

# The Core Logic

As you iterate through the array, you ask yourself one question at every number:
"Should I extend the previous subarray, or start a new subarray from
here?"

1. If the previous sum was negative: It is a "burden." Adding a negative
   number to the current number will only make the result smaller. So,
   you discard the past and restart from the current number.
2. If the previous sum was positive: It is helpful. You extend the
   subarray by adding the current number to it.

# The Formula (Recurrence Relation)

For each elelment 'num' in the array:
currentSum = max(num, currentSum + num)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            current_max = max(num, current_max + num)
            global_max = max(global_max, cureent_max)

        return global_max
```
