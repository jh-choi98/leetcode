from collections import defaultdict


# DFS
"""
    Time: O(V + E)
    Space: (V)
"""
def install_order_dfs(packages, get_dependencies):
    """
    packages: a single package (str) or a list of packages to install
    get_dependencies(pkg): returns the list of packages that pkg directly depends on
    Returns installation order (dependencies before dependents).
    Raises ValueError on circular dependency.
    """
    
    if isinstance(packages, str):
        packages = [packages]
        
    order = []
    visited = set() # fully processed
    in_progress = set() # on the current DFS path - for cycle detection
    
    def dfs(pkg):
        if pkg in visited:
            return
        if pkg in in_progress:
            raise ValueError(f"Circular dependency at {pkg}")
        
        in_progress.add(pkg)
        for dep in get_dependencies(pkg):
            dfs(dep)
            
        in_progress.discard(pkg)
        visited.add(pkg)
        order.append(pkg)
    
    for pkg in packages:
        dfs(pkg)
        
    return order

# BFS, in-degree (Kahn's algorithm)
"""
    Time: O(V + E)
    Space: (V + E)
"""
from collections import defaultdict, deque

def install_order_kahn(packages, get_dependencies):
    if isinstance(packages, str):
        packages = [packages]

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    all_pkgs = set()

    stack = list(packages)
    seen = set()
    while stack:
        pkg = stack.pop()
        if pkg in seen:
            continue
        seen.add(pkg)
        all_pkgs.add(pkg)
        deps = set(get_dependencies(pkg))   # dedupe: a dependency relation is unique
        in_degree[pkg] += len(deps)
        for dep in deps:
            graph[dep].append(pkg)
            all_pkgs.add(dep)
            stack.append(dep)

    queue = deque(p for p in all_pkgs if in_degree[p] == 0)
    order = []
    while queue:
        pkg = queue.popleft()
        order.append(pkg)
        for dependent in graph[pkg]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    if len(order) != len(all_pkgs):
        raise ValueError("Circular dependency detected")

    return order
