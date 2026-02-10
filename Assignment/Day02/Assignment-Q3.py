# 4digit facing code
num=input("Enter a 4-digit number: ").strip()
if not (num.isdigit() and len(num) ==4):
    print("please enter a 4-digit positive number for eg - 6732")
else:
    numb=int(num)
    thou=numb//1000
    hun=(numb//100)%10
    ten=(numb//10)%10
    ones=numb%10

    print(f"face values: {thou} {hun} {ten} {ones}")

    print (f"place_exp = {numb} = {thou}000 + {hun}00 + {ten}0 + {ones}")

    reverse_num=ones*1000+ten*100+hun*10+thou
    print(f"Reverse of {numb} is {reverse_num}")