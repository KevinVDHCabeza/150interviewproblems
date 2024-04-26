prices = [7,1,5,3,6,4]

barato = 0
caro = 0
beneficio = 0

for i in range(len(prices)):
    if prices[i] < prices[barato]:
        barato = i
    if prices[i] - prices[barato] > beneficio:
        beneficio = prices[i] - prices[barato]
        caro = i

print(beneficio)
