l = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input(f"Enter the {i+1} element: ")))

max_val = l[0]
min_val = l[0]
for i in range(n):
    if l[i]>max_val:
        max_val = l[i]
    if l[i]<min_val:
        min_val = l[i]

print(f"Max: {max_val} \nMin: {min_val}\n")

se_max = min_val
se_min = max_val

for i in range(n):
    if l[i]>se_max and l[i] != max_val:
        se_max = l[i]
    if l[i]<se_min and l[i] != min_val:
        se_min = l[i]

print(f"Second Max: {se_max} \nSecond Min: {se_min}\n")

