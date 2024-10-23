from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]):
        hashset = set()
        for num in nums:
            if num not in hashset:
                # 가독성 측면에서 if num not in hashset:을 쓰는걸 권장 (Python에서도 권장하는 구문)
                # instead of if not num in hashset:
                hashset.add(num)
            else:
                return True
        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]):
        if len(set(nums)) != len(nums):
            return True
        return False
