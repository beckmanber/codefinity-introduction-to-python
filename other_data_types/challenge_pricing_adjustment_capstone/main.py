grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
eggs_price = grocery_inventory["Eggs"][1]
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    cat, price, stk = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (cat, price -1, stk)
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    cat, price, stk = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (cat, price, stk + 20)
else:
    print("Milk has sufficient stock")

apples_price = grocery_inventory["Apples"][1]
if apples_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory:", grocery_inventory)