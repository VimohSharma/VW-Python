# Intersection of two lists-
def intersection(list1,list2):
    res=[]
    for ele in list1:
        if ele in list1 and ele in list2:
            res.append(ele)
    return res

list1=[10,20,30,40]
list2=[30,40,50,60]
print(f"{list1} & {list2} is: {intersection(list1,list2)}")