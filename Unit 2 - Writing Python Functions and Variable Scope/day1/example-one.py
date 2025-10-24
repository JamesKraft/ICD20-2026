# Note - Ctrl K then Ctrl 1 closes all bodies of code for functions
# Ctrl K then Ctrl J to show


# Prints a welcome message to the user
# Parameters: none
# Returns: nothing
def show_welcome():
    print("Welcome to the program! Let's learn functions.")

# Calculates and returns the area of a rectangle
# Parameters: width (float), height (float)
# Returns: area (float)
def calculate_area(width, height):
    return width * height

# Prints a simple greeting with a name
# Parameters: name (string)
# Returns: nothing
def greet(name):
    print("Hello, " + name + "!")

# Converts Celsius to Fahrenheit
# Parameters: temp_c (float)
# Returns: temperature in Fahrenheit (float)
def celsius_to_fahrenheit(temp_c):
    return temp_c * 9 / 5 + 32

# Adds two numbers and returns the sum
# Parameters: num1 (int), num2 (int)
# Returns: sum (int)
def add_numbers(num1, num2):
    return num1 + num2

# Prints a horizontal divider line
# Parameters: none
# Returns: nothing
def print_divider():

    print("-------------------------")

show_welcome() # Function #1

area = calculate_area(2.5, 10.0) # Function #3 - Use this way if you need to store the variable
print(f"The area is {area}")

print(f"The area is {calculate_area(2.5, 10.0)}") # Function #3 - Use this way if you DO NOT NEED TO store the area

greet("James Kraft") # Function #3

print(f"The temperature in North York in F is {celsius_to_fahrenheit(21.0)}") # Function #4

x = 6
y = 8

print(f"When adding numbers {x} and {y} the sum is {add_numbers(x,y)}") # Function #5

print_divider() # Function #6