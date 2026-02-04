"""
Since the environment is a Tree (no cycles) and Jerry cannot revisit
nodes, the optimal strategy for Jerry is to escape to a node where he
can arrive strictly earlier than Tom. Among all such reachable nodes,
Jerry picks the one that is furthest from Tom to delay the capture as
long as possible.

1. Graph construction
    - The input gives us Node objects that only contain references to
      their children. This represents a directed structure (Top-down)
    - The code first converts the tree into an undirected adjacency list
    
2. Distance calculation (BFS)
   - Determine the minimum time (steps) it takes for Tom and Jerry to
   reach every node in the tree
   -  BFS is used because it guarantees the shortest path in an
   unweighted graph
        - tom_dist: Maps every Node -> Minimum steps from Tom's start
        - jerry_dist: Maps every Node -> Minimum steps from Jerry's
          start
    - We need these two baselines to compare who can reach a specific
      node faster
    
3. The "Safe Zone" Strategy (Core Logic)
    - For Jerry to safely pass through or arrive at a node v, he must
      get there strictly before Tom
        - jerry_dist[v] < tom_dist[v]
            Jerry arrives first. He can use this node to escape further
        - jerry_dist[v] >= tom_dist[v]
            Tom arrives at the same time (capture) or earlier (blocking
            the path). Jerry cannot safely reach this node
"""

from collections import defaultdict, deque
from typing import Dict, List, Optional, Set

class Node:
    def __init__(self, children=None):
        self.children = children if children else []

# Time: O(n)
# We traverse the tree once to build the graph, run BFS twice, and
# iterate through the nodes one last time. Since the nubmer of edges in
# a tree is N - 1, all these operations are proportional to the number
# of nodes N
# Space: O(n)
# We store the adjacency list, distance maps, and recursion stack(or
# queue), which all scale linearly with N
def get_min_steps_to_catch(root: Node, tom: Node, jerry: Node) -> int:
    if tom is jerry:
        return 0
    
    # Build the graph
    # Key: Node, Value: List of neighbor Nodes
    neighbors: Dict[Node, List[Node]] = defaultdict(list)
    stack = [root]
    visited: Set[Node] = {root}
    
    while stack:
        cur = stack.pop()
        
        for child in cur.children:
            if child not in visited:
                visited.add(child)
                stack.append(child)
                
                neighbors[cur].append(child)
                neighbors[child].append(cur)
                    
    # Calculate BFS distance from both Tom and Jerry
    # Time: O(n)
    # Space: o(n)
    def bfs(start: Node) -> Dict[Node, int]:
        dist: Dict[Node, int] = {start: 0}
        queue = deque([start])
        while queue:
            x = queue.popleft()
            for nx in neighbors.get(x, []):
                if nx not in dist:
                    dist[nx] = dist[x] + 1
                    queue.append(nx)
        return dist
    
    tom_dist = bfs(tom)
    jerry_dist = bfs(jerry)
    
    # Determine the maximum time Jerry can survice
    # Logic: Jerry can only safely reach nodes where he arrives strictly
    # earlier than Tom (jerry_dist < tom_dist). Among these ssafe nodes,
    # Jerry chooses the one that takes Tom the longest time to reach
    # (maximizing the gram duration)
    ans = 0
    for v in neighbors.keys():
        if v in tom_dist and v in jerry_dist:
            if jerry_dist[v] < tom_dist[v]:
                ans = max(ans, tom_dist[v])
    
    return ans
