def binarySearch(arr, l, r, data):
    if l > r:
        return False
    else:
        mid = (l+r)//2
        if(data == arr[mid]):
            return mid
        elif(data < arr[mid]):
            return (binarySearch(arr, l, mid-1, data))
        else:
            return (binarySearch(arr, mid+1, r, data))
    return -1


arr = [1, 3, 4, 5, 12, 14, 16, 23, 27, 29, 30, 35, 45, 48, 50]
print(binarySearch(arr, 0, len(arr)-1, 12))
