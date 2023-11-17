def merge_sort(arr, lb, ub):
    if(lb < ub):
        mid = (lb+ub+1)//2
        merge_sort(arr, lb, mid)
        merge_sort(arr, mid+1, ub)
        merge(arr, lb, mid, ub)


def merge(arr, lb, mid, ub):
    i = lb
    j = mid+1
    k = lb
    sorted_arr = []

    while i <= mid and j <= ub:
        if arr[i] < arr[j]:
            sorted_arr[k] = arr[i]
            i += 1
        else:
            sorted_arr[k] = arr[j]
            j += 1
        k += 1

    if i > mid:
        while j <= ub:
            sorted_arr[k] = arr[j]
            j += 1
            k += 1
    else:
        while i <= mid:
            sorted_arr[k] = arr[i]
            i += 1
            k += 1

    while k <= ub:
        arr[k] = sorted_arr[k]


arr = [1, 3, 5, 2, 6, 9, 6, 7, 13, 34, 23, 21, 18, 45]
merge_sort(arr, 0, len(arr)-1)
