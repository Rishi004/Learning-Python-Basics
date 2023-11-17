def heapInsert(arr, n, val):
    arr[n] = val
    i = n

    while (i > 1):
        parent = i // 2
        if (arr[parent < arr[i]]):
            arr[parent], arr[i] = arr[i], arr[parent]
            i = parent
        else:
            return -1


arr = [40, 30, 20, 10, 5, 4, 3]
heapInsert(arr, len(arr), 35)
print(arr)
