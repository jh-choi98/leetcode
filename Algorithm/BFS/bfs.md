# BFS (Breadth-First Search)

## Concept
BFS is a graph/tree traversal algorithm that explores nodes level by
level, visiting all nodes at the current depth before moving to nodes at
the next dept level. 

## Key Characteristics
- Uses a Queue (FIFO)
- Guarantees the shortest path in unweighted graphs
- Time: O(V + E), V is vertices and E is edges
- Space: O(V)

## How It Works
1. Start with a root node and add it to the queue
2. Mark the node as visited
3. While the queue is not empty:
    - Dequeue a node from the front
    - Process the node
    - Enqueue all unvisited neighbors
    - Mark neighbors as visited

## Common BFS Applications
Shortest path finding, Level-order traversal, Connected components
(finding all connected nodes in a graph), Minimum steps problems
(finding minimum operations to reach a target), Social networks(finding
friends at k-degrees of separation)

## When to Use BFS
- When you need the shortest path in an unweighted graph
- When exploring nodes by distance/levels from a source
- When you need to visit all nodes at the same depth before going deeper
- In problems involving minimum steps/operations
