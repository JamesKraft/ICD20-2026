str = input("Enter a string:")

def first_last(str):
    new_variable = (str[0])
    new_variable2 = (str[-1])
    return (new_variable) + (new_variable2)

def middle_two(str):
    div_proper = (str[1:3])
    return (div_proper)

def without_ends(str):
    cal = len(str)
    value = (str[1:(cal-1)])
    return (value)

def rotate_left2(str):
    cal1 = len(str)
    value1 = (str[2:cal1])
    value2 = (str[0:2])
    return (value1) + (value2)

def rotate_right2(str):
    cal = len(str)
    value = (str[(cal-2):(cal)])
    value1 = (str[0:3])
    return (value) + (value1)

def back_front_halves(str):
    cal = len(str)
    value = (str[1:(cal-2)])
    value1 = (str[(cal-2):(cal)])
    value2 = (str[0])
    return (value1) + (value2) + (value)

def every_other(str):
    cal = len(str)
    value = (str[0:cal:2])
    return (value)

def last3_reversed(str):
    return (str[-1]) + (str[-2]) + (str[-3])

def wrap_with_ends(str):
    cal = len(str)
    value = (str)
    value1 = (str[0])
    value2 = (str[(cal-1)])
    return (value1) + (value) + (value2)

def middle_pair(str):
    cal = len(str)
    value = (str[1:(cal-1)])
    return value

print(first_last(str))
print(middle_two(str))
print(without_ends(str))
print(rotate_left2(str))
print(rotate_right2(str))
print(back_front_halves(str))
print(every_other(str))
print(last3_reversed(str))
print(wrap_with_ends(str))
print(middle_pair(str))