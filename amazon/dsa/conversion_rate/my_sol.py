from collections import defaultdict, deque

def find_conversion_rate(rates: list[tuple[str, str, float]], from_currency, to_currency) -> float:
    graph: dict[str, list[tuple[str, float]]] = defaultdict(list)
    
    for source, target, rate in rates:
        if rate <= 0:
            raise ValueError("Invalid rate")
        
        graph[source].append((target, rate))
        graph[target].append((source, 1 / rate))
        
    if from_currency not in graph or to_currency not in graph:
        return -1.0
    
    queue = deque([(from_currency, 1.0)])
    visited = {from_currency}
    
    while queue:
        current_currency, current_rate = queue.popleft()
        
        if current_currency == to_currency:
            return current_rate
        
        for next_currency, edge_rate in graph[current_currency]:
            if next_currency in visited:
                continue
            visited.add(next_currency)
            next_rate = current_rate * edge_rate
            queue.append((next_currency, next_rate))
            
    return -1.0
            