# def isPrime(x):
#     if x < 2:
#         return False
#     elif x == 2:
#         return True  
#     for n in range(2, x):
#         if x % n ==0:
#             return False
#     return True

# def primeGenerator(a, b):
#     #your code goes here
#     for i in range(a,b):
#         if isPrime(i):
#             yield i
    
# f = int(input("Enter start range: "))
# t = int(input("Enter end range: "))


# print(list(primeGenerator(f, t)))

# print(bool({})) 
# print(bool([]))
# print(bool(''))

for i in range(5,0,-1):
    for j in range(i):
        print("* ",end=" ")
    print("")
for i in range(6):
    for j in range(i):
        print("* ",end = " ")
    print(" ")