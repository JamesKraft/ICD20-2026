# Beginning of Upper School Resource Calculator

print(f"Upper School Resource Density Calculator \n----------------------------------------")

# Collect Data

classrooms = int(input("How many classrooms are in the Upper School? "))
fountains = int(input("How many student water fountains? "))
restrooms = int(input("How many student restrooms? "))
add_resource = (input("Enter ONE additional resource to track (e.g., vending machines): "))
added_resource = int(input(f"How many {add_resource.lower()}? "))

# String Collection

fountain_condition = (input("Condition of fountains: "))
restroom_condition = (input("Condition of restrooms: "))
resource_condition = (input(f"Condition of {add_resource.lower()}: "))

# Calculations

fountain_per_class = round(fountains/classrooms,2)
restroom_per_class = round(restrooms/classrooms,2)
resource_per_class = round(added_resource/classrooms,2)

# Print

print(f"\nResults\n-------")
print(f"Fountains per classroom: {fountain_per_class} (Condition: {fountain_condition})")
print(f"Restrooms per classroom: {restroom_per_class} (Condition: {restroom_condition})")
print(f"{add_resource.title()} per classroom: {resource_per_class} (Condition: {resource_condition})")
print(f"\nThanks for helping map our Upper School resources!")

# Reflection Questions

# Question #1: 
# Writing this code has allowed me to understand whether or not a certain number of people have adequate resources. 
# For example, if the ratio of people to restrooms is too small, I will know to install more restrooms. 

# Question #2: 
# If I had more time, I would analyze the number of students in the BVG Upper School. 
# Therefore, I would analyze the density of students to restrooms, fountains and cafeteria tables!