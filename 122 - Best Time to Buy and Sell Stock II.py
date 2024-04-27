prices = [7, 1, 5, 3, 6, 4]


beneficio_total = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        beneficio_total += prices[i] - prices[i-1]

