from collections import deque

# BFS
"""
    Time: O(V + E), where V is the number of profiles and E is the
    number of friendship relationships. 
    BFS visits each profile at most once and checks each friendship edge
    at most once. 
    
    Space: O(V) because we store the visited set, parent map, queue, and the final path.
"""
def find_path_bfs(g, start, end):
    if start == end:
        return [start]
    
    visited = {start}
    parent = {start: None}
    queue = deque([start])
    
    while queue:
        cur = queue.popleft()
        
        for friend in g.get(cur, []):
            if friend in visited:
                continue
            
            visited.add(friend)
            parent[friend] = cur
            
            if friend == end:
                path = []
                node = end
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return path[::-1]
            queue.append(friend)
            
    return []

         
def test1():
    graph = {
        "Gordon":  {"Shantel"},
        "Shantel": {"Gordon", "Maria"},
        "Maria":   {"Shantel", "David"},
        "David":   {"Maria", "Stephen"},
        "Stephen": {"David"},
        "Alice":   {"Bob"},          # disconnected from Gordon
        "Bob":     {"Alice"},
    }

    # normal path
    assert find_path_bfs(graph, "Gordon", "Stephen") == ["Gordon", "Shantel", "Maria", "David", "Stephen"]
    # start == end
    assert find_path_bfs(graph, "Gordon", "Gordon") == ["Gordon"]
    # direct friends
    assert find_path_bfs(graph, "Gordon", "Shantel") == ["Gordon", "Shantel"]
    # no path (separate friend group)
    assert find_path_bfs(graph, "Gordon", "Alice") == []

    print("All tests passed")

test1()


"""
    Time: O(V + E) + path copy cost
        Worst-case: O(V^2 + E)
    Space: O(V^2) worst-case from copied path lists over recursion calls, or O(V) active recursion/path depth
"""
def find_path_dfs_recurison(g, start, end):
    visited = set()
    
    def dfs(cur, path):
        if cur == end:
            return path
        visited.add(cur)
        for friend in g.get(cur, []):
            if friend not in visited:
                result = dfs(friend, path + [friend])
                if result:
                    return result
        return[]
    return dfs(start, [start])
        
def test2():
    graph = {
        "Gordon":  {"Shantel"},
        "Shantel": {"Gordon", "Maria"},
        "Maria":   {"Shantel", "David"},
        "David":   {"Maria", "Stephen"},
        "Stephen": {"David"},
        "Alice":   {"Bob"},          # disconnected from Gordon
        "Bob":     {"Alice"},
    }

    # normal path
    assert find_path_dfs_recurison(graph, "Gordon", "Stephen") == ["Gordon", "Shantel", "Maria", "David", "Stephen"]
    # start == end
    assert find_path_dfs_recurison(graph, "Gordon", "Gordon") == ["Gordon"]
    # direct friends
    assert find_path_dfs_recurison(graph, "Gordon", "Shantel") == ["Gordon", "Shantel"]
    # no path (separate friend group)
    assert find_path_dfs_recurison(graph, "Gordon", "Alice") == []

    print("All tests passed")

test2()

"""
    Time: O(V + E)
    Space: O(V)
"""
def find_path_dfs_stack(g, start, end):
    if start == end:
        return [start]
    
    visited = {start}
    parent = {start: None}
    stack = [start]
    
    while stack:
        cur = stack.pop()
        
        for friend in g.get(cur, []):
            if friend in visited:
                continue
            visited.add(friend)
            parent[friend] = cur
            if friend == end:
                path = []
                node = end
                while node is not None:
                    path.append(node)
                    node = parent[node]
                
                return path[::-1]
            
            stack.append(friend)
    return []
        
def test3():
    graph = {
        "Gordon":  {"Shantel"},
        "Shantel": {"Gordon", "Maria"},
        "Maria":   {"Shantel", "David"},
        "David":   {"Maria", "Stephen"},
        "Stephen": {"David"},
        "Alice":   {"Bob"},          # disconnected from Gordon
        "Bob":     {"Alice"},
    }

    # normal path
    assert find_path_dfs_stack(graph, "Gordon", "Stephen") == ["Gordon", "Shantel", "Maria", "David", "Stephen"]
    # start == end
    assert find_path_dfs_stack(graph, "Gordon", "Gordon") == ["Gordon"]
    # direct friends
    assert find_path_dfs_stack(graph, "Gordon", "Shantel") == ["Gordon", "Shantel"]
    # no path (separate friend group)
    assert find_path_dfs_stack(graph, "Gordon", "Alice") == []

    print("All tests passed")

test3()
