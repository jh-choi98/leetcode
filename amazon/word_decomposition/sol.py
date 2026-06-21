# DFS/DP memoization

"""
    Let W be the number of words, L be the maximum word length, and K be
    the number of distinct word lengths in the dictionary. R = total size of all decompositions we output
    - Time: O(W * L * K + R)
        For each word, the DFS has at most L start positions. At each
        start position, instead of trying all possible end positions, I
        only try K possible word length. So the base candidate-checking
        work is O(L * K) per word,or O(W * L * K) across all words.
        Since K is at most L, the worst case is still O(W * L^2), but in
        practice this can be much better when the dictionary only
        contains words of a few different lengths.
        Also, because the problem asks us to print all valid
        decompositions, the true runtime is output-sensitive. If there
        are many decompositions, we must spend time proportional to the
        total size of the output
    - Space: O(W + K + L + R)
        the recursion depth is O(L), and the memo table stores
      decompositions for suffixes, so the memory usage is also
      output-sensitive. Ignoring the output itself, the extra structual
      space is O(L), but including memoized decompositions, it can grow
      the toal number of decompositions.
"""
def find_word_decomposition(words: list[str]) -> dict[str, list[list[str]]]:
    """
        I'll put all non-empty words into a set so that checking whether
        a piece is a valid word is O(1) on average
    """
    word_set = {word for word in words if word}
    
    if not word_set:
        return {}
    
    """
        Since the input can be large, I don't want to try every possible
        end index blindly. I'll only try substring lengths that actually
        exist in the dictionary
    """
    word_lengths = sorted({len(word) for word in word_set})
    min_word_len = word_lengths[0]
    
    result = {}
    seen_words = set()
    
    for word in words:
        if not word or word in seen_words:
            continue
        
        seen_words.add(word)
        
        """
            A valid decomposition needs at least two non-emtpy words.
            So if the word is shorter than two times the smallest word
            length, it cannot be decomposed
        """
        if len(word) < 2 * min_word_len:
            continue
        
        memo = {}
        
        def dfs(start: int) -> list[list[str]]:
            """
                If start reaches the end, then the current path forms a
                complete decomposition
            """
            if start == len(word):
                return [[]]
            
            if start in memo:
                return memo[start]
            
            decompositions = []
            
            """
               Instead of trying every end index, I only try lengths
               that correspond to actual words in the dictionary 
            """
            for length in word_lengths:
                end = start + length
                
                if end > len(word):
                    break
                
                piece = word[start:end]
                
                if piece not in word_set:
                    continue
                
                """
                    I should not count the whole word itself as one
                    piece. The decomposition must use at least two words
                """
                if start == 0 and end == len(word):
                    continue
                
                suffix_decompositions = dfs(end)
                
                for suffix in suffix_decompositions:
                    decompositions.append([piece] + suffix)
                    
            memo[start] = decompositions
            return decompositions
        
        decompositions = dfs(0)
        
        # At the end, I only keep decompositions with two or more parts
        valid_decompositions = []
        
        for decomposition in decompositions:
            if len(decomposition) >= 2:
                valid_decompositions.append(decomposition)
        
        if valid_decompositions:
            result[word] = valid_decompositions
        
    return result

def print_decompositions(words: list[str]) -> None:
    decompositions = find_word_decomposition(words)
    
    for word, combinations in decompositions.items():
        for combination in combinations:
            print(f"{word}: {combination}")
            
            
words = [
    "high", "super", "way", "superhighway", "highway",
    "rockstar", "rock", "star", "rocks", "tar", "stars", "rockstars"
]

print_decompositions(words)

# superhighway: ['super', 'high', 'way']
# superhighway: ['super', 'highway']
# highway: ['high', 'way']
# rockstar: ['rock', 'star']
# rockstar: ['rocks', 'tar']
# rockstars: ['rock', 'stars']
