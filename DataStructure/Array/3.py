class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_map = {}
        l = 0
        max_count = 0
        for i, c in enumerate(s):
            if c in sub_map and l <= sub_map[c]:
                l = sub_map[c] + 1
            sub_map[c] = i
            max_count = max(max_count, i - l + 1)
        return max_count

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
            
        return res
