from collections import Counter


def translate(s: str) -> str:
    return f"Translated: {s}"

def is_valid(data):
    if isinstance(data, dict):
        return all(is_valid(v) for v in data.values())
    if isinstance(data, str):
        return not data.endswith("_id")
    return True

def translate_map(data):
    if not is_valid(data):
        return data

    if isinstance(data, dict):
        return {k: translate_map(v) for k, v in data.items()}
    elif isinstance(data, str):
        return translate(data)
    
    return data


def find_most_freq(data):
    if not data or not is_valid(data):
        return ""
    
    counts = Counter()
    
    def collect(node):
        if isinstance(node, dict):
            for v in node.values():
                collect(v)
        elif isinstance(node, str):
            counts[node] += 1
            
    collect(data)
    
    if not counts: 
        return ""
    
    return max(counts, key=lambda x: counts[x])

# 4단계: Part 3 함수 내부 수정 (Refactoring)

def find_optimal_phrase(data): # 이름 변경해도 됨
    if not data or not is_valid(data):
        return ""
    
    counts = Counter()
    
    def collect(node):
        if isinstance(node, dict):
            for v in node.values():
                collect(v)
        elif isinstance(node, str):
            # [Update] 여기만 바뀜! (N-gram 로직 추가)
            words = node.split()
            n = len(words)
            for i in range(n):
                for j in range(i, n):
                    phrase = " ".join(words[i:j+1])
                    counts[phrase] += 1
            
    collect(data)
    
    if not counts: return ""
    
    # [Update] 점수 계산 로직 변경 (빈도 * 길이)
    return max(counts, key=lambda p: counts[p] * len(p.split()))
            
