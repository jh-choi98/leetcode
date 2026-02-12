def winning_hands(tiles: str):
    original_counts = [0] * 10
    for t in tiles:
        original_counts[int(t)] += 1
        
    def check(i, counts):
        while i <= 9 and counts[i] == 0:
            i += 1
        if i > 9:
            return True
        
        if counts[i] >= 3:
            counts[i] -= 3
            if check(i, counts):
                return True
            counts[i] += 3
            
        if i <= 7 and counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            
            if check(i, counts):
                return True
            
            counts[i] += 1
            counts[i+1] += 1
            counts[i+2] += 1
            
        return False
        
    res = []
    for new_tile in range(1, 10):
        if original_counts[new_tile] >= 4:
            continue
        
        original_counts[new_tile] += 1
        
        win = False
        for head in range(1, 10):
            if original_counts[head] >= 2:
                temp_C = original_counts[:]
                temp_C[head] -= 2
                
                if check(1, temp_C):
                    win = True
                    break
        if win:
            res.append(new_tile)
        original_counts[new_tile] -= 1
        
    return res
