from typing import Optional


class Employee:
    def __init__(self, name):
        self.name = name
        self.manager: Optional[Employee] = None
        self.direct_reports = []
        
    def __repre__(self):
        return self.name
    
class OrgChart:
    def __init__(self):
        """
            I'll use a dictionary for name-based lookup.
            In a production system, this would likely be employee ID
            instead of name
        """
        self.employees: dict[str, Employee] = {}
        
    def get_or_create_employee(self, name) -> Employee:
        if name not in self.employees:
            self.employees[name] = Employee(name)
        
        return self.employees[name]
    
    def add_employee(self, employee_name, manager_name=None) -> Employee:
        employee = self.get_or_create_employee(employee_name)
        
        if manager_name is None:
            return employee
        
        manager = self.get_or_create_employee(manager_name)
        
        if employee is manager:
            raise ValueError("An employee cannot manage themselves")
        
        if employee.manager is not None and employee.manager is not manager:
            raise ValueError(f"{employee_name} already has a different manager")
        
        """
            Since I'm designing the org chart API, I want to prevent
            cycles when assigning a manager. If the proposed manager
            already reports, directly or indirectly, to this employee,
            then this assignment would create a cycle
        """
        if self._would_create_cycle(employee, manager):
            raise ValueError("This manager assignment would create a cycle")
        
        employee.manager = manager
        
        if employee not in manager.direct_reports:
            manager.direct_reports.append(employee)
        
        return employee
        
    def _would_create_cycle(self, employee, proposed_manager) -> bool:
        current = proposed_manager
        
        while current is not None:
            if current is employee:
                return True
            current = current.manager
        return False

    def first_common_manager(self, name1, name2) -> Optional[Employee]:
        if name1 not in self.employees or name2 not in self.employees:
            raise ValueError("Both employees must exist in the org chart")
        
        return find_first_common_manager(self.employees[name1], self.employees[name2])
    
def find_first_common_manager(e1, e2) -> Optional[Employee]:
    managers_seen = set()
    
    current = e1.manager
    
    """
        First, I'll walk up the first employee's manager chain and store
        all managers in a set. I'm assuming the org chart API has
        already enforeced that this chain has no cycle
    """
    while current is not None:
        managers_seen.add(current)
        current = current.manager
    
    current = e2.manager
    
    """
        Then I walk up from the second employee. The first manager that
        appears in the set is the closest common manager
    """
    while current is not None:
        if current in managers_seen:
            return current
        current = current.manager
    return None

"""
    - Time:
        - add_employee time: O(h), worst-case O(n)
        - first_common_manager time: O(h1 + h2), or O(h), worst-case O(n)
        
        “Building or adding an employee takes O(h) time because I check
        whether the manager assignment would create a cycle. Looking up
        the first common manager takes O(h1 + h2) time, since I may walk
        from both employees up to the root. If we define h as the height
        of the org chart, that is O(h), and in the worst case h can be
        n.”
        
    - Space:
        - OrgChart storage: O(n)
        - Lookup time: O(h), worst-case O(n)
        - Lookup extra space: O(h), worst-case O(n)
        where n is the number of employees and h is the height of the
        org chart
        
        “The org chart data structure itself stores all employees, so it
        uses O(n) space. For the common manager lookup operation, the
        additional space is O(h), because I only store one employee’s
        manager chain. In the worst case, h can be n.”
"""
