# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)

if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked")

if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock.")