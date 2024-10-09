def can_reach_end(arr):
    n = len(arr)
    max_reach = 0
    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + arr[i])
        if max_reach >= n - 1:
            return True
    return max_reach >= n - 1


arr1 = [3, 2, 0, 0, 4]
arr2 = [3, 2, 0, 1, 4]
arr3 = [3, 1, 0, 1, 4]
arr4 = [2, 1, 0, 1, 4]

print(can_reach_end(arr1))  # f
print(can_reach_end(arr2))  # t
print(can_reach_end(arr3))  # t
print(can_reach_end(arr4))  # f


# def test_can_reach_end():
#     # 테스트 케이스 1: 마지막 인덱스에 도달할 수 있는 경우
#     arr1 = [3, 2, 0, 1, 4]
#     print(f"Test case 1: {can_reach_end(arr1)} (Expected: True)")

#     # 테스트 케이스 2: 마지막 인덱스에 도달할 수 없는 경우
#     arr2 = [3, 2, 0, 0, 4]
#     print(f"Test case 2: {can_reach_end(arr2)} (Expected: False)")

#     # 테스트 케이스 3: 배열에 하나의 요소만 있는 경우 (항상 도달 가능)
#     arr3 = [0]
#     print(f"Test case 3: {can_reach_end(arr3)} (Expected: True)")

#     # 테스트 케이스 4: 배열의 모든 요소가 0일 경우 (도달 불가능)
#     arr4 = [0, 0, 0, 0]
#     print(f"Test case 4: {can_reach_end(arr4)} (Expected: False)")

#     # 테스트 케이스 5: 마지막 인덱스 바로 전에 도달 가능
#     arr5 = [2, 3, 1, 1, 4]
#     print(f"Test case 5: {can_reach_end(arr5)} (Expected: True)")

#     # 테스트 케이스 6: 중간에 0이 있어 도달 불가능한 경우
#     arr6 = [1, 0, 2]
#     print(f"Test case 6: {can_reach_end(arr6)} (Expected: False)")
# # 테스트 실행
# test_can_reach_end()
