grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}
bread_details = grocery_inventory["Bread"]
print("Details of Bread:", grocery_inventory.get ("Bread"))
grocery_inventory["Cookies"] = 143, "Bakery"
print("Inventory after adding cookies:", grocery_inventory)
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)