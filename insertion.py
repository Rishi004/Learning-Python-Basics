# declare list
lst = []

# get number of elements
n = int(input('Enter number of elements: '))

print('Enter Numbers')
for i in range(0, n):
    num = int(input())
    lst.append(num)

print(lst)


def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


insertionSort(lst)
print(lst)
