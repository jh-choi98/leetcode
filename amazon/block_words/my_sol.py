def can_spell(blocks: list[tuple[str, str]], word: str) -> bool:
    if len(word) > len(blocks):
        return False
    
    candidates = []
    
    for ch in word:
        possible_blocks = []
        
        for i, block in enumerate(blocks):
            if ch in block:
                possible_blocks.append(i)
                
        if not possible_blocks:
            return False
        
        candidates.append(possible_blocks)
        
    candidates.sort(key=len)
    used = [False] * len(blocks)
    
    def backtrack(pos: int) -> bool:
        if pos == len(candidates):
            return True
        
        for block_index in candidates[pos]:
            if used[block_index]:
                continue
            
            used[block_index] = True
            
            if backtrack(pos + 1):
                return True
            
            used[block_index] = False
            
        return False
    
    return backtrack(0)
