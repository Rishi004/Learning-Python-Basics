def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [1, 3, 2, 4, 6, 5]
bubble(arr)
print(arr)
