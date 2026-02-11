#loop for fact till 10
fact=1
print(f"0! = {fact}")
print(f"1! = {fact}")
for num in range(2,11):
    fact*=num
    print(f"{num}! = {fact}")
