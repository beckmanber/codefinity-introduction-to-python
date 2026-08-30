vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")

if "carrots" in vegetables:
    print("Carrots are already in the list.")
else:
    vegetables.append("carrots")
    
if "cucumbers" in vegetables:
    print("Cucumbers are already in the list.")
else:
    vegetables.append("cucumbers")

vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)