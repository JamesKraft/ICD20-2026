str = input("Enter a string")
str1 = input("Enter a second string")

def remove_first_two(str):
    cal = len(str)
    return (str[2:cal])

def sandwich_center(str, str1):
    cal = len(str)
    cal1 = len(str1)
    value1 = (str1)
    value = (str[1:(cal-1)])
    return value1 + value + value1

def first_half(str):
    cal = len(str)
    value = (str[0:(cal//2)])
    return value

def last_half(str):
    cal = len(str)
    value = (str[(cal//2):cal])
    return value

def edges2(str):
    cal = len(str)
    value = (str[0:2])
    value1 = (str[-1])
    value2 = (str[-2])
    return value + value1 + value2

def clip4(str):
    return (str[0:4])

def swap_ends(str):
    cal = len(str)
    value = (str[0])
    value1 = (str[1:(cal-1)])
    value3 = (str[(cal-1)])
    return value3 + value1 + value

def trim3_yay(str):
    value = (str[3:-3])
    return value

def center(str):
    m = (len(str))//2
    value = (str[m-1:m+2])
    return value

def weave_edges(str,str1):
    m = len(str)
    return (str[0]) + (str1[0]) + (str[-1]) + (str1[-1])

print(remove_first_two(str))
print(sandwich_center(str, str1))
print(first_half(str))
print(last_half(str))
print(edges2(str))
print(clip4(str))
print(swap_ends(str))
print(trim3_yay(str))
print(center(str))
print(weave_edges(str,str1))
