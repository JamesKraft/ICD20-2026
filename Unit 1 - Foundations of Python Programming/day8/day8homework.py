# Homework Pratice 1 - Rounding
import math

print(f"\n{math.pi:.3f}")

price1 = 29.99
print(f"{price1:.2f}")

# Homework Practice 2 - Percentage
tax_rate = 0.075
print(f"\n{tax_rate:.2%}")
discount = 0.25
print(f"{discount:.1%}")

# Homework Practice 3 - Width
city = "New York"
print(f"\n{city:<10}")
Temperature = 72.5
print(f"{Temperature:^10}")

# Homework Practice 4 - Table
price = 25.99
quantity = 3
item = "Product"
total = price*quantity
print(f"{"\nItem":<10}{"Price":>10}{"Quantity":>15}{"Total":>12}")
print(f"{item:<10}{price:>10}{quantity:>15}{total:>12}")


# Homework Practice 5 - Table
cityny = "New York"
cityla = "Los Angeles"
citywindy = "Chicago"

popny = "8,398,748"
popla = "3,990,456"
popwindy = "2,693,976"

areany = 468.19
areala = 503.79
areawindy = 227.63

print(f"{"\nCity":<13}{"Population":<15}{"Area (sq km):":<10}")
print(f"{cityny:<12}{popny:<15}{areany:<10}")
print(f"{cityla:<12}{popla:<15}{areala:<10}")
print(f"{citywindy:<12}{popwindy:<15}{areawindy:<10}")