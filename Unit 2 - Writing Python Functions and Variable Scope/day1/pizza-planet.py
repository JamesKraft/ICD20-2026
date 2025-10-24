# Prints a welcome message
# Parameters: none
# Returns: nothing
def greet_customer():
    print("Welcome to Pizza Planet! 🍕🚀")

# Calculates total price of a pizza
# Parameters: base_price (float), extra_toppings (int)
# Returns: total price (float)
def get_total(base_price, extra_toppings):
    return base_price + (extra_toppings * 1.25)

# Prints a thank-you message
# Parameters: name (string)
# Returns: nothing
def thank_you(name):
    print("Thanks for ordering, " + name + "! Enjoy your pizza.")

# Returns number of slices based on pizza size
# Parameters: size (string)
# Returns: number of slices (int)
def slices_for_size(size):
    if size == "small":
        return 6
    elif size == "medium":
        return 8
    elif size == "large":
        return 10
    else:
        return 0

greet_customer()
name = "James Kraft"
size = "medium"
price = get_total(10.00, 2)
thank_you(name)
slice_count = slices_for_size(size)
print(f"The customer will receive {slice_count} slices")