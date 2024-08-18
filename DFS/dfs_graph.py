# def dfs_recursive(graph, node, visited=None):
#     if not visited:
#         visited = set()

#     # 현재 노드를 방문으로 표시하고 출력
#     visited.add(node)
#     print(node, end=" ")

#     # 인접한 노드들에 대해 재귀적으로 DFS 수행
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs_recursive(graph, neighbor, visited)


# def dfs_iterative(graph, start):
#     visited = set()
#     stack = [start]

#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#             print(node, end=" ")

#             for neighbor in reversed(graph[node]):
#                 if neighbor not in visited:
#                     stack.append(neighbor)
