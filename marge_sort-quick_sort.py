# Implement merge sort and find kth largest element in an array.

arr = [3, 2, 1, 5, 6, 4]
k = 2


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    left_index = right_index = 0
    sorted_array = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])
    return sorted_array


# print(merge_sort(arr))


# quick sort


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    pivot = arr[mid]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left)+middle+quick_sort(right)
    

# print(quick_sort(arr)[-k])

