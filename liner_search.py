def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [12,56,1,2,9,7,15]
target = 1
result = linear_search(arr, target)
if result !=-1:
    print(f"Element is found index: {result}")
else:
    print("Element is not found")

