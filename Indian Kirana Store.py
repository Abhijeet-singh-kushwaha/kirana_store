from datetime import datetime

# Store item details
items = []

print("welcome to indian kirana store")
print("-" * 40)

while True:
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit(₹): "))

    total_price = quantity * price
    items.append({"name": name, "qty": quantity, "price": price, "total": total_price})

    more = input("add another item? (y/n): ")
    if more.lower() != 'y':
        break

#calculate total amount
total_amount = sum(item["total"] for item in items)

#print reciept
print('\n'+ "=" * 40)
print('\n',"kirana store receipt")
print("_" * 40)
print("{:<15} {:>5} {:>7} {:>8}".format("Item", "Qty", "Rate", "Total"))
print("-" * 40)

for item in items:
    print("{:<15} {:>5} {:>7.2f} {:>8.2f}".format(item["name"], item["qty"], item["price"], item["total"]))

print("-" * 40)
print("{:<28} ₹{:>8.2f}".format("Total Amount:", total_amount))
print("=" * 40)
print("Thank you for shopping with us! ")
