
def fibonacci(num):
    if num < 0:
        return "Invalid Input"
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num -1) + fibonacci(num -2)
    

term = int(input("Enter find fibonacci term: "))
print("Fibonacci Series:")
for i in range(term):
    print(fibonacci(i))

    
