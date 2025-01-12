# Определение минимального размера подмассива для сортировки слиянием
MIN_MERGE = 32

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr, left, mid, right):
    len1 = mid - left + 1
    len2 = right - mid
    left_arr = []
    right_arr = []
    for x in range(len1):
        left_arr.append(arr[left + x])
    for x in range(len2):
        right_arr.append(arr[mid + 1 + x])

    i = 0
    j = 0
    k = left
    while i < len1 and j < len2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_arr[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right_arr[j]
        k += 1
        j += 1

def tim_sort(arr):
    n = len(arr)
    for i in range(0, n, MIN_MERGE):
        insertion_sort(arr, i, min((i + MIN_MERGE - 1), n - 1))

    size = MIN_MERGE
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))

            merge(arr, left, mid, right)
        size *= 2

# Пример использования:
array = [5, 3, 8, 4, 2, 1, 6, 7]
tim_sort(array)
print(array)
