# Q1
print(f"Hello James!")

# Q2
height = 160
age = 15
is_student = True
print(f"James has a height of {height}cm, is {age} years old, and stating that he is a student is {is_student}")

# Q3
print(f"There is a person named John, who is 25 years old, and is 1.75 metres tall.")

# Q4
import math
pi = math.pi
pir = (f"{pi:.2f}")
print(f"{pir:>20}")

# Q5
num1 = 10
num2 = 5
calc = num1 + num2
print(f"Adding {num1} to {num2} is equal to {calc}")
print(f"Multiplying {num1} by {num2} is equal to {num1*num2}")

# Q6 
int = int(input("Enter a counting number:"))
print(f"The square of {int} is {int**2}")

# Q7
float = float(input("Enter a decimal number:"))
floatnot = round(float)
print(f"The integer value is {floatnot}")

# Q8
name = input("What is your name?")
age = int(input("Enter your age:"))
print(f"Hello {name}, you are {age} years old!")

# Q9
float1 = float(input("Enter a decimal:"))
float2 = float(input("Enter a decimal:"))
average = (float1 + float2)/2
print(f"The average of {float1} and {float2} is {average}")

# Q10
# If you do not choose proper variable names in python, and you choose something incredibly dumb, you will not remember the name of the variable and will mess the name up later on.
# Ex. choose variable fl for a float number.

# Q11
# When you imbed int or float in f-string, it will merely print it out. However, it should be noted that if you make a number a string, python will not let you add or subtract it. 
# Ex. (f"{num1*num2}") does not work if num1 and num2 have not been defined as integers or floats. 

# Q12
# Using parantheses in math is very important as it forces python to for sure use BEDMAS correctly. 
# Ex. (math.pi*12)+24

# Q13
# With an f-string, you can format it to be aligned left/right/centre. If you align it correctly, the output will look very polished. 
# f_string = number
# print(f"{f_string:=20}") - this string is center aligned with 20 characters. 

# Q14
# Variables can store four different data types. Int is a counting number, Boolean assigns 1 or 0 to a numer (yes/no,true/false etc.)
# Float is a decimal, and string is text. 

# Q15
# The role of the input function is to accept user input in the form of int, float, bool or string. 
# By converting input to int -> int(input("Enter a integer value: "))
