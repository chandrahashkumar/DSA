max_num = int(input("Enter the maximum number: "))
# odd_list = [i for i in range(1, max_num+1) if i % 2 !=0 ]
odd_list = []
for i in range(1, max_num+1):
    if i %2 !=0:
        odd_list.append(i)
print(odd_list)