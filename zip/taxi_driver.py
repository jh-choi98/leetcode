from collections import defaultdict, deque
from typing import Dict, List, Tuple


def find_shortest_path_infinite(start: Tuple[int, int], 
                                destination: Tuple[int, int], 
                                barriers: List[Tuple[int, int]]) -> str:
    if start == destination:
        return ""
    
    barriers_set = set(barriers)
    visited = set([start])
    directions = [(0, 1, 'N'), (0, -1, 'S'), (1, 0, 'E'), (-1, 0, 'W')]
    
    if destination in barriers_set:
        return ""
    
    queue = deque([(start[0], start[1], "")])
    
    while queue:
        r, c, path = queue.popleft()
        
        for dr, dc, move_char in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) == destination:
                return path + move_char
            
            if (nr, nc) not in barriers_set and (nr, nc) not in visited:
                queue.append((nr, nc, path + move_char))
                visited.add((nr, nc))
                
    return ""

import heapq
from collections import defaultdict
from typing import List, Tuple, Dict, Set

def shortestPathWithParades(start: Tuple[int, int],
                            goal: Tuple[int, int],
                            barriers: List[Tuple[int, int]],
                            parades: List[Dict]) -> Tuple[List[str], int]:
    """
    Solves the Shortest Path problem with dynamic obstacles (Parades) using A* Search.
    
    Strategy:
    1. Preprocess parades into row/col lookups for O(1) collision checks.
    2. Use A* algorithm with Manhattan distance heuristic to handle the infinite grid.
    3. State is defined as (x, y, time).
    
    parades = [
    { "start": (0, 1), "dir": "E" },
    { "start": (3, 5), "dir": "N" },
    { "start": (10, -2), "dir": "W" },
    ...
]
    """
    
    # --- 0. Edge Cases ---
    if start == goal:
        return ([], 0)
    
    # --- 1. Preprocessing (Optimization) ---
    # Group parades by their fixed axis (Row or Column) to avoid iterating all parades every step.
    parades_by_row = defaultdict(list)
    parades_by_col = defaultdict(list)
    
    for p in parades:
        # If moving East/West, they stay on the same Row (y).
        if p['dir'] in ('E', 'W'):
            parades_by_row[p['start'][1]].append(p)
        # If moving North/South, they stay on the same Column (x).
        else:
            parades_by_col[p['start'][0]].append(p)

    # Use a Set for O(1) lookup of static barriers.
    barrier_set = set(barriers)

    # --- 2. Collision Check Helper ---
    def is_safe(x: int, y: int, t: int) -> bool:
        """Checks if coordinate (x, y) is safe at time t."""
        
        # A. Check Static Barriers
        if (x, y) in barrier_set:
            return False
        
        # B. Check Dynamic Parades
        # Calculate parade head displacement: floor(t / 2)
        dist = t // 2
        
        # Check horizontal parades on this row (y)
        for p in parades_by_row[y]:
            px = p['start'][0]
            direction = p['dir']
            
            if direction == 'E':
                head_x = px + dist
                # Eastward parade occupies the ray starting at head extending East (x >= head)
                if x >= head_x: return False
            elif direction == 'W':
                head_x = px - dist
                # Westward parade occupies the ray starting at head extending West (x <= head)
                if x <= head_x: return False

        # Check vertical parades on this column (x)
        for p in parades_by_col[x]:
            py = p['start'][1]
            direction = p['dir']
            
            if direction == 'N':
                head_y = py + dist
                # Northward parade occupies the ray starting at head extending North (y >= head)
                if y >= head_y: return False
            elif direction == 'S':
                head_y = py - dist
                # Southward parade occupies the ray starting at head extending South (y <= head)
                if y <= head_y: return False
                
        return True

    # --- 3. A* Algorithm Setup ---
    
    # Check if start position is safe at t=0
    if not is_safe(start[0], start[1], 0):
        return ([], -1)
    
    # Heuristic: Manhattan Distance (Best for grid based paths)
    def heuristic(x, y):
        return abs(x - goal[0]) + abs(y - goal[1])
    
    # Priority Queue stores: (f_score, time, x, y, state_id)
    # f_score = g_score (time) + h_score (heuristic)
    pq = []
    
    # Parent tracking for path reconstruction (memory efficient)
    # Key: (x, y, t), Value: (parent_x, parent_y, parent_t, move_cmd)
    parent = {}
    start_state = (start[0], start[1], 0)
    parent[start_state] = None
    
    start_h = heuristic(start[0], start[1])
    # Push start state: (f_score, time, x, y)
    heapq.heappush(pq, (start_h, 0, start[0], start[1]))
    
    # Possible moves: 4 directions + WAIT
    # (dx, dy, move_command)
    moves = [
        (0, 1, 'N'), (0, -1, 'S'), (1, 0, 'E'), (-1, 0, 'W'), 
        (0, 0, 'WAIT') # Waiting is a valid move to avoid parades
    ]
    
    while pq:
        # Pop the state with the lowest estimated cost (f_score)
        _, curr_time, x, y = heapq.heappop(pq)
        
        # Goal Check
        if (x, y) == goal:
            # Reconstruct path from parent pointers
            path = []
            state = (x, y, curr_time)
            while parent[state] is not None:
                prev_x, prev_y, prev_t, cmd = parent[state]
                path.append(cmd)
                state = (prev_x, prev_y, prev_t)
            path.reverse()
            return (path, curr_time)
        
        # Explore neighbors
        next_time = curr_time + 1
        
        for dx, dy, cmd in moves:
            nx, ny = x + dx, y + dy
            next_state = (nx, ny, next_time)
            
            # Optimization: Check visited before complex safety checks
            if next_state in parent:
                continue
                
            # Check if the next cell is valid at the NEXT time step
            if is_safe(nx, ny, next_time):
                parent[next_state] = (x, y, curr_time, cmd)
                
                # Calculate A* scores
                new_h = heuristic(nx, ny)
                new_f = next_time + new_h
                
                heapq.heappush(pq, (new_f, next_time, nx, ny))
                
    # If queue is empty and goal not reached
    return ([], -1)
