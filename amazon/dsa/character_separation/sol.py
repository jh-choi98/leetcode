from collections import Counter
import heapq
"""
    n: the length of the string
    k: the number of unique characters
    
    - Time: O(nlogk)
        - Counting frequencies: O(n)
        - heap push and pop: O(nlogk)
    - Space: O(n + k)
        - heap stores at most k characters: O(k)
        - output: O(n)
        
    Let n be the length of the string and k be the number of unique characters.
    Counting frequencies takes O(n). Each character is pushed and popped
    from the heap at most once per occurrence, so the total time
    complexity is O(n log k).
    
    The heap stores at most k characters, and the output takes O(n)
    space, so the space complexity is O(n + k).
"""
def rearrange_string(s: str) -> str:
    """
        I'll start with a couple of simple edge cases. If the string has
        zero or one character, it's already valid
    """
    if len(s) <= 1:
        return s
    
    """
        The first thing I need is the frequency of each character,
        because the character that appears the most is the hardest one
        to place
    """
    counts = Counter(s)
    
    """
        Before building the result, I want to check if this is
        impossible. If one character appears more than half of the
        string length rounded up, we can't separate all copies of that character
    """
    max_count = max(counts.values())
    if max_count > (len(s) + 1) // 2:
        raise ValueError("No valid rearrangement possible")
    
    """
        Now I'll use a max heap so that I can always try to place the
        character with the highest remaining count
        Python's heapq is a min heap, so I'll store negative counts to
        simulate a max heap
    """
    heap = []
    
    for ch, count in counts.items():
        heapq.heappush(heap, (-count, ch))
        
    result = []
    
    """
       The key trick is that after I use a character, I don't want to
       put it back immediately. If I put it back right away, I might
       pick the same character again and create adjacent duplicates.
       
       So I'll hold the previously used character out of the heap for
       one round. After I choose a different character, then the
       previous one becomes safe to use again
    """
    prev_count = 0
    prev_char = ""
    
    while heap:
        """
            At each step, I pick the currently most frequent character
            that is allowed to be used
        """
        count, ch = heapq.heappop(heap)
        
        result.append(ch)
        
        """
            I used one copy of this character, so I move its negative
            count one step closer to zero
        """
        count += 1
        
        """
            Now that I've placed a different character, the previous
            character can go back into the heap if it still has
            remaining copies
        """
        if prev_count < 0:
            heapq.heappush(heap, (prev_count, prev_char))
            
        """
            Then I hold the current character out for the next round, so
            it cannot be placed immediately again
        """
        prev_count = count
        prev_char = ch
        
    """
        This is mostly a safety check. If there is still a leftover
        character after the heap is empty, then no valid arrangement was pissible
    """
    if prev_count < 0:
        raise ValueError("No valid reaarangement possible")
    
    """
        At this point, every character has been placed, and the way we
        managed the previous character guarantees that no adjacent
        characters are equal
    """
    return "".join(result)
