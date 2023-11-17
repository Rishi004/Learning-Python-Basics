def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i+1, len(arr)):
            if (arr[min_index] > arr[j]):
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print(arr)
