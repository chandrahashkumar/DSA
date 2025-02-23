def sum(num):
    if num < 0:
         return "Invalid Input"
    elif num == 0:
        return 0
    else:
        return(num%10) + sum(num//10)
    
num = int(input("Enter a number: "))
print(sum(num))