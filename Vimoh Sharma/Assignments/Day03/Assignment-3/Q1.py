lst1=["Hello","take"]
lst2=["Dear","Sir"]
#print(lst1.__add__(lst2))

lst3=[x + y for x in lst1 for y in lst2]
print(lst3)