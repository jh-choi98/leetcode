from typing import Optional


class Employee:
    def __init__(self, name):
        self.name = name
        self.manager: Optional[Employee] = None
        self.direct_reports = []
        
class OrgChart:
    def __init__(self):
        self.employees: dict[str, Employee] = {}
        
    def get_or_create_employee(self, name) -> Employee:
        if name not in self.employees:
            self.employees[name] = Employee(name)
            
        return self.employees[name]
    
    def add_employee(self, emp_name, mang_name=None) -> Employee:
        employee = self.get_or_create_employee(emp_name)
        
        if mang_name is None:
            return employee
        
        manager = self.get_or_create_employee(mang_name)
        
        if employee is manager:
            raise ValueError("An employee cannot manage themselves")
        
        if employee.manager is not None and employee.manager is not manager:
            raise ValueError(f"{emp_name} already has a different manager")
        
        if self._would_create_cycle(employee, manager):
            raise ValueError("This manager assignment would create a cycle")
        
        employee.manager = manager
        
        if employee not in manager.direct_reports:
            manager.direct_reports.append(employee)
        
        return employee
        
    def _would_create_cycle(self, employee, manager) -> bool:
        current = manager
        
        while current is not None:
            if current is employee:
                return True
            current = current.manager
        return False
    
    def first_common_manager(self, n1, n2) -> Optional[Employee]:
        if n1 not in self.employees or n2 not in self.employees:
            raise ValueError("Both employees must exist in the org chart")
        
        return find_first_common_manager(self.employees[n1], self.employees[n2])
    
def find_first_common_manager(e1, e2) -> Optional[Employee]:
    managers_seen = set()
    
    current = e1.manager
    
    while current is not None:
        managers_seen.add(current)
        current = current.manager
        
    current = e2.manager
    
    while current is not None:
        if current in managers_seen:
            return current
        current = current.manager
    return None
