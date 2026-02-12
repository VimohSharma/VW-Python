#FizzBuzz while
st=int(input("Enter your starting number: "))
end=int(input("Enter your ending number: "))
num=st
while num<=end:
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)
    num+=1
