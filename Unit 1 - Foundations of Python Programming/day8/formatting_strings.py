number = 42
print(f"|{number}|")     # Displays |42|
print(f"|{number:>5}|") # Greater than sign > points to the right or |   42| width of 5 right aligned
print(f"|{number:<5}|") # Less than sign < points to the left or |42   | width of 5 left aligned
print(f"|{number:^5}|") # Carrot sign ^ is centered or | 42  | width of 5 centre alinged /// needs an even # of characters to be centered
print(f"|{number:^6}|") # Perfectly centered as it has an even number of digits. 


value = 123.456789
print(f"{value}") # prints value
print(f"{value:.2f}") # the .2f specifies that the # should only have two decimal places. It does ROUND.
print(f"{value:.3f}") # the .3f rounds to three decimal places and rounds.

value = 7.5
print(f"{value:.2f}") # If there is nothing after the decimal place, python puts a zero. 

percentage = 15/17
print(f"{percentage:.1%}") # the percent dictates # of decimal places and gives percentage. 


cost = 5.67
print(f"The cost is ${cost:.2f}")