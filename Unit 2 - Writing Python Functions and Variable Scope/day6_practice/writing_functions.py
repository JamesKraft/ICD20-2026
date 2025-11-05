import math
def format_circle_radius(radius,decimals):
    # Returns: Area is 50.27
    area = math.pi*(radius**2)
    area_formatted = round(area,decimals)
    return f"Area is equal to {area_formatted}!"

def velocity(distance, time, decimals):
    # Returns: Speed: 3.24 m/s
    speed = distance/time
    speed_formatted = round(speed,decimals)
    return f"Speed: {speed_formatted} m/s"

def format_total_price(price, quantity, tax, decimals):
    # Returns: Total: $34.653
    total = (price*quantity)*((tax*0.01)+1)
    total_formatted = round(total,decimals)
    return f"Total: ${total_formatted}"

def temperature_report(celsius,decimals):
    # Returns: Temp: 75.32F
    temperature_in_F = (celsius*(9/5))+32
    temperature_formatted = round(temperature_in_F,decimals)
    return f"Temp: {temperature_formatted}F"

def travel_summary(distance,hours,decimals):
    # Returns: You travelled 550.0 km in 5.0 hours. Avg speed: 110.0 km/h
    avg_speed = round((distance/hours),decimals)
    return f"You travelled {distance} km in {hours} hour(s). Avg speed: {avg_speed} km/h"

print(format_circle_radius(10,1))
print(velocity(100,60,1))
print(format_total_price(100,2,13,2))
print(temperature_report(1,1))
print(travel_summary(100,1,1))