# subtract two lists
def subtract(list1,list2):
    res=[]
    for ele in list1:
        if ele not in list2:
            res.append(ele)
    return res

list1=[10,20,30,40]
list2=[30,40,50,60]
print(f"{list1} - {list2} is: {subtract(list1,list2)}")