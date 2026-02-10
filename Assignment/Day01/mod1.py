def menu():
    while True:
        print("Enter your choice of numbers!")
        print("press 1. to print Even numbers")
        print("press 2. to print Odd Numbers")
        print("press 3. to print All the numbers")
        print("Press anything else to exit.")

        choice = int(input("Enter your choice: "))
        
        if choice not in(1,2,3):
            print("Exiting Function..")
            break
        
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))

        if choice==1:
            even_nums(start,end)
        elif choice==2:
            odd_nums(start,end)
        elif choice==3:
            all_nums(start,end)

def even_nums(start,end):
    print("Even numbers: ")
    for i in range(start,end+1):
        if i%2==0:
            print(i, end=" ")

def odd_nums(start,end):
    print("Odd numbers: ")
    for i in range(start,end+1):
        if i%2!=0:
            print(i, end=" ")
            
def all_nums(start,end):
    print("All numbers: ")
    for i in range(start,end+1):
        print(i, end=" ")
            

if __name__ == "__main__":
    menu()
    print("working in mod1")
    