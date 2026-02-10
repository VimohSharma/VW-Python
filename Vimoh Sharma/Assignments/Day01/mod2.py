import mod1

def menuhere():
    while True:
        print("\nEnter your choice of numbers!")
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
            mod1.even_nums(start,end)
        elif choice==2:
            mod1.odd_nums(start,end)
        elif choice==3:
            mod1.all_nums(start,end)

if __name__ == "__main__":
    menuhere()
    print("working with mod2")