# Running Median / Median of Stream

"""
    I'll keep the smaller half of the numbers in a max heap and the
    larger half in a min heap
    
    The max heap gives me the largest value int the smaller half.
    The min heap gives me the smallest value in the larger half.
    
    If the total count is ood, the median is the top of the larger side.
    If the total count is even, the median is the average of the two
    heap tops
    
    - lower: 작은 절반을 저장하는 max heap
    - uppder: 큰 절반을 저장하는 min heap
"""

import heapq

"""
    Let n be the number of delivery times
    
    - Time: O(nlogn)
        For each delivery time, we intert into one heap, which takes
        O(logn). Rebalanceing may also move one value between heaps,
        which is another O(logn). We do this for all n delivery times,
        so the total time is O(nlogn)
    - Space: O(n)
        The two heaps together store all delivery times seen so far. The
        output list also stores one median per delivery time. So overall
        space is O(n)
"""
def running_medians(delivery_times: list[int]) -> list[int | float]:
    """
        Max heap for the smaller half.
        Python only has a min heap, so we store negative values
    """
    lower = []
    
    # Min heap for the larger half
    upper = []
    
    medians = []
    
    for delivery_time in delivery_times:
        """
            I'll first decide which half this new value belongs to.
            If it is smaller than or equal to the largest value in the
            lower half, it goes to the lower heap. Otherwise, it goes to
            the upper heap
        """
        if not lower or delivery_time <= -lower[0]:
            heapq.heappush(lower, -delivery_time)
        else:
            heapq.heappush(upper, delivery_time)
            
        """
            Now I'll rebalance the heaps so that lower is either the
            same size as upper, or has exactly one more element
        """
        if len(lower) > len(upper) + 1:
            heapq.heappush(upper, -heapq.heappop(lower))
        elif len(upper) > len(lower):
            heapq.heappush(lower, -heapq.heappop(upper))
            
        """
            After balancing, if lower has more elements, the median is
            the top of lower. If both heaps have the same size, the
            median is the average of both heap tops
        """
        if len(lower) > len(upper):
            median = -lower[0]
        else:
            median = (-lower[0] + upper[0]) / 2
            
            # This is only to match outputs like 11 instead of 11.0.
            # If the interviewer doesn't care about formatting, this
            # part can be skipped
            if median == int(median):
                median = int(median)
        medians.append(median)
        
    return medians
