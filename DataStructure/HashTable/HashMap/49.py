from collections import defaultdict
from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: dict[tuple, list[str]] = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for ch in s:
                count[ord(ch) - ord('a')] += 1
                
            res[tuple(count)].append(s)
            
        return list(res.values())
