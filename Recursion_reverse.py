
# reverse , base = 0 ,1
# def reverse_num(num):
#     global reverse
#     global base
#     # revers = 0
#     # base = 1
#     if num > 0:
#         reverse_num(num//10)
#         reverse = reverse + (num % 10) * base
#         base = base * 10
#     return reverse

# num = int(input("Enter number: "))
# print(reverse_num(num))


def rev(num, reverse_num = 0):
    if num == 0:
        return reverse_num
    else:
        digit = num % 10
        reverse_num = reverse_num *10 + digit

        num  = num //10

        return rev(num , reverse_num)
    
num = int(input("Enter number: "))
print(rev(num))