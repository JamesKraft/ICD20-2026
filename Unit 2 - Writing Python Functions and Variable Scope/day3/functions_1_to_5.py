import math
def greeting(name):
    return f"Hello {name}"

def cube(num):
    cubed = num**3
    return cubed

def area_rectangle(length,width):
    area = length*width
    return area

def format_pi(decimals):
    pi_rounded = round(math.pi,decimals)
    return pi_rounded

def seconds(hours):
    seconds_hours = hours*(60*60)
    return seconds_hours

print(greeting("Kevin"))
print(cube(2))
print(area_rectangle(10,10))
print(format_pi(2))
print(seconds(6))



