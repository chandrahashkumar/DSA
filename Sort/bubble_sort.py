def bubble_sort(arr):
    n = len(arr)
    for _ in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped is False:
            break

arr = [10,3,45,7,89]
bubble_sort(arr)
print("Sorted elements")
for i in arr:
    print(i,end=" ")