# ATM System Using Functions

# Deposit Function
def deposit(balance):
    try:
        amount = int(input("Enter amount to deposit:"))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully!")
        else:
            print("Enter a valid amount")
    except ValueError:
        print("Invalid input!")
    return balance


# Withdraw Function
def withdraw(balance):
    try:
        amount = int(input("Enter amount to withdraw:"))
        if amount>balance or amount<=0:
            print("Invalid amount!")
        else:
            balance -= amount
            print("Withdrawal successful")
    except ValueError:
        print("Invalid input!")
    return balance


# Check Balance Function
def check_balance(balance):
    print("Current Balance:", balance)


# ATM Menu Function
def atm_menu():
    print("\nATM MENU")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")


# Main Function
def main():
    balance = 10000

    while True:
        atm_menu()
        choice = input("Enter your choice: ")

        if choice=='1':
            balance=deposit(balance)

        elif choice=='2':
            balance=withdraw(balance)

        elif choice=='3':
            balance=check_balance(balance)

        elif choice=='4':
            print("Thank you for using the ATM!")
            break

#main() function
main()