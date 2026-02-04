from collections import defaultdict
from typing import List

# Time: O(n)
#   - Bounded (rank 1-13, 4 suits): O(n)
#   - Unbounded rank: O(n^3)
# Space: 
#   - O(n^3) (including output)
#   - O(n)  (excluding output)
def find_valid_group(cards: List[str]) -> List[List[str]]:
    """
    valid group
        - SSCR
            - The same suit
            - consecutive integers
            - size >= 3
            - must output evey contiguous sub-run (3 <= <= L)
        
        - SRS
            - The same rank
            - size >= 3
            - output one group
    """
    rank_map = defaultdict(list)
    suit_map = defaultdict(list)
    
    for card in cards:
        rank_str = card[:-1]
        suit_char = card[-1]
        rank = int(rank_str)
        
        rank_map[rank].append(card)
        suit_map[suit_char].append(rank)
        
    results = []
    
    # 2. Same-rank set (동일 숫자 그룹) 처리
    # 조건: 개수가 3개 이상이면 해당 숫자의 모든 카드를 하나의 그룹으로
    # 반환
    for r in rank_map:
        if len(rank_map[r]) >= 3:
            results.append(rank_map[r])
            
    for s in suit_map:
        ranks = sorted(suit_map[s]) # O(nlogn)
        
        if not ranks:
            continue
        
        maximal_runs = []
        current_run = [ranks[0]]
        for i in range(1, len(ranks)):
            if ranks[i] == ranks[i-1] + 1:
                current_run.append(ranks[i])
            else:
                maximal_runs.append(current_run)
                current_run = [ranks[i]]
        maximal_runs.append(current_run)
        
        for run in maximal_runs:
            n = len(run)
            if n < 3:
                continue
            
            for length in range(3, n + 1):
                for i in range(n - length + 1):
                    sub_ranks = run[i : i + length]
                    group = [f"{r}{s}" for r in sub_ranks]
                    results.append(group)
                    
    return results
            
if __name__ == "__main__":
    input_cards = ["1C", "1H", "1D", "2C", "3C"]
    output = find_valid_group(input_cards)
    
    print("Input:", input_cards)
    print("Output:")
    for group in output:
        print(group)
    