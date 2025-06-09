def greet():
    print("Hi! Welcome to the Money Bank!")
    print()

balance = 100
transactions = []

greet()

name = input("What is your name? ")
print()

while True:
    print("-" * 30)
    print("BALANCE: $" + str(balance))
    print()

    print(
        "What do you want to do?\n"
        "1. Deposit\n"
        "2. Withdraw\n"
        "3. See transaction history\n"
        "4. Exit"
    )
    print()

    choice = input(" > ")
    print()

    choice = int(choice)

    if choice == 1:
        deposit_amount = int(input("How much do you want to deposit? "))
        balance = balance + deposit_amount
        transactions.append(name + " deposited $" + str(deposit_amount))
        print("Successfully deposited $" + str(deposit_amount))

    elif choice == 2:
        withdraw_amount = int(input("How much do you want to withdraw? "))
        if withdraw_amount > balance:
            print("Insufficient funds.")
        else:
            balance = balance - withdraw_amount
            transactions.append(name + " withdrew $" + str(withdraw_amount))
            print("Successfully withdrew $" + str(withdraw_amount))

    elif choice == 3:
        print("--- Transaction History ---")
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(" - " + transaction)
        print("---------------------------")

    elif choice == 4:
        print("Good bye!")
        break

    else:
        print("I don't understand that choice.")

    print()