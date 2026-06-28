from collections import defaultdict, deque

MANAGER = "Manager"
DEVELOPER = "Developer"

class Employee:
    def __init__(self, emp_id, name, role, manager_id, working_years):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.manager_id = manager_id
        self.working_years = working_years

class Directory:
    def __init__(self):
        self.employees = {}
        self.reports = defaultdict(set)
    
    # Time: O(1)
    def insert(self, emp_id, name, role, manager_id, working_years):
        if emp_id in self.employees:
            raise ValueError("Already exists")
        if manager_id is not None and manager_id not in self.employees:
            raise ValueError(f"Manager {manager_id} does not exist")
        
        self.employees[emp_id] = Employee(emp_id, name, role, manager_id, working_years)
        if manager_id is not None:
            self.reports[manager_id].add(emp_id)
            
    # Time: O(1)     
    def delete(self, emp_id):
        if emp_id not in self.employees:
            raise ValueError(f"Employee {emp_id} does not exist")
        
        if self.reports[emp_id]:
            raise ValueError(f"Employee {emp_id} still has reports")
        
        emp = self.employees[emp_id]
        if emp.manager_id is not None:
            self.reports[emp.manager_id].remove(emp_id)
            
        del self.employees[emp_id]
        self.reports.pop(emp_id, None)

    # Time: O(k), where k = size of subtree under emp_id
    # Space: O(w), where w = max width of the subtree
    def avg_working_years_bfs(self, emp_id):
        if emp_id not in self.employees:
            raise ValueError("Does not exist")
        
        # BFS over the subtree rooted at emp_id, excluding emp_id itself
        total = 0
        count = 0
        queue = deque(self.reports[emp_id])
        while queue:
            cur = queue.popleft()
            total += self.employees[cur].working_years
            count += 1
            queue.extend(self.reports[cur])
            # for report_id in self.reports[cur]:
            #     queue.append(report_id)
            
        return total / count if count else 0.0
    
    def avg_working_years_dfs_stack(self, emp_id):
        if emp_id not in self.employees or self.employees[emp_id].role != MANAGER:
            raise ValueError("Invalid emp_id")
        
        total = 0
        count = 0
        stack = list(self.reports[emp_id])
        while stack:
            cur = stack.pop()
            total += self.employees[cur].working_years
            count += 1
            for report_id in self.reports[cur]:
                stack.append(report_id)
                
        return total / count if count else 0.0
    
    def avg_working_years_dfs_recursion(self, emp_id):
        if emp_id not in self.employees or self.employees[emp_id].role != MANAGER:
            raise ValueError("Invalid emp_id")
        
        def dfs(eid):
            total, count = 0, 0
            for report_id in self.reports[eid]:
                total += self.employees[eid].working_years
                count += 1
                sub_total, sub_count = dfs(report_id)
                total += sub_total
                count += count
            return total, count
        
        total, count = dfs(emp_id)
        return total / count if count else 0.0

"""
Time Complexity — 셋 다 O(k)
세 방식 모두 **O(k)**예요. k = emp_id의 subtree 크기 (후손 수). 어떤 순회든 각 노드를 정확히 한 번씩 방문하고, 각 노드에서 하는 일(working_years 더하기, 자식 큐/스택에 넣기)이 상수 시간이라 동일해요. 최악의 경우(emp_id가 루트라 subtree = 전체)는 O(n).
순회 순서만 다를 뿐 방문하는 노드 수는 같으니, time은 셋 다 차이 없어요.

Space Complexity
BFS (queue)     O(w)    max width
DFS (stack)     O(h)    max height/depth
DFS (recursion) O(h)    max height/depth
"""
