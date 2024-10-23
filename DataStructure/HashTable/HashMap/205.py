# Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}
        for i in range(len(s)):
            if (s[i] in hm1 and t[i] != hm1[s[i]]) or (
                t[i] in hm2 and s[i] != hm2[t[i]]
            ):
                return False
            hm1[s[i]] = t[i]
            hm2[t[i]] = s[i]
        return True
