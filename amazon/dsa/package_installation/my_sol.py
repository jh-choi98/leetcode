# DFS
def install_order_dfs(packages, get_dependencies):
    if isinstance(packages, str):
        packages = [packages]
        
    visited = set()
    in_progress = set()
    order = []
    
    def dfs(pkg):
        if pkg in visited:
            return
        if pkg in in_progress:
            raise ValueError(f"cycle dependencies at {pkg}")
        
        in_progress.add(pkg)
        for dep in get_dependencies(pkg):
            dfs(dep)
            
        in_progress.discard(pkg)
        visited.add(pkg)
        order.append(pkg)
    
    for pkg in packages:
        dfs(pkg)
        
    return order





# def test():
#     deps = {
#         "A": ["B"],
#         "B": ["C"],
#         "C": [],
#         "D": [],
#     }
#     get_dependencies = lambda pkg: deps.get(pkg, [])

#     for fn in (install_order_dfs, install_order_kahn):
#         order = fn("A", get_dependencies)
#         # valid if every dependency appears before the package that needs it
#         pos = {p: i for i, p in enumerate(order)}
#         for pkg, ds in deps.items():
#             if pkg in pos:
#                 for d in ds:
#                     assert pos[d] < pos[pkg], f"{d} should come before {pkg}"
#         print(fn.__name__, "->", order)

#     # cycle case
#     cyclic = {"A": ["B"], "B": ["A"]}
#     get_cyclic = lambda pkg: cyclic.get(pkg, [])
#     for fn in (install_order_dfs, install_order_kahn):
#         try:
#             fn("A", get_cyclic)
#             print(fn.__name__, "-> FAILED to detect cycle")
#         except ValueError:
#             print(fn.__name__, "-> cycle detected ✓")

# test()
