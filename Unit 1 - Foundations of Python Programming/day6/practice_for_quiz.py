# Practicing for ICD20 quiz

# HW1

drink = float(input("Enter the cost of your drink:"))
entree = float(input("Enter the cost of your entree:"))
dessert = float(input("Enter the cost of your dessert: "))
appetizer = float(input("Enter the cost of your appetizer: "))
tiprate = int(input("Enter the tip rate as a percentage: "))

subtotal = round(drink + entree + dessert + appetizer,2)
tipcalc = subtotal*(tiprate*0.01)
total = tipcalc + subtotal

print(f"Subtotal: ${subtotal}")
print(f"Tip: ${tipcalc}")
print(f"Total Cost: ${total}")

# HW2

length_wall = float(input("Enter the length of your wall in meters:"))
width_wall = float(input("Enter the width of your wall:"))
height_house = float(input("What is the height of your house in meters?"))
Cost_brick = float(input("Enter the cost per brick:"))
wbrick = float(input("Enter the width of a brick:"))
lbrick = float(input("Enter the length of a brick:"))
hbrick = float(input("Enter the height of a brick:"))

sa_walls = (length_wall*width_wall)*4
sa_bricks = (wbrick*wbrick)
tot_bricks = round(sa_walls/sa_bricks,1)
cost_bricks = round(tot_bricks*Cost_brick)

print(f"The surface area of the walls is equal to {sa_walls}m2")
print(f"We require {tot_bricks} bricks for this project!")
print(f"The total cost of the bricks is equal to ${cost_bricks}")

# HW 3
distance = int(input("What is the distance of trip in km?"))
fuel_efficiency = float(input("What is the fuel efficiency of your car in /100km?"))
price_fuel = float(input("What is the price of fuel in dollars?"))
pax = int(input("Enter the number of passengers in your vehicle:"))

total_fuel = round(distance/fuel_efficiency,2)
total_fuel_cost = round(total_fuel*price_fuel,2)
cost_fuel_pax = round(total_fuel_cost/pax,2)

print(f"Total Fuel: {total_fuel}Litres")
print(f"Total Fuel Cost: ${total_fuel_cost}")
print(f"Fuel Cost evenly Split per {pax} people: {cost_fuel_pax}")