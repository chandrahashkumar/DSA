# l = []
# n = int(input("Enter number of elements: "))
# for i in range(n):
#     l.append(int(input(f"Enter element {i+1}: ")))
#
# min = l[0]
# max = l[0]
#
# for i in range(n):
#     if l[i] > max:
#         max = l[i]
#     if l[i] < min:
#         min = l[i]
# print(f"The minium and maximum is {min} and {max}.")
#
l = [6,6,9,44,8,991]
max_val = max(l)
min_val = min(l)
# print(f"min: {lm}")
# print(f"max: {m}")
#
# help(min)

s_max = 0
s_min = 0
for  i in range(len(l)):
    if