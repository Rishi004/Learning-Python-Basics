def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    return end


def quick_sort(arr, start, end):
    if start < end:
        pivot_loc = partition(arr, start, end)
        quick_sort(arr, start, pivot_loc-1)
        quick_sort(arr, pivot_loc+1, end)


arr = [200, 4, 5, 8, 19, 10, 7, 3, 24, 45, 35, 3, 23]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
