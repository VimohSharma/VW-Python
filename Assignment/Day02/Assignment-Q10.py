#Grade avg calculation

phy=float(input("Enter your marks for physics out of 100: "))
chem=float(input("Enter your marks for chemistry out of 100: "))
mat=float(input("Enter your marks for maths out of 100: "))

avgGrade=(phy+chem+mat)/3

if 90 <= avgGrade <= 100:
    grade='A'
elif 80 <= avgGrade < 90:
    grade='B'
elif 70 <= avgGrade < 80:
    grade='C'
elif 60 <= avgGrade < 70:
    grade='D'
elif 0 <= avgGrade < 60:
    grade='F'

print(f"you have obtained a {grade} Grade with an average of {avgGrade:.2f}")