#display elements of list thrice if number

mylist=['41','DROND','BVs','13','ZARA']

for ele in mylist:
    if ele.isdigit():
        print(f"{ele} {ele} {ele}")
    else:
        print(ele + "#")
