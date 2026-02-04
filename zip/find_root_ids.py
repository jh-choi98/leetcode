from collections import defaultdict
from typing import Dict, List

def findRootID(blocks: List[Dict]) -> List[str]:
    id_set = set()
    res = []
    for block in blocks:
        id_set.add(block["id"])
        if block["parentId"] is None:
            res.append(block["id"])
    
    for block in blocks:
        if block["parentId"] and block["parentId"] not in id_set:
            res.append(block["id"])
        
    return res
    
def findPath(blocks: List[Dict], target: str) -> List[str]:
    childToParent = defaultdict(str)
    for block in blocks:
        childToParent[block["id"]] = block["parentId"]
        
    path_reverse = []
    
    cur_id = target
    while cur_id and cur_id in childToParent:
        path_reverse.append(cur_id)
        cur_id = childToParent[cur_id]
        
    return path_reverse[::-1]




def findRootIDSol(blocks: List[Dict]) -> List[str]:
    id_set = {block["id"] for block in blocks}
    
    roots = []
    for block in blocks:
        parent_id = block.get("parentId")
        if parent_id is None or parent_id not in id_set:
            roots.append(block["id"])
    
    return roots

# Cycle detection
def findPathSol(blocks: List[Dict], target: str) -> List[str]:
    parent_map = {block["id"]: block["parentId"] for block in blocks}
    
    path = []
    current_id = target
    visited = set()
    
    while current_id is not None and current_id in parent_map:
        if current_id in visited:
            print(f"Cycle detected at {current_id}")
            break
        
        path.append(current_id)
        visited.add(current_id)
        current_id = parent_map[current_id]

    return path[::-1]



if __name__ == "__main__":
    blocks = [
  { "id": "A", "parentId": None },
  { "id": "B", "parentId": "A" },
  { "id": "C", "parentId": "A" },
  { "id": "D", "parentId": "B" },
  { "id": "E", "parentId": "Z" },
  { "id": "F", "parentId": None },
  { "id": "G", "parentId": "F" }
    ]
    path = findPath(blocks, "D")
    print(path)

    blocks2 = [
  { "id": "Node-1", "parentId": None },
  { "id": "Node-2", "parentId": "Node-1" },
  { "id": "Node-3", "parentId": "Node-2" },
  { "id": "Node-4", "parentId": "Node-3" },
  { "id": "Node-5", "parentId": "Ghost-99" },
  { "id": "Node-6", "parentId": "Node-5" },
  { "id": "Node-7", "parentId": "Node-6" },
  { "id": "Node-8", "parentId": None },
  { "id": "Node-9", "parentId": "Node-8" },
  { "id": "Node-10", "parentId": "Node-8" }
]
    path2 = findPath(blocks2, "Node-4")
    path3 = findPath(blocks2, "Node-7")
    print(path2)
    print(path3)


