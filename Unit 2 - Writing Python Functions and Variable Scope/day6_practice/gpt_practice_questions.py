str = input("Enter a String")
stra = input("Enter a new string")
def every_other(str):
    return (str[0::2])

def rotate_right2(str):
    cal = len(str)
    return (str[-2:]) + (str[0:cal-2])\

def sandwich_center(str,stra):
    cal = (len(str))//2
    return str + (stra[cal-1:cal+1]) 

def format_total_price(price, quantity, decimals, tax):
    total = (price*quantity)*((tax*0.01)+1)
    total_formatted = round(total,decimals)
    return f"Total: ${total_formatted}"

print(every_other(str))
print(rotate_right2(str))
print(sandwich_center(str,stra))
print(format_total_price(11,2,5,2))