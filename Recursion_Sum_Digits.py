def sum(num):
    if num < 0:
         return "Invalid Input"
    elif num < 10:
        return num
    else:
        return num % 10 + sum(num // 10)
    
num = int(input("Enter a number: "))
print(f"The sum of the digits of {num} is {sum(num)}")