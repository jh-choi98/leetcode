class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_map: dict[str, int] = {}
        for ch in t:
            if ch in t_map:
                t_map[ch] += 1
            else:
                t_map[ch] = 1

        for ch in s:
            if ch not in t_map:
                return False
            else:
                t_map[ch] -= 1

        result_list: list[int] = list(t_map.values())
        for i in result_list:
            if i != 0:
                return False
        return True

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s: dict[str, int] = {}
        count_t: dict[str, int] = {}
        
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
            
        for ch in count_s:
            if count_s[ch] != count_t.get(ch, 0):
                return False
            
        return True
