# Boolean
x = True
y = False

print(f"The value of being x 15 is {x}")

x = 23
x1 = bool(x)
print(x1)

# String
age = 15
name = "James"

print(f"My name is {name} and I am {age} years old!")

# Integer
x = "25"
xproper = int(x)
print(f"25 multiplied by 2 is equal to {xproper*2}")

# Float
x = 0.78
xproper = int(x)
print(f"{x}")
print(f"{xproper}")

# Escape Sequence
print(f"\nHi my name is James!")
print(f"\\Hi my names is James!")

# Import Math
import math
print(f"12 multiplied by pi is equal to {round(math.pi*12,2)}")
x = 6
print(f"{x} square rooted is equal to {math.sqrt(x)}")
r = 12
print(f"The area of a circle with radius {r} is equal to {(math.pi)*(r**2)}")

# Input/Input Conversion
robicat = str(input("What is your favorite type of cat?"))
gobicat = int(input(f"If your favorite type of cat is a {robicat}, then what would you rate it out of 10?"))
print(f"Your favorite type of cat is the {robicat} and you thought it had a rating of {gobicat}/10!")

# Output Formatting (L,R,C)
robi = "Robi Cat"
gobi = "Gobi Cat"
cat = "Funny Cat"
print(f"{robi:^20}")
print(f"{gobi:>20}")
print(f"{cat:<10}")

# Rounding/Percentage inside F-Strings
x = 123.4567890
y = 234567.89990909
print(f"Rounding is cool: {x:.2f}  {y:.4f}")
x = 0.88
y = 0.99
z = 1.00
print(f"F-String percentages are awesome: {x:.2%}{y:.1%}{z:.0%}")

# Upper/Lowercase
x = "uppercase funny bunny"
y = "LOWERCASE GOBI CAT"
print(f"{x.upper()} {y.lower()}")

# Calculating Length of Characters
x = str(12345375687658974659764589734658736587436587936549873649587364985)
y = "dsfsdhfuerhiuthfnkjghertiytrghfvygrhfuejwgfhjdkghfjkdlsghfjdkslaghfjdkstyrueiowptyrueiwoqpghfjdkslvncm"
xlen = len(x)
ylen = len(y)
print(f"{xlen} {ylen}")

# Math Operators
x = 90
y = 98
z = 94
avg = (x+y+z)/3
add = (x+y+z)
sub = (x-y-z)
multiplication = (x*y*z)
division = (x/y/z)
print(f"I did many operations for three numbers of {x} {y} and {z}. Here are they:\n{avg} {add} {sub} {multiplication} {division}")

# Printing
x = "string"
y = 123
z = 0.98
a = True
print(f"{x} {y} {z} {a}")

# Concatenating Strings
x = 10
y = 12
print("The value of ", x, "multiplied by ", y ,"is equal to ", x*y)
x = "comma"
y = "concatenating strings"
print("I like the word " + x + " and I like " + y)

# F-Strings
x = 10
y = 20
print(f"F-Strings are better and {x} multiplied by {y} equals to {x*y}. Also, you do can mathematical operations in F-Strings!")