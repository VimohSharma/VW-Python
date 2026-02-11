#find repeated item of a tuple
tuple=(1,2,3,4,5,6,7,8,9,10,5,5,5)
num=int(input("Enter the numba you wanna find: "))

cnt=tuple.count(num)
if cnt>1:
    print(f"{num} appears {cnt} times")
elif cnt==1:
    print(f"{num} present only once")
else:
    print(f"{num} does not exist in the tuple.")
