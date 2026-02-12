#Union of two lists
def union(list1,list2):
    res=list1.copy()
    for ele in list2:
        if ele not in res:
            res.append(ele)
    return res


list1=[10,20,30,40]
list2=[30,40,50,60]
print(f"{list1} | {list2} is: {union(list1,list2)}")