# T: O(nlogn)
# S: O(n)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    i, j = 0, 0
    sorted_arr = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # append remaining elements from both lists
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


def main():
    arr = [7, 6, 5, 4, 3, 2, 1]
    print(merge_sort(arr))


main()

"""
퀵 정렬(Quick Sort)
상위에서 하위로 내려가면서 정렬하는 방식입니다.
각 단계에서 피벗(pivot)을 선택하고, 피벗을 기준으로 배열을 두 부분으로 분할한 뒤, 
각 부분에서 재귀적으로 정렬합니다.
즉, 분할할 때 이미 어느 정도 정렬이 진행됩니다. 피벗을 중심으로 한쪽에는 작은 값들, 
다른 한쪽에는 큰 값들이 배치됩니다.

정렬 과정: 피벗을 기준으로 배열을 나누면서 각 부분에서 정렬이 이루어지고, 
그 이후 재귀적으로 하위 문제로 내려가서 각 부분을 정렬하는 방식입니다.

병합 정렬(Merge Sort)
하위 문제로 내려간 다음에 정렬하면서 올라오는 방식입니다.
배열을 더 이상 나눌 수 없을 때까지 계속 반으로 나누고, 그 후에 작은 부분 배열을 다시 병합(merge)하면서 정렬합니다.
즉, 병합할 때 정렬이 이루어집니다. 하위 배열이 정렬된 상태에서 병합하면서 정렬된 결과를 만들어냅니다.

정렬 과정: 배열을 반으로 나누면서 하위 문제로 내려간 후, 병합하는 단계에서 정렬을 시작하며 위로 올라갑니다.
"""
