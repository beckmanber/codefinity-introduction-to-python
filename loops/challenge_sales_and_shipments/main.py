# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]


for sold in range(len(products)):
    products[sold][1] -= units_sold[sold][1]
    
for stocked in range(len(products)):
    products[stocked][1] += shipment_received[stocked][1]

print("Final stock levels for all products:", products)