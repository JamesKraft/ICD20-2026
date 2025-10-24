# Homework #1
fn = input("What is your first name?")
ln = input("What is your last name?")
ufn = fn.upper()
uln = ln.upper()
print(f"Your full name is {ufn} {uln}!")

# Homework #2
grapes = float(input("What is the price of the Grapes you bought?"))
cookies = float(input("What is the price of the cookies you bought?"))
croissants = float(input("What is the price of the croissants you bought?"))

total = (grapes + cookies + croissants)*1.08
rounded_total = round(total,2)

print(f"The total cost of everything you bought was ${rounded_total}")

# Homework #3
days = int(input("What is the total number of days you spent outside last week?"))

hours = days*24

print(f"Last week, you spent {days} days or {hours} hours playing outside!")

# Homework #4
hours1 = float(input("How many hours did you spend in the car on your last road trip?"))
distance = float(input("How many kilometers did you drive the last time you went on a road trip?"))

speed = distance/hours1

print(f"On the last road trip you went, you drove at {speed} km/h!")

