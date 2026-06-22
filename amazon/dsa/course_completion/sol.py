# Topological Ordering / Cycle Detection

# Prerequisite 관계를 directed graph로 만들고, cycle이 있으면 모든
# course를 완료할 수 없다.

"""
    This is a directed graph cycle detection problem
    
    Each course is a node, and each prerequisite relationship is a
    directed edge. If there is a cycle, then at least one course depends
    on itself indirectly, so it is impossible to complete all courses
"""

from collections import defaultdict, deque
from typing import Optional

"""
Let V = the number of courses (node), E = the number of prerequisite
relationships (edge)

- Time: O(V + E)
    We build the graph by processing all prerequisite pairs once, which
    takes O(E). Then DFS visits each course once and checks edge once,
    so the traversal is O(V + E)
    
- Space: O(V + E)
    The graph stores all courses and prerequisite edges. The state
    dictionary stores one entry per course, and the recursion stack can
    go as deep as O(V) in the worst case. So overall space is O(V + E)
"""

# Stateful DFS
def can_complete_all_courses(prerequisites: list[tuple[str, str]]) -> bool:
    """
        I'll model this as a directed graph.
        Each pair is [course, prerequisite], so I'll add an edge from
        the course to its prerequisite
    """
    graph: dict[str, set[str]] = defaultdict(set)
    courses = set()
    
    for course, prerequisite in prerequisites:
        # A course cannot directly depend on itself
        if course == prerequisite:
            return False
        
        graph[course].add(prerequisite)
        courses.add(course)
        courses.add(prerequisite)
        
    # 0 = unvisited
    # 1 = currently visiting
    # 2 = fully processed
    state: dict[str, int] = {}
    
    def has_cycle(course: str) -> bool:
        """
            If I reach a course that is already in the current DFS path,
            that means we found a cycle
        """
        if state.get(course, 0) == 1:
            return True
        """
            If this course was already fully checked before, I don't
            need to process it again
        """
        if state.get(course, 0) == 2:
            return False
        
        state[course] = 1
        
        for prerequisite in graph[course]:
            if has_cycle(prerequisite):
                return True
        
        state[course] = 2
        return False
    
    # The graph may be disconnected, so I need to start DFS from every
    # course
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

# --------------------------------------
# Follow-up: Can you return one valid order to complete the courses?
# --------------------------------------

# Topological Sort

"""
    Input pair is [course, prerequisite]
    So for topological sort, the edge should be:
        Prerequisite -> course
"""

"""
Time: O(V + E):
    We process all courses and prerequisite pairs to build the graph. Then topological sort visits each course once and processes each edge once.

Space: O(V + E):
    The graph stores all courses and prerequisite edges. The indegree
    dictionary stores one count per course. The queue and output list
    can each hold up to V courses. So the total space is O(V + E).
"""

def find_course_order(prerequisites: list[tuple[str, str]], all_courses: Optional[list[str]] = None) -> list[str]:
    """
        I'll use topological sort. Since each pair is [course,
        prerequisite], the prerequisite must come before the course. So
        I'll create an edge from prerequisite to course
    """
    graph: dict[str, list[str]] = defaultdict(list)
    indegree: dict[str, int] = {}
    
    courses = []
    seen_courses = set()
    
    def add_course(course: str) -> None:
        if course not in seen_courses:
            seen_courses.add(course)
            courses.append(course)
            indegree[course] = 0
    
    """
        If the interviewer gives a separate list of all required
        courses, I'll include those too, because some courses may have
        no prerequisites.
    """
    if all_courses is not None:
        for course in all_courses:
            add_course(course)
            
    seen_edges = set()
    
    for course, prerequisite in prerequisites:
        # A course depending on itself is an immediate cycle
        if course == prerequisite:
            return []
        
        add_course(course)
        add_course(prerequisite)
        
        edge = (prerequisite, course)
        
        """
            I'll avoid counting duplicate prerequisite pairs twice,
            because duplicate edges should not increase indegree
            multiple times
        """
        if edge in seen_edges:
            continue
        
        seen_edges.add(edge)
        graph[prerequisite].append(course)
        indegree[course] += 1
        
    """
        Courses with indegree 0 have no remaining prerequisites, so they
        can be taken first
    """
    queue = deque()
    
    for course in courses:
        if indegree[course] == 0:
            queue.append(course)
            
    order = []
    
    """
        Each time I take a course, I reduce the indegree of courses that
        depend on it. If any of them reaches 0, it becomes available
    """
    while queue:
        current_course = queue.popleft()
        order.append(current_course)
        
        for next_course in graph[current_course]:
            indegree[next_course] -= 1
            
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    """
        If I could not take all courses, then some courses are stuck in
        a cycle, so there is no valid order
    """
    if len(order) != len(courses):
        return []
    
    return order

prerequisites = [
    ("Python Course", "Systems Course"),
    ("Low Level Course", "Python Course"),
]

print(find_course_order(prerequisites))
# ['Systems Course', 'Python Course', 'Low Level Course']
