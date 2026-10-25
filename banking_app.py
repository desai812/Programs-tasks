# Task 03 - Banking Console Application (Balance, Deposit & Withdrawal) - Python

# Fixed opening balance
balance = 10000


def show(amount):
    """Show whole amounts without .0 (11500.0 -> 11500)."""
    if amount == int(amount):
        return str(int(amount))
    return f"{amount:.2f}"


print("Welcome to Kiran Bank")
print("Opening Balance: Rs.", show(balance))

while True:
    # Step 1: Main menu
    print("\n----- BANKING MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        # Step 2: Check balance
        print("Current Balance: Rs.", show(balance))

    elif choice == "2":
        # Step 3: Deposit money
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue

        if amount <= 0:
            print("Invalid amount! Deposit must be greater than Rs. 0.")
        else:
            balance = balance + amount
            print("Deposit successful.")
            print("Updated Balance: Rs.", show(balance))

    elif choice == "3":
        # Step 4: Withdraw money
        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue

        if amount <= 0:
            print("Invalid amount! Withdrawal must be greater than Rs. 0.")
        elif amount > balance:
            print("Transaction failed: Insufficient balance.")
            print("Current Balance: Rs.", show(balance))
        else:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Updated Balance: Rs.", show(balance))

    elif choice == "4":
        # Step 6: Exit
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        # Step 5: Invalid menu choice
        print("Invalid choice! Please enter 1, 2, 3 or 4.")
