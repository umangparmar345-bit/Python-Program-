'''Banking System Using Functions
Functions for:
Deposit
Withdraw
Check Balance'''

balance = 0

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited Successfully")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print("Withdrawal Successful")

def check_balance():
    print("Current Balance =", balance)


# Main Program
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)
    elif choice == 2:
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)
    elif choice == 3:
        check_balance()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid Choice")
