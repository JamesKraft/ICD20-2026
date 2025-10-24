import math
def format_circle_area(radius,decimals):
    area = math.pi*(radius**2)
    rounda = round(area,decimals)
    return f"Area is {rounda}"

def velocity(distance, time, decimals):
    speed = distance/time
    return f"Speed: {speed:.{decimals}f}m/s"

def format_total_price(price,quantity,tax,decimals):
    total_price = (price*quantity)*((tax*0.01)+1.00)
    return f"Total: ${total_price:.{decimals}f}"

def temperature_report(celsius,decimals):
    convert_fahrenheit = ((celsius*9/5)+32)
    round_f = round(convert_fahrenheit,decimals)
    return f"Temp: {round_f}F"

def travel_summary(distance,hours,decimals):
    avg_speed = distance/hours
    return f"You travelled {distance}km in {hours} hours. Avg speed: {avg_speed:.{decimals}f}km/h"

print(format_circle_area(2,2))
print(velocity(2,2,2))
print(format_total_price(24,2,13,2))
print(temperature_report(-20,2))
print(travel_summary(1000,2,2))