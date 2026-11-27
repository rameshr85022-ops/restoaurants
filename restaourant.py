print("----- RESTAURANT MENU -----")
print("1. Idli       - Rs. 30")
print("2. Dosa       - Rs. 50")
print("3. Meals      - Rs. 100")
print("4. Fried Rice - Rs. 80")

name = input("Enter customer name: ")
choice = int(input("Enter food choice (1-4): "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    item = "Idli"
    price = 30
elif choice == 2:
    item = "Dosa"
    price = 50
elif choice == 3:
    item = "Meals"
    price = 100
elif choice == 4:
    item = "Fried Rice"
    price = 80
else:
    item = "Invalid"
    price = 0

total = price * quantity
discount = total * 0.05
final_bill = total - discount

print("\n----- CUSTOMER BILL -----")
print("Customer Name:", name)
print("Food Item:", item)
print("Quantity:", quantity)
print("Total Bill: Rs.", total)
print("Discount (5%): Rs.", discount)
print("Final Bill: Rs.", final_bill)