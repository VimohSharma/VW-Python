#count until tuple appears

lst=[10,20,30,(40,50),60]

cnt=0
for num in lst:
    if type(num)== tuple:
        break
    cnt+=1
print(f"the number of elements before tuple appears is: {cnt} in {lst}")