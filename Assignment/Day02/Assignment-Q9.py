# leap year

lyear=int(input("Enter a year: "))

if (lyear%400==0) or (lyear%4==0 and lyear%100!=0):
    print(f"{lyear} is a leap year.")
else:
    print(f"{lyear} is not a leap year.")