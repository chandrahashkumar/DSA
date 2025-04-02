l = []
n = int(input("Enter number of elements: "))
for i in range(n):
    l.append(int(input(f"Enter element {i+1}: ")))

min = l[0]
max = l[0]

for i in range(n):
    if l[i] > max:
        max = l[i]
    if l[i] < min:
        min = l[i]
print(f"The minium and maximum is {min} and {max}.")

