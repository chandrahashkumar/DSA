# num = int(input("Enter a number: "))
# rem , rev = 0, 1
# for i in range(num):
#     rem = num % 10
#     rev = rev * 10 + rem
#     num /=10
# print(rev)

# for n in range(11, 100):
#     if n >50:
#         break
#     tens = n // 10
#     units = n % 10
#     if tens + units == 5:
#         print(n)


#
# for n in range(11, 999):
#     if n < 100:
#         tens = n // 10
#         units = n % 10
#         digit_sum = tens + units
#     else:
#         hundreds = n // 100
#         tens = (n // 10) % 10
#         units = n % 10
#         digit_sum = hundreds + tens + units
#     if digit_sum == 5:
#         print(n)

num = int(input("Enter a number: "))
k = 1
fact = 0
for i in range(num+1):
    if i % k == 0:
        fact +=1

if fact == 2:
    print("prime")
