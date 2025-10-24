# Q1
print(f"\n*\n**\n***\n****")

# Q2
message = "Python Programming"
length = len(message)
print(f"\nThe message {message} is made up of {length} characters")

# Q3
name = "James"
age = 15
print(f"\nMY NAME IS {name} AND I AM {age*2} YEARS OLD!")

# Q4
import math
pi = math.pi
pir = round(pi,5)
print(f"\n{pir:>20}")

# Q5
num1 = 25
num2 = 7
calc = round(num1/num2,3)
print(f"\n{num1} divided by {num2} is equal to {calc}")

# Q6
int1 = int(input("\nEnter a counting number:"))
print(f"{round(math.sqrt(int1),2)}")

# Q7
float2 = float(input("Enter a decimal number:"))
notfloat = int(float2)
print(float2)
print(notfloat)

# Q8
birth_year = int(input("Enter your birth year:"))
current_year = int(input("Enter the current year"))
age = current_year - birth_year
print(f"You are {age} years old!")

# Q9
float3 = float(input("Enter a floating point number:"))
print(f"\n{float3}")
print(f"{float3:.0f}")

# Q10
Apple = "Apple"
Apple_Price = "$0.99"
Apple_Discount = "10%"

Banana = "Banana"
Banana_Price = "$0.49"
Banana_Discount = "5%"

Orange = "Orange"
Orange_Price = "$1.29"
Orange_Discount = "15%"

print(f"\n{"Product":<16}{"Price":<16}{"Discount":<16}")
print(f"{Apple:<16}{Apple_Price:<16}{Apple_Discount:<16}")
print(f"{Banana:<16}{Banana_Price:<16}{Banana_Discount:<16}")
print(f"{Orange:<16}{Orange_Price:<16}{Orange_Discount:<16}")