class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(s):
            cur = hm[c]
            if i < len(s) - 1:
                if (c == 'I' and s[i + 1] in 'VX') or (c == 'X' and s[i + 1] in 'LC') or (c == 'C' and s[i + 1] in 'DM'):
                    cur = -cur
            result += cur

        return result

class Solution2:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        prev = 0
        
        for ch in s:
            cur = romanDict[ch]
            if prev >= cur:
                ans += prev
            else:
                ans -= prev

            prev = cur
        ans += prev
        return ans
