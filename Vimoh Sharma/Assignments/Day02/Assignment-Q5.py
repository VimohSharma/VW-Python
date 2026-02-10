#fxn to get the max of three numbers.

def max3(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
    
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))

print(f"the max between {num1}, {num2} & {num3} is {max3(num1,num2,num3)}")