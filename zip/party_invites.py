from typing import List, Tuple
from collections import defaultdict


def max_party_level(levels: List[int], chain: List[List[int]]) -> int:
    n = len(levels)
    if n == 0:
        return 0
    
    tree = defaultdict(list)
    children = set()
    for manager, report in chain:
        tree[manager].append(report)
        children.add(report)
        
    roots = [i for i in range(n) if i not in children]
    
    def dfs(node) -> Tuple[int, int]:
        include = levels[node]
        exclude = 0
        
        for child in tree[node]:
            inc_child, exc_child = dfs(child)
            
            include += exc_child
            exclude += max(inc_child, exc_child)
            
        return (include, exclude)
    
    total_max = 0
    for root in roots:
        total_max += max(dfs(root))
        
    return total_max
