# Weighted graph traversal
# Graph + BFS/DFS

from collections import defaultdict, deque

"""
    Time: O(V + E)
        We build the graph from the rates, and then in the worst case
        BFS may explore the entire graph before finding the target
        currency
        
    Space: O(V + E)
        Mainly for storing the graph. The BFS queue and visited set add O(V), but the graph is the dominant part.
"""
def find_conversion_rate(rates: list[tuple[str, str, float]], from_currency, to_currency) -> float:
    """
        I'll model this as a graph. Each currency is a node, and each
        conversion rate is a weighted edge
    """
    graph: dict[str, list[tuple[str, float]]] = defaultdict(list)
    
    for source, target, rate in rates:
        if rate <= 0:
            raise ValueError("Invalid conversion rate")
        
        """
            Since conversion can go both ways, I'll add the original
            direction and also the reciprocal direction
        """
        graph[source].append((target, rate))
        graph[target].append((source, 1 / rate))
        
    """
        I'll handle unknown currencies first. This way, if someone asks
        for ABC to ABC is not in the input, I return -1 instead of 1
    """
    if from_currency not in graph or to_currency not in graph:
        return -1.0
    
    queue = deque([(from_currency, 1.0)])
    visited = {from_currency}
    
    """
        I'll run BFS from the source currency. Along the way, I'll keep
        the accumulated conversion rate from the source
    """
    while queue:
        current_currency, current_rate = queue.popleft()
        
        if current_currency == to_currency:
            return current_rate
        
        for next_currency, edge_rate in graph[current_currency]:
            if next_currency in visited:
                continue
            visited.add(next_currency)
            
            """
                When I move to the next currency, I multiply the rate so
                far by the edge conversion rate
            """
            next_rate = current_rate * edge_rate
            queue.append((next_currency, next_rate))
    """
        If BFS finishes and we never reach the target currency, then
        there is no valid conversion path
    """      
    return -1.0
