#telephone bill calculator

calls=int(input("Enter the number of calls: "))

bill=0.0
if calls<=100:
    bill = 200.0
elif calls<=150:
    bill = 200.0 + (calls-100)*0.6
elif calls<=200:
    bill = 200.0 + 50*0.6 + (calls-150)*0.5
else:
    bill = 200.0 + 50*0.6 + 50*0.5 + (calls-200)*0.4

print(f"for {calls} calls your monthly bill comes out to be: {bill:.2f}")