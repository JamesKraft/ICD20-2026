Item = "Item"
Quantity = "Quantity"
Price = "Price ($)"

# Apples
Apples = "Apples"
qtyApples = 12
Applesmoney = 0.75

# Bananas
Ban = "Bananas"
qtyBan = 20
Banmoney = 0.60

# Oranges
Oran = "Oranges"
qtyoran = 8
Oranmoney = 2.50

# Cherries
Cher = "Cherries"
qtyCher = 123
Chermoney = 4.41

print(f"{Item:<0}{Quantity:>14}{Price:>11}")
print(f"{Apples}{qtyApples:>12}{Applesmoney:>11}")
print(f"{Ban:<0}{qtyBan:>11}{Banmoney:>11}")
print(f"{Oran:<0}{qtyoran:>11}{Oranmoney:>11}")
print(f"{Cher:<0}{qtyCher:>10}{Chermoney:>11}")