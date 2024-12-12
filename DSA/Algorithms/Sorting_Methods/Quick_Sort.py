# Divide and conquer approach
def partition(arr, low, high):
    pivot = arr[low]  # first element is considered pivot
    i = low + 1  # start from 2nd index
    j = high  # start from last index
    while True:
        while i <= j and arr[i] <= pivot:  # keep incrementing till we find value greater than pivot
            i += 1
        while j >= i and arr[j] >= pivot:  # keep incrementing till we find value lower than pivot
            j -= 1
        if i < j:  # swap i and j
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]  # swap j and pivot
    return j


def quick_sort(arr, i, j):  # function that calls partition
    if i < j:
        id = partition(arr, i, j)  # get value of j
        quick_sort(arr, i, id - 1)  # for left side
        quick_sort(arr, id + 1, j)  # for right side


arr1 = [10, 5, 4, 13, 42, 12, 7, 9, 11, 32]  # array creation
quick_sort(arr1, 0, len(arr1) - 1)  # function call
for i in range(len(arr1)):  # print array elements
    print(arr1[i], end=' ')
print()
