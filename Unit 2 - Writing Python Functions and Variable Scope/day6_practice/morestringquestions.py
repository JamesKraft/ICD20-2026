str = input("Enter a string:")
stra = input("Enter a new string:")

def first_last(str):
    return (str[0]) + (str[-1])

def middle_two(str):
    return (str[1:3])

def without_ends(str):
    cal = len(str)
    return (str[1:(cal-1)])

def rotate_left2(str):
    return (str[2:]) + (str[0:2])

def rotate_right2(str):
    cal = len(str)
    return (str[-2:]) + (str[0:(cal-2)])

def back_front_halves(str):
    cal = ((len(str))+1)//2
    return (str[cal:]) + (str[:cal]) 

def every_other(str):
    return (str[0::2])

def last3_reversed(str):
    return (str[-1]) + (str[-2]) + (str[-3])

def wrap_with_ends(str):
    return (str[0]) + str + (str[-1])

def middle_pair(str):
    cal = (len(str))//2
    return (str[cal-1:cal+1])

def remove_first_two(str):
    return (str[2:])

def sandwich_center(str,stra):
    cal = (len(str))//2
    return str + (stra[cal-1:cal+1]) + str

def first_half(str):
    cal = (len(str))//2
    return (str[0:cal])

def last_half(str):
    cal = (len(str))//2
    return (str[cal:])

def edges2(str):
    cal = (len(str))
    return (str[0:cal]) + (str[cal:])

def clip4(str):
    return (str[0:4])

def swap_ends(str):
    cal = (len(str))//2
    return (str[-1]) + (str[1:(cal+1)]) + (str[0])

def trim3(str):
    return (str[3:-3])

def center3(str):
    cal = (len(str))//2
    return (str[cal-1:cal+2])

def weave_edges(str,stra):
    return (str[0]) + (stra[0]) + (str[-1]) + (stra[-1])


print(back_front_halves(str))
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
print(remove_first_two(str))
print(sandwich_center(str,stra))
print(first_half(str))
print(last_half(str))
print(edges2(str))
print(clip4(str))
print(swap_ends(str))
print(trim3(str))
print(center3(str))
print(weave_edges(str,stra))