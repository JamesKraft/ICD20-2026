# Homework #1
Appetizer = float(input("What is the cost of your appetizer?"))
Drink = float(input("What is the cost of your drink?"))
Entree = float(input("What is the cost of your entree?"))
Dessert = float(input("What is the cost of your dessert?"))
Tip_Rate = int(input("Enter the tip rate as a percentage:"))
Total = round(Appetizer + Drink + Entree + Dessert,2)
Tipr = Tip_Rate*0.01
Tipx = round(Tipr*Total,2)


print("\nBill Summary:")
print(f"Subtotal: ${Total}")
print(f"Tip: ${Tipx}")
print(f"The total is equal to ${Tipx + Total}")

# Homework #2
Length = float(input("Enter the length of wall 1 in meters:"))
Width = float(input("Enter the width of wall 1 in meters:"))
Height = float(input("Enter the height of the house in meters:"))
Cost = float(input("Enter the cost per brick in dollars:"))
WBrick = float(input("Enter the width of a brick"))
LBrick = float(input("Enter the length of a brick:"))
HBrick = float(input("Enter the height of a brick in meters:"))

Surface_Area_of_Walls = (Length*Height)*4
Surface_Area_of_Bricks = (LBrick*HBrick)
Num_of_Bricks = round(Surface_Area_of_Walls/Surface_Area_of_Bricks,0)
Total_Cost_of_Bricks = Num_of_Bricks*Cost

print(f"Walls Surface Area: {Surface_Area_of_Walls}m2")
print(f"Bricks Required: {Num_of_Bricks}")
print(f"Total Cost of Bricks: ${Total_Cost_of_Bricks}")

# Homework #3
Distance = int(input("Enter the distance of the trip in km:"))
Efficiency = float(input("Enter the fuel efficiency of your vehicle in L/100km:"))
Fuel_Price = float(input("Enter the current fuel price in CAD:"))
Pax = int(input("Enter the number of passengers in the vehicle:"))

# Calculate
Total_Fuel = round(Distance/Efficiency,2)
Total_Fuel_Cost = round(Total_Fuel*Fuel_Price,2)
Split_Cost = round(Total_Fuel_Cost/Pax,2)

# Print
print(f"\nTotal Fuel: {Total_Fuel}")
print(f"Total Fuel Cost: ${Total_Fuel_Cost}")
print(f"The Cost Split evenly among all {Pax} passengers is: {Split_Cost}")

