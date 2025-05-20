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

s = 3
input_list = [10,12,2,5,100,45,0,3]
s_smallest = heapq.nsmallest(s, input_list)
print(f"The smallest {s} elements are: {s_smallest}")

