# Example #1
name = input("Please enter your name:")
print(f"Hello {name}!")

# Example #2
num1 = input("Please enter a number:")
num2 = input("Please enter a different number:")

num1r = int(num1)
num2r = int(num2)

print(f"When adding {num1r} with {num2r} you get {num1r + num2r}")
print(f"when subtracting {num1r} with {num2r} you get {num1r - num2r}")
print(f"when multiplying {num1r} with {num2r} you get {num1r*num2r}")
print(f"when dividing {num1r} with {num2r} you get {num1r/num2r}")

# Example #3
c = input("Input a temperature in Celsius:")

c1 = int(c)

print(f"{c1} degrees Celsius is equal to {(c1*9/5)+32} Fahrenheit")

# Example #4
city = input("What city do you live in?")
name1 = input("What is your name?")
age1 = input("what is your age?")

print(f"Hi {name1}! It is so cool that you live in {city} and that you are {age1} years old!")

# Example #5
len = input("Enter a length value:")
wid = input("Enter a width value:")

le1 = int(len)
wi2 = int(wid)

print(f"With a length of {le1} and a width of {wi2} you get an area of {le1*wi2}!")

# Example #6
ca1 = input("Enter a value in Canadian Dollars:")
us1 = input("Enter the exchange rate for United States Dollars to CAD:")

cad = int(ca1)
usd = float(us1)

print(f"{cad} dollars CAD is equal to {cad*usd} US Dollars!")