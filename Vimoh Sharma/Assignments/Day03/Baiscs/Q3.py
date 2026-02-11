#marks
marks={}
for mark in range(3):
    subj=input("Enter the Subject: ")
    score=int(input("Enter the mark obtained in that subject: "))
    marks[subj]=score
print(marks)