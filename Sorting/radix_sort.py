def get_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


def count_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10  # //는 정수 나눗셈, /는 실수 나눗셈
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_val = get_max(arr)
    exp = 1
    while max_val // exp > 0:
        count_sort(arr, exp)
        exp *= 10


arr = [4, 3, 5, 6, 7, 434, 6, 0, 8, 43]
radix_sort(arr)
print(arr)
