"""
Given an array of n integers, A[1], ... , A[n], 
find the maximum sum of consecutive entries of A
(return 0 if all entries of A are negative)
"""


# Brute Force
# T: O(n^2)
class Solution:
    def find_max_sum(self, arr):
        length = len(arr)
        max_sum = 0
        for i in range(length):
            sum = arr[i]
            for j in range(i + 1, length):
                sum += arr[j]
                max_sum = max(max_sum, sum)
        print(max_sum)
        return max_sum


# Divide and Conquer
# T: O(nlogn)
class Solution2:
    def find_max_sum(self, arr):
        n = len(arr)
        if n == 1:
            return max(0, arr[0])

        mid = n // 2
        left_max = self.find_max_sum(arr[:mid])
        right_max = self.find_max_sum(arr[mid:])

        # 중간에서 왼쪽으로 이동하면서 최대 부분합 계산
        left_sum = 0
        temp_sum = 0
        for i in range(mid - 1, -1, -1):  # range(start, stop, step)
            temp_sum += arr[i]
            if temp_sum > left_sum:
                left_sum = temp_sum
        # 중간에서 오른쪽으로 이동하면서 최대 부분합 계산
        right_sum = 0
        temp_sum = 0
        for i in range(mid, n):
            temp_sum += arr[i]
            if temp_sum > right_sum:
                right_sum = temp_sum

        # 가운데를 가로지르는 최대 부분합
        max_crossing_sum = left_sum + right_sum
        return max(left_max, right_max, max_crossing_sum)


sol = Solution()
sol2 = Solution2()
arr1 = [1, 7, 4, 0, 2, 1, 3, 1]
arr2 = [-1, -7, -4, -1, -2]
arr3 = [1, -7, 4, 0, 2, -5, 3, -1]

sol.find_max_sum(arr1)
sol.find_max_sum(arr2)
sol.find_max_sum(arr3)
print("------------------------------")
print(sol2.find_max_sum(arr1))
print(sol2.find_max_sum(arr2))
print(sol2.find_max_sum(arr3))

"""
최대 부분합의 3가지 경우
1. 왼쪽 부분 배열에 최대 부분합이 존재하는 경우
2. 오른쪽 부분 배열에 최대 부분합이 존재하는 경우
3. 가운데를 가로지르는 부분 배열에 최대 부분합이 존재하는 경우

3번째 경우에서 중간에서 양쪽 끝으로 이동하는 이유
: 끝에서 중간으로 이동하면 부분 배열이 중간 지점을 포함하는지 확실하지 않음.


알고리즘
1. 배열을 중간 지점으로 분할합니다.
2. 왼쪽 부분 배열에서 최대 부분합을 재귀적으로 찾습니다.
3. 오른쪽 부분 배열에서 최대 부분합을 재귀적으로 찾습니다.
4. 가운데를 가로지르는 최대 부분합을 찾습니다.
    - 중간 지점에서 왼쪽으로 이동하면서 최대 부분합을 계산합니다.
    - 중간 지점에서 오른쪽으로 이동하면서 최대 부분합을 계산합니다.
    - 두 값을 더하여 가운데를 가로지르는 최대 부분합을 구합니다.
5. 세 가지 경우 중 최대값을 반환합니다.
"""
