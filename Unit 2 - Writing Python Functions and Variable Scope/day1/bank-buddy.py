# Prints the welcome message
# Parameters: none
# Returns: nothing
def start_bank_session():
    print("🏦 Welcome to Bank Buddy!")

# Calculates new balance after deposit
# Parameters: balance (float), deposit (float)
# Returns: updated balance (float)
def deposit_money(balance, deposit):
    return balance + deposit

# Calculates new balance after withdrawal
# Parameters: balance (float), withdrawal (float)
# Returns: updated balance (float)
def withdraw_money(balance, withdrawal):
    return balance - withdrawal

# Prints a transaction summary
# Parameters: name (string), balance (float)
# Returns: nothing
def show_summary(name, balance):
    print(name + "'s current balance is $" + str(round(balance, 2)))

start_bank_session()
name = "Aiden"
balance = 100.00
deposit = 25.50
balance = deposit_money(balance, deposit)
print(f"Your balance is {balance}")
balance = withdraw_money(balance, 40.00)

print(show_summary(name,balance))