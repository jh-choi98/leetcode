class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
            
        return res

class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
            
        return res
