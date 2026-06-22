import heapq


def running_medians(delivery_times: list[int]) -> list[int | float]:
    lower = []
    upper = []
    medians = []
    
    for delivery_time in delivery_times:
        if not lower or delivery_time <= -lower[0]:
            heapq.heappush(lower, -delivery_time)
        else:
            heapq.heappush(upper, delivery_time)
            
        if len(lower) > len(upper) + 1:
            heapq.heappush(upper, -heapq.heappop(lower))
        elif len(upper) > len(lower):
            heapq.heappush(lower, -heapq.heappop(upper))
        
        if len(lower) > len(upper):
            median = -lower[0]
        else:
            median = (-lower[0] + upper[0]) / 2
            
            if median == int(median):
                median = int(median)
        medians.append(median)
    return medians
