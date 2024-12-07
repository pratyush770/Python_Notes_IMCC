# Works only on sorted set of elements.
def binarySearch(arr, ele):
    low = 0  # start
    high = len(arr) - 1  # end
    while low <= high:
        mid = (low + high) // 2  # calculate mid value
        if ele > arr[mid]:  # if element is present on right side
            low = mid + 1
        elif ele < arr[mid]:  # if element is present on left side
            high = mid - 1
        else:
            return mid  # if element matches mid value
    return -1  # if match not found


arr = [5, 10, 20, 30, 40, 50]
ele = int(input("Enter the element you want to search: "))  # takes user input
res = binarySearch(arr, ele)  # function call
if res != -1:  # if element exists
    print(f"Element is present at {res}")
else:  # if element does not exist
    print("Element is not present in the array")
