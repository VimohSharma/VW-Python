#max from list without using max
lst=list(map(int,input("Enter numbers seperated by spaces: ").split()))
max=lst[0]
for num in lst:
    if(num>max):
        max=num
print(f"the greatest element in the list {lst} is: {max}")