from collections import Counter
import heapq

def rearrange_string(s: str) -> str:
    if len(s) <= 1:
        return s
    
    counts = Counter(s)
    
    max_count = max(counts.values())
    if max_count > (len(s) + 1) // 2:
        raise ValueError("No valid rearrangement possible")
    
    heap = []
    
    for ch, count in counts.items():
        heapq.heappush(heap, (-count, ch))
        
    result = []
    
    prev_count = 0
    prev_char = ""
    
    while heap:
        count, ch = heapq.heappop(heap)
        
        result.append(ch)
        
        count += 1
        
        if prev_count < 0:
            heapq.heappush(heap, (prev_count, prev_char))
            
        prev_count = count
        prev_char = ch
        
    if prev_count < 0:
        raise ValueError("No valid rearrangement possible")
    
    return "".join(result)
