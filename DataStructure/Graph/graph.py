"""
1. Key Terminology
- Vertex (Node): The individual data point
- Edge: The connection between two vertices
- Undirected Graph: Edges have no direction (like a two-way street or a mutual friendship)
- Directed Graph (Digraph): Edges have a direction (like a one-way
  street or a hyperlink)
- Weighted Graph: Edges have a value/cost (e.g., distance between cities
  in miles)

2. How to Represent a Graph in Code
- Adjacency Matrix
    A 2D array (grid) where rows and columns represent vertices. If
    there is an edge between row i and column j, we put a 1 (or the
    weight)
    - Pros: Fast lookup (is A connected to B? O(1))
    - Cons: Takes up huge space (V^2), mostly empty if connections are few

- Adjacency List
    We use a Dictionary (Hash Map) or an Array of Lists. Each vertex is a key, and its value is a list of all vertices it connects to
    - Pros: Space-efficient for most real-world graphs
    - Cons: Slightly slower to check if a specific edge exists
    
    
암기 포인트

BFS = 최단 거리, 레벨 순회 → deque + visited는 넣을 때 체크
DFS = 모든 경로, 백트래킹 → stack 또는 재귀
Directed Graph Cycle = 3가지 상태 (미방문/방문중/완료)
Undirected Graph Cycle = parent 체크
Topological Sort = indegree 0인 것부터
그리드 = dr, dc = [(0,1), (0,-1), (1,0), (-1,0)]
"""

from collections import deque

# Adjacency List
class Graph:
    def __init__(self):
        self.adj_list: dict[str, list[str]] = {}

    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            
    def add_edge(self, v1: str, v2: str) -> None:
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
            
        # undirected
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
    
    def dispaly(self) -> None:
        for v, n in self.adj_list.items():
            print(f"{v} -> {n}")
    

# ============================================================
# 1. BFS 기본 - 레벨 탐색, 최단 거리
# ============================================================ 
def bfs(g: dict[str, list[str]], start: str) -> list[str]:
    visited = {start}
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for n in g[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return result
        
# ============================================================
# 2. DFS 기본 - 경로 탐색, 백트래킹
# ============================================================
def dfs_iterative(g: dict[str, list[str]], start: str) -> list[str]:
    visited = set()
    stack = [start]
    result = []
    
    while stack:
           node = stack.pop()
           if node in visited:
               continue
           visited.add(node)
           result.append(node)
           for n in g[node]:
               if n not in visited:
                   stack.append(n)
                   
    return result
       
def dfs_recursive(g: dict[str, list[str]], start: str) -> list[str]:
    result = []
    visited = set()
    
    def dfs(node: str) -> None:
        visited.add(node)
        result.append(node)
        for n in g[node]:
            if n not in visited:
                dfs(n)
    
    dfs(start)
    return result
    
# ============================================================
# 3. 최단 거리 (BFS) - 가중치 없는 그래프
# ============================================================
def shortest_path(g: dict[str, list[str]], start: str, end: str) -> int:
    if start == end:
        return 0
    
    visited = {start}
    queue = deque([(start, 0)])
    
    while queue:
        node, dist = queue.popleft()
        for n in g[node]:
            if n == end:
                return dist + 1
            if n not in visited:
                visited.add(n)
                queue.append((n, dist + 1))
    
    return -1
    
# ============================================================
# 4. 경로 복원 - 어떻게 왔는지 추적
# ============================================================
def find_path(g: dict[str, list[str]], start: str, end: str) -> list[str]:
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        for n in g[node]:
            if n == end:
                return path + [n]
            if n not in visited:
                visited.add(n)
                queue.append((n, path + [n]))
    
    return []

# ============================================================
# 5. 연결 요소 개수 (Connected Components)
# ============================================================
def count_components(n: int, edges: list[list[int]]) -> int:
    graph = {i: [] for i in range(n)}
    for e1, e2 in edges:
        graph[e1].append(e2)
        graph[e2].append(e1)
        
    visited = set()
    count = 0
    
    for node in range(n):
        if node not in visited:
            count += 1
            queue = deque([node])
            visited.add(node)
            while queue:
                cur = queue.popleft()
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
    return count

# ============================================================
# 6. 사이클 탐지 - 무방향 그래프
# ============================================================
def has_cycle_undirected(n: int, edges: list[list[int]]) -> bool:
    graph = {i: [] for i in range(n)}
    for e1, e2 in edges:
        graph[e1].append(e2)     
        graph[e2].append(e1)
    
    visited = set()
    
    def dfs(node: int, parent: int) -> bool:
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei, node):
                    return True
            elif nei != parent: # 부모가 아닌데 이미 방문 = 사이클
                return True
        return False
    
    for node in range(n):
        if node not in visited:
            if dfs(node, -1):
                return True
            
    return False

# ============================================================
# 7. 사이클 탐지 - 방향 그래프 (3가지 상태)
# ============================================================
def has_cycle_directed(n: int, edges: list[list[int]]) -> bool:
    graph = {i : [] for i in range(n)}
    for e1, e2 in edges:
        graph[e1].append(e2)
    
    # 0: 미방문, 1: 방문 중 (현재 경로), 2: 완료
    state = [0] * n
    
    def dfs(node: int) -> bool:
        state[node] = 1
        for nei in graph[node]:
            if state[nei] == 1: # 현재 경로에서 다시 만남 = 사이클
                return True
            if state[nei] == 0 and dfs(nei):
                return True
        state[node] = 2
        return False
    
    for node in range(n):
        if state[node] == 0:
            if dfs(node):
                return True
    return False

# ============================================================
# 8. 위상 정렬 (Topological Sort) - Kahn's Algorithm
# ============================================================
def topological_sort(n: int, edges: list[list[int]]) -> list[int]:
    # edges = [[a, b], ...] = a -> b 의존 관계. 사이클 있으면 빈 리스트
    graph = {i: [] for i in range(n)}
    indegree = [0] * n
    
    for e1, e2 in edges:
        graph[e1].append(e2)
        indegree[e2] += 1
        
    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
                
    return result if len(result) == n else []

# ============================================================
# 9. 이분 그래프 판별 (Bipartite Check)
# ============================================================
def is_bipartite(n: int, edges: list[list[int]]) -> bool:
    graph = {i: [] for i in range(n)}
    for e1, e2 in edges:
        graph[e1].append(e2)
        graph[e2].append(e1)
        
    color = [-1] * n # -1: 미방문, 0/1: 두 그룹
    
    for start in range(n):
        if color[start] != -1:
            continue
        
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if color[nei] == -1:
                    color[nei] = 1 - color[node]
                    queue.append(nei)
                elif color[nei] == color[node]:
                    return False
    return True
        
# ============================================================
# 10. 2D 그리드 BFS - 섬 개수, 최단 경로 등
# ============================================================
def num_islands(grid: list[list[str]]) -> int:
    """'1'은 땅, '0'은 물. 섬 개수 반환"""
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def bfs(r: int, c: int) -> None:
        queue = deque([(r, c)])
        grid[r][c] = '0'
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))
                    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                bfs(r, c)
    return count

# ============================================================
# 11. 2D 그리드 DFS
# ============================================================
def num_island(grid: list[list[str]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    count = 0
    
    def dfs(r: int, c: int) -> None:
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
            return
        
        grid[r][c] = "0"
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc)
            
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    return count
