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
        
    def insert(self, emp_id, name, role, manager_id, working_years):
        if emp_id in self.employees:
            raise ValueError("Already exists")
        
        if manager_id is not None and manager_id not in self.employees:
            raise ValueError("Manager does not exist")
        
        if manager_id is not None and self.employees[manager_id].role != MANAGER:
            raise ValueError("Invalid Manger ID")
        
        self.employees[emp_id] = Employee(emp_id, name, role, manager_id, working_years)
        
        if manager_id is not None:
            self.reports[manager_id].add(emp_id)
    
    def delete(self, emp_id):
        if emp_id not in self.employees:
            return
        
        if self.reports[emp_id]:
            raise ValueError(f"Employee {emp_id} still has reports")
        
        emp: Employee = self.employees[emp_id]
        
        if emp.manager_id is not None:
            self.reports[emp.manager_id].remove(emp_id)
            
        del self.employees[emp_id]
        self.reports.pop(emp_id, None)
    
    def get_avg_working_years_bfs(self, emp_id):
        if emp_id not in self.employees or self.employees[emp_id].role != MANAGER:
            raise ValueError("Invalid emp_id")
        
        total = 0
        count = 0
        queue = deque(self.reports[emp_id])
        
        while queue:
            cur = queue.popleft()
            total += self.employees[cur].working_years
            count += 1
            for report_id in self.reports[cur]:
                queue.append(report_id)

        return total / count if count else 0.0
                
            
