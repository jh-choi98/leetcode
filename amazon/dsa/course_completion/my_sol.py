from collections import defaultdict, deque
from typing import Optional


def can_complete_all_courses(prerequisites: list[tuple[str, str]]) -> bool:
    graph: dict[str, set[str]] = defaultdict(set)
    courses = set()
    
    for course, preq in prerequisites:
        if course == preq:
            return False
        
        graph[course].add(preq)
        courses.add(course)
        courses.add(preq)
        
    # 0 = unvisited
    # 1 = visiting
    # 2 = fully processed
    state: dict[str, int] = {}
    
    def has_cycle(course: str) -> bool:
        if state.get(course, 0) == 1:
            return True
        
        if state.get(course, 0) == 2:
            return False
        
        state[course] = 1
        
        for preq in graph[course]:
            if has_cycle(preq):
                return True
        
        state[course] = 2 
        return False
    
    for course in courses:
        if has_cycle(course):
            return False
        
    return True

prerequisites = [
    ("Python Course", "Systems Course"),
    ("Systems Course", "Python Course"),
    ("Low Level Course", "Python Course"),
]

print(can_complete_all_courses(prerequisites))  # False

def find_course_order(prerequisites: list[tuple[str, str]], all_courses: Optional[list[str]]=None) -> list[str]:
    graph: dict[str, list[str]] = defaultdict(list)
    indegree: dict[str, int] = {}
    
    courses = []
    seen_courses = set()
    
    def add_course(course: str) -> None:
        if course not in seen_courses:
            seen_courses.add(course)
            courses.append(course)
            indegree[course] = 0
            
    if all_courses is not None:
        for course in all_courses:
            add_course(course)
            
    seen_edges = set()
    
    for course, prerequisite in prerequisites:
        if course == prerequisite:
            return []
        
        add_course(course)
        add_course(prerequisite)
        
        edge = (prerequisite, course)
        
        if edge in seen_edges:
            continue
        
        seen_edges.add(edge)
        graph[prerequisite].append(course)
        indegree[course] += 1
        
    queue = deque()
    
    for course in courses:
        if indegree[course] == 0:
            queue.append(course)
            
    order = []
    
    while queue:
        current_course = queue.popleft()
        order.append(current_course)
        
        for next_course in graph[current_course]:
            indegree[next_course] -= 1
            
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    if len(order) != len(courses):
        return []
    
    return order
        
prerequisites = [
    ("Python Course", "Systems Course"),
    ("Low Level Course", "Python Course"),
]

print(find_course_order(prerequisites))
# ['Systems Course', 'Python Course', 'Low Level Course']
