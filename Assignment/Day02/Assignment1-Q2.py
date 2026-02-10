#temp changer C and F

def celsius_to_fahrenheit(cel):
    return (cel*1.8)+32
def fahrenheit_to_celsius(fahr):
    return (fahr-32)/1.8

temp_type=input("Enter whether your reading is in C or in F: ")
val=float(input("Enter your reading: "))

if temp_type=='C':
    print(f"{val}C = {celsius_to_fahrenheit(val):.2f}F")
elif temp_type=='F':
    print(f"{val}F = {fahrenheit_to_celsius(val):.2f}C")
else:
    print("Invalid Choice, Enter C for Celsius or F for Fahrenheit.")