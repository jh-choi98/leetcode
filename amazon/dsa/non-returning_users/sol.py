from collections import defaultdict
import heapq

# sort
def oldest_single_visit_users_sort(logs, k=20000):
    visits = defaultdict(lambda: [0, float('inf')])
    for user_id, ts in logs:
        visits[user_id][0] += 1
        visits[user_id][1] = min(visits[user_id][1], ts)
    
    single = [(ts, user_id) for user_id, (count, ts) in visits.items() if count == 1]
    
    single.sort()
    return [user_id for _, user_id in single[:k]]

# heap
"""
    Time: O(N + U log k)
    Space: O(U + k)
"""
def oldest_single_visit_users_heap(logs, k=20000):
    visits = defaultdict(lambda: [0, float('inf')])
    
    for user_id, ts in logs:
        visits[user_id][0] += 1
        visits[user_id][1] = min(visits[user_id][1], ts)
       
    heap = [] # max heap by timestamp using negative timestamp
    
    for user_id, (count, ts) in visits.items():
        if count != 1:
            continue
        
        entry = (-ts, user_id)
        
        if len(heap) < k:
            heapq.heappush(heap, entry)
        elif ts < -heap[0][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, entry)
            
    result = [(-neg_ts, user_id) for neg_ts, user_id in heap]
    result.sort()
    
    return [user_id for _, user_id in result]
