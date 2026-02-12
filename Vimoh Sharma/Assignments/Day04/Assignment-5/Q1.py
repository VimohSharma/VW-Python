#FizzBuzz For
st=int(input("Enter your starting number: "))
end=int(input("Enter your ending number: "))

for num in range(st,end+1):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)
