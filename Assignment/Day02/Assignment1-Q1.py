#Area of and perimeter of the rectangle
def Rec():
    len=int(input("Enter length of the rectangle: "))
    bth=int(input("Enter breadth of the rectangle: "))
    area=len*bth
    per=2*(len+bth)
    print(f"the area and the perimeter of the rectangle are {area} & {per} respectively")

Rec()
