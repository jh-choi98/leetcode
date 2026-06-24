from collections import defaultdict
import heapq

"""
    - Time: O(nlogn)
    - Space: O(n)
"""
def min_vms_required(jobs: list[tuple[int, int]]) -> int:
    if not jobs:
        return 0
    
    sorted_jobs = sorted(jobs)
    active_end_times = []
    max_vms = 0
    
    for start, end in sorted_jobs:
        if start > end:
            return -1
        
        if start == end:
            continue
        
        while active_end_times and active_end_times[0] < start:
            heapq.heappop(active_end_times)
        
        heapq.heappush(active_end_times, end)
        
        max_vms = max(max_vms, len(active_end_times))
        
    return max_vms


def run_tests():
    cases = [
        ([], 0),
        ([(2, 5)], 1),
        ([(6, 8), (2, 5), (3, 7)], 2),
        ([(2, 5), (5, 7)], 1),        # 끝=시작 -> VM 재사용
        ([(1, 10), (2, 9), (3, 8)], 3),  # 전부 겹침
        ([(1, 4), (1, 4), (1, 4)], 3),   # 같은 시작
        ([(1, 2), (3, 4), (5, 6)], 1),   # 안 겹침
        ([(1, 3), (2, 5), (4, 6)], 2),   # 중간에서 peak
    ]
    for jobs, expected in cases:
        result = min_vms_required(jobs)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] {jobs} -> got {result}, expected {expected}")


run_tests()


"""
    - Time: O(nlogn)
    - Space: O(n)
"""
def min_vms_required2(jobs: list[tuple[int, int]]) -> int:
    if not jobs:
        return 0
    
    events = defaultdict(int)
    
    for start, end in jobs:
        if start > end:
            return -1
        
        if start == end:
            continue
        
        events[start] += 1
        events[end] -= 1
    
    active_vms = 0
    max_vms = 0
    
    for time in sorted(events):
        active_vms += events[time]
        max_vms = max(max_vms, active_vms)
        
    return max_vms
