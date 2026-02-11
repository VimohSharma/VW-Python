#remove repetitive items
num=[2,3,4,5,2,6,3,2]
res=[]
for n in num:
    if n not in res:
        res.append(n)

print(res)