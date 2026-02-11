#dict of students

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
print(f"there are {len(people)} students in the dictionary")
people['Lisa']='Green'
print(f"Dictionary after changing the color of Lisa: {people}")
people.pop('Jenny')
print(f"Dictionary after Removal of Jenny: {people}")

print("Sorted Dictionary:- ")
for key in sorted(people):
    print(key,":", people[key])