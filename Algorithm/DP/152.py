from typing import List

# Brute Force
# Time: O(n^2)
# Space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        
        for i in range(len(nums)):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)
                
        return res

# Sliding Window <- TOO COMPLICATED
"""
The maximum-product subarray problem is tricky because:
    - A negative number flips the sign (a very small negative can become a very large positive after another negative)
    - A zero breaks any product (anything crossing a zero becomes 0)
    
So we can treat the array as separate segments split by zeros
Inside one zero-free segment:
    - If the count of negative numbers is even, the product of the whole segment is positive → usually the best
    - If the count is odd, we must drop either the prefix up to the
      first negative or the suffix after the last negative to make the
      remaining product have an even number of negatives
    
This “sliding window” idea maintains a window that contains an allowed number of negatives (even), shrinking from the left when we exceed that
"""
class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        A = []
        cur = []
        res = float('-inf')

        for num in nums:
            res = max(res, num)
            if num == 0:
                if cur:
                    A.append(cur)
                cur = []
            else:
                cur.append(num)

        if cur:
            A.append(cur)

        for sub in A:
            negs = sum(1 for i in sub if i < 0)
            prod = 1
            need = negs if negs % 2 == 0 else negs - 1
            negs = 0
            j = 0

            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i] < 0:
                    negs += 1
                    while negs > need:
                        prod //= sub[j]
                        if sub[j] < 0:
                            negs -= 1
                        j += 1
                if j <= i:
                    res = max(res, prod)

        return int(res)
            
# Kadane's Algorithm
# Time: O(n)
# Space: O(1)
"""
This is the Kadane-style solution adapted for products.

In the classic maximum-sum subarray, we only track one value (current max sum).
For products, that’s not enough because:
    - A negative × negative = positive
    - A very small (negative) product can suddenly become the maximum
      after multiplying by another negative.
    
So at every index, we must track two values:
    - curMax: maximum product ending at this index.
    - curMin: minimum product ending at this index.
    
Why curMin matters:
    - If the current number is negative, multiplying it with curMin
      might produce a new maximum.
    
Zeros are naturally handled because choosing num alone can reset the product.
"""
class Solution3:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1
        
        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res
