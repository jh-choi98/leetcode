from typing import List

# Time: O(nlogn)
# Space: O(1)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda pair: pair[0])
        count = 0
        prev_end = intervals[0]
        for i in range(1, len(intervals)):
            if prev_end[1] > intervals[i][0]:
                prev_end = intervals[i] if prev_end[1] > intervals[i][1] else prev_end
                count += 1
            else:
                prev_end = intervals[i]
        return count

# Recursion
# Time: O(2^n)
# Space: O(n)
"""
A helpful way to think about this is:
- Instead of directly counting removals, we can try to keep as many
  non-overlapping intervals as possible
- If we know the maximum number of intervals we can keep without
  overlap,then
    - minimum removals = total intervals - maximum kept

To make decisions, we sort the intervals by start time and use recursion
to explore two choices at each interval:
    1. Skip the current interval
    2. Take the current interval (only if it does not overlap with the previously taken interval)

The recursive function represents:
    What is the maximum number of non-overlapping intervals we can keep starting from index i, given that the last chosen interval is prev?
"""
class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[0])
        n = len(intervals)
        
        def dfs(i, prev):
            if i == n:
                return 0
            res = dfs(i + 1, prev)
            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1 + dfs(i + 1, i))
            return res
        
        return len(intervals) - dfs(0, -1)

# DP (Top-Down)
# "가중치 구간 스케줄링(Weighted Interval Scheduling)" 문제를 풀기 위해
# DP 로직이 필수 -> 하지만 가중치가 없는 이 문제 같은 경우는 쓰면 안 됨
# (follow-up 대비용)
# Time: O(n^2)
# Space: O(n)
"""
We want to remove the minimum number of intervals so that the remaining intervals do not overlap.

A common trick is to flip the problem:
    - instead of counting removals directly, find the maximum number of non-overlapping intervals we can keep
    - then:
        minimum removals = total intervals - maximum kept
        
This solution sorts intervals by end time. After that, for any interval
i, the next interval we choose must start at or after intervals[i][1]

We define a DP state that answers:
    If we choose interval i as part of our set, what is the maximum
    number of non-overlapping intervals we can take starting from i?

The result for an index depends on future indices, and many states
repeat, so we use memoization
"""
class Solution3:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])
        n = len(intervals)
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            
            res = 1
            for j in range(i + 1, n):
                if intervals[i][1] <= intervals[j][0]:
                    res = max(res, 1 + dfs(j))
            
            memo[i] = res
            return res
        
        return n - dfs(0)

# DP (Bottom-Up)
# Time: O(n^2)
# Space: O(n)
class Solution4:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])
        n = len(intervals)
        dp = [0] * n
        
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        max_non_overlapping = max(dp)
        return n - max_non_overlapping
    
# DP with Binary Search
# Time: O(nlogn)
# Space: O(n)
"""
"가중치(Weight)가 있는 구간 스케줄링(Weighted Interval Scheduling)"
문제의 정석적인 풀이법인 DP(동적 계획법) + 이진 탐색(Binary Search) 방식

1. 전체 로직 흐름
이 알고리즘의 목표는 "겹치지 않게 선택할 수 있는 구간의 최대 개수"를
구한 뒤, 전체 개수(n)에서 빼서 "제거해야 할 최소 개수"를 구하는
것입니다.
1) 정렬 (Sorting): 구간들을 끝나는 시간(End Time) 기준으로 오름차순
정렬합니다. (DP를 위해 필수)
2) DP 테이블 초기화: dp[i]는 "i번째 구간까지 고려했을 때, 겹치지 않게
선택할 수 있는 최대 구간 수"를 저장합니다.
3) 이진 탐색 (Binary Search): 현재 구간(i)을 선택했을 때, 이와 겹치지
않는 가장 가까운 이전 구간을 빠르게(O(log N)) 찾습니다.
4) 점화식 적용:현재 구간을 포함한다 vs 포함하지 않는다 중 큰 값을 선택.
5) 결과 반환: 전체(n) - 최대 유지 개수(dp[n-1]).
"""
class Solution5:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])
        # 끝나는 시간을 기준으로 정렬합니다. 이는 DP를 진행할 때 "내
        # 앞에 있는 애들은 나보다 빨리 끝났다"는 것을 보장하기
        # 위함입니다
        n = len(intervals)
        dp = [0] * n
        dp[0] = 1
        
        # 현재 구간의 **시작 시간(target)**보다 일찍(혹은 동시에) 끝나는
        # 구간들 중 가장 뒤에 있는 구간의 위치를 찾습니다
        def bs(r, target):
            l = 0
            while l < r:
                m = (l + r) // 2
                if intervals[m][1] <= target:
                    l = m + 1
                else:
                    r = m
            return l 
            # 최종적으로 반환되는 l은 "겹치지 않는 구간의 개수" 혹은
            # "겹치지 않는 구간들의 바로 다음 인덱스"를 의미
            # 따라서, 실제 겹치지 않는 직전 구간의 인덱스는 l - 1
            # (코드에서는 idx - 1)
                
        for i in range(1, n):
            idx = bs(i, intervals[i][0])
            if idx == 0:
                # 나와 겹치지 않는 이전 구간이 아예 없음
                # dp[i-1]: 나를 포기하고 이전까지의 최대값 유지
                # (원래는 max(dp[i-1], 1)이어야 하지만, dp[i-1] >= 1
                # 이므로 그냥 dp[i-1]로 퉁침)
                dp[i] = dp[i - 1]
            else:
                # 점화식: Max(나를 안 뽑음,  나를 뽑음 + 내 짝꿍까지의
                # 최대값)
                dp[i] = max(dp[i - 1], 1 + dp[idx - 1])
        return n - dp[n - 1]

# Greedy (sort By Start)
# Time: O(nlogn)
# Space: O(1)
class Solution6:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[0])
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res

# Greedy (sort By End)
# Time: O(nlogn)
# Space: O(1)
class Solution7:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])
        prevEnd = intervals[0][1]
        res = 0
        
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]
                
        return res
