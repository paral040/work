balance = 100

while True:
    print("Menu:")
    print("(1) Deposit")
    print("(2) Withdraw")
    print("(3) Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        deposit_amount = float(input("Enter the amount to deposit: "))
        balance += deposit_amount
        print(f"Deposit successful. Your new balance is £{balance}")
    elif choice == "2":
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"Withdrawal successful. Your new balance is £{balance}")
        else:
            print("Error: Insufficient funds.")
    elif choice == "3":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")