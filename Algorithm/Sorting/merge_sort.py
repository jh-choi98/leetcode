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
