prices = [29.99, 45.50, 12.75, 38.20]

for i in range(len(prices)):
    if i == 0:
        discount = 0.10
    elif i == 1:
        discount = 0.20
    elif i == 2:
        discount = 0.15
    else:
        discount = 0.05
    original_price = prices[i]
    new_price = original_price * (1 - discount)
    prices[i] = new_price
    print(f"Updated price for item {i}: ${new_price:.2f}")

