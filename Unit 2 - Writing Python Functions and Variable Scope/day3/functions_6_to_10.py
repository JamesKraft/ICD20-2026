import math 
def total_with_tax(price,tax_rate):
    rate = (tax_rate*0.01)+1.00
    total_price = (price*rate)
    return f"Total: ${total_price:.2f}"

def bmi(weight,height):
    actual_bmi = (weight/height)**2
    return f"Your BMI is equal to {actual_bmi}"

def greeting_with_age(name,age):
    return f"His {name}, you are {age} years old!"

def pay(hours,rate):
    real_pay = hours*rate
    return f"You are paid ${real_pay:.2f} total"

def format_score(score,decimals):
    format = round(score, decimals)
    return f"Score: {format}%"

print(total_with_tax(20,13))
print(bmi(90,180))
print(greeting_with_age("James", 15))
print(pay(108,89))
print(format_score(15,2))