def Bubble_sort(list):
    for i in range(len(list)-1,0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


l = [5,1,15,20,78,2,70,1]


list = []
size = int(input("Enter list size: "))
for i in range(1, size + 1):
    ele = int(input(f"Enter {i} element: "))
    list.append(ele)

Bubble_sort(list)
print(list)