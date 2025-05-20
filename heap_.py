import heapq

heap = []
# insert the element into the heap
elements = [3,1,4,1,5,9,2,6,5,3,5]

for element in elements:
    heapq.heappush(heap, element)
print(f"The heap after insertion is: {heap}")

smallest = heapq.heappop(heap)
print(f"the smallest element is: {smallest}")
print(f"The heap after removing the smallest element is: {heap}")

new_element = 100
heapq.heappushpop(heap, new_element)
print(f"The heap after the push - pop : {heap}")

n = 3
input_list = [10,12,2,5,100,45,0,3]
s_smallest = heapq.nsmallest(n, input_list)
print(f"The smallest {n} elements are: {s_smallest}")

n_largest = heapq.nlargest(n, input_list)
print(f"the largest {n} elements are: {n_largest}")

heapq.heapify(input_list)
print(f"The heapified list is: {input_list}")


