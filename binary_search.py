# Binary search work on only sorted array or list.
def binary_search(arr, target):
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] <target:
            low = mid + 1
        else:
            high = mid -1
    return -1

arr = [12,56,1,2,9,7,15]
arr.sort()
print(arr)
target = 15
result = binary_search(arr, target)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print(f"Element is not present in array")