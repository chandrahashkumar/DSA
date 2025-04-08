l = []
n = int(input("Enter number of elements: "))
for i in range(n):
    l.append(int(input(f"Enter element {i+1}: ")))

min_e = l[0]
max_e = l[0]

for i in range(n):
    if l[i] > max_e:
        max_e = l[i]
    if l[i] < min_e:
        min_e = l[i]
s_max = min_e
s_min = max_e
# [5,6,9,1,0,99,788]
for i in range(n):
    if l[i]>s_max and l[i]!=max_e:
        smax = l[i]
    if l[i]<s_min and l[i] !=min_e:
        s_min = l[i]


print(f"Second max = {s_max} and Second min = {s_min}")
