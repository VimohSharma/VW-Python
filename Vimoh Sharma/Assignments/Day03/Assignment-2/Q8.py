#price calculate over quantity
quantity=int(input("Enter the quantity of goods: "))

unit_price=5
total_price=quantity*unit_price

if quantity>50:
    total_price*=0.85
elif quantity>30:
    total_price*=0.9

print(f"the final price for {quantity} goods comes out to be {total_price}")