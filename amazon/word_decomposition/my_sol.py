# DFS/DP memoization

def find_word_decomposition(words: list[str]) -> dict[str, list[list[str]]]:
    word_set = {word for word in words if word}
    
    if not word_set:
        return {}
    
    word_lengths = sorted({len(word) for word in word_set})
    min_word_len = word_lengths[0]
    
    result = {}
    seen_words = set()
    
    for word in words:
        if not word or word in seen_words:
            continue
        
        seen_words.add(word)
        
        if len(word) < 2 * min_word_len:
            continue
        
        memo = {}
        
        def dfs(start: int) -> list[list[str]]:
            if start == len(word):
                return [[]]
            
            if start in memo:
                return memo[start]
            
            decompositions = []
            
            for length in word_lengths:
                end = start + length
                
                if end > len(word):
                    break
                
                piece = word[start:end]
                
                if piece not in word_set:
                    continue
                
                if start == 0 and end == len(word):
                    continue
                
                suffix_decompositions = dfs(end)
                
                for suffix in suffix_decompositions:
                    decompositions.append([piece] + suffix)
                    
            memo[start] = decompositions
            return decompositions
        
        decompositions = dfs(0)
        
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
