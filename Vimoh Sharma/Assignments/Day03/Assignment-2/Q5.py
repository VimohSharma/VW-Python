#see common ele between 2 lists
def overlapping(lst1,lst2):
        return bool(set(lst1) & set(lst2))

print(overlapping([1,2,3,4,5],[9,8,7,6,5]))
print(overlapping([1,2,3,4,5],[9,8,7,6,10]))