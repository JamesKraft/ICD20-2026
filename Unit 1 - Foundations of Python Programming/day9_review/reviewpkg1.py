# T1: Q1 - The purpose of printing is to display words,numbers or strings in the python command prompt. 
# T1: Q2 - Demonstrate how to use print function:
vx = "VS Code"
print(f"\nHello, my name is James!")
print(vx)
# T1: Q3 - Demonstrate how to use Print function with multiple variables and strings. 
plane = "Boeing 787-9"
plane2 = "Boeing 777-300ER"
plane3 = "Boeing 777-200LR"
print(f"\nSome of my favorite planes are {plane}, {plane2}, and the {plane3}")
# T1: Q4 - I will create a table using hte print function. This table will be of planes, and how great they are, according to me. 
# It will be aligned left. 
b787 = "Boeing 787-9"
B787r = "10/10"

b777 = "Boeing 777-300ER"
B777r = "10/10"

ptype = "Plane Type"
rting = "Rating"

print(f"\n{ptype:<18}{rting:<18}")
print(f"{b787:<18}{B787r:<18}")
print(f"{b777:<18}{B777r:<18}")

# T2: Q1 - The role of variables in programming is to assign a series of letters or numbers a value as a number,
# or a string. Example: p1 = "Boeing 787-9 Dreamliner"
# T2: Q2 - 
# Integer: A counting number, negative, positive, or 0.
# Floats: A decimal value. 
# Boolean: Assigns something a 1 or 0, representing true or false, yes or no etc.
# String: Letters enclosed in quotations. ex: "Plane"
# T2: Q3
x = 1
print(x)
# T2: Q4 - Convert string to integer. If you do not convert, python cannot perform math calcs with string. 
x1 = input("Input a number:")
x2 = int(x1)
print(x2)
# T2: Q5 - Sometimes, when getting a user to input a value, you must declare whether that value is int, float, string or boolean.
xnumber = int(input("Enter a random number:"))
# or you can do this:
xnumber = input("Please enter a number:")
xnumer1 = int(xnumber)
print(xnumer1)
# T2: Q6 - If you do not choose appropriate variable names, later on, a hundred or so lines later, you will not remember what you named a specific variable. 
# Additionally, it makes it easier for the coder to write code quicker if the names are intuitive. 
# T3: Q1 - F-strings are very simple ways to format strings. This allows the coder to quickly add vairables into strings. 
# Additionally, it allows the user to right/left align the string and to create tables simply. 
# T3: Q2 - print(f"") - This is how to write f-strings. 
# T3: Q3 - print(f"Hi my name is {name}") - This is how to put variables inside of an f-string.
import math
name = "James"
print(f"Hi my name is {name}")
# T3: Q4
x = 12
y = 54
r = 10
area_circle = math.pi*r**2
print(f"The area of a circle with radius {r} is equal to {area_circle}")
# T3: Q5 - If you use f-strings to format output, you easily create tables. If you do not use f-strings, it will take you 2-3 times as long to create simple things. 
# T4: Q1 - Decimal place for floats (to 2 decimal places) - align left/right
x = 123.456
print(f"{x:.2f}")
print(f"{x:>10}")
print(f"{x:=20}")
print(f"{x:<}")
# T4: Q2 - These valuable skills of align left/center/right and setting the width for fields can be used in complex graphs. 
# T4: Q3 - Additionally, f-string formatting skills are very important for python!
# T5: Q1 - The equals sign (=) just makes one value/string equal to another value/string. 
# T5: Q2 - + - * /
x = 12
y = 12
add = 12+12
sub = 12-12
multiplication = 12*12
division = 12/12
print(f"{add}{sub}{multiplication}{division}")
# T5: Q3 - Done, see lines 72-78
# T5: Q4 - Python knows the order of operations, but it is still hepful to formation equations keeping BEDMAS in mind. 
x = 12
y = 16
print(f"{(x*y)+y}")
# T5: Q5 - Using parentheses for order of operations is good as it makes sure that python will follow BEDMAS correctly. 
# T6: Q1 - Input is very important. It allows the user to change the equations, and display and calculate things that the user wants to do. 
# T6: Q2 - Input for int - I have converted the string to int in the line. 
x3 = int(input("Enter a funny number:"))
print(x3)
# T6: Q3 - See lines 87-88
# T6: Q4 - Perform math operations with user entered values. 
x4 = int(input("Enter a round number:"))
x5 = int(input("Enter another, different round number:"))
print(f"{x4} multiplied by {x5} is equal to {x4*x5}")
# T6: Q5 - Perform interactive operations with user entered values. 
cat = input("Enter a category (e.g. planes):")
rate = int(input(f"Rate {cat} on a scale of 1-10:"))
like = input(f"What do you like about {cat}? Elaborate:")
print(f"You chose the category of {cat}, you though it was {rate}/10, and you like that it was {like}!")