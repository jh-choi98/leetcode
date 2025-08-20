# DFS

## Concept
DFS is a graph/tree traversal algorithm that explores as far as possible
along each branch before backgracking. It goes deep into one path until
it can't go further, then backtracks and explores other paths.

## Key Characteristics
- Uses a stack data structure (or recursion which uses call stack)
- Does not guarantee shortest path
- T: O(V + E)
- S: O(V)
- Better for exploring all possible paths or finding any path

## How It Works
1. Start at root node and mark it as visited
2. Explore one neighbor completely before moving to next neighbor
3. When struck (no visited neighbors), backtrack
4. Repeat until all reachable nodes are visited

