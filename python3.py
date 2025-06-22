# Basic ATM Simulation

balance = 1000  # Initial balance
pin = 1234      # Example PIN

print("Welcome to Simple ATM")

# PIN Verification (optional)
entered_pin = int(input("Please enter your PIN: "))
if entered_pin != pin:
    print("Incorrect PIN. Exiting.")
else:
    while True:
        print("\n==== ATM Menu ====")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == '1':
            print(f"Your current balance is: ${balance}")
        
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= balance:
                balance -= amount
                print(f"Please collect your cash. New balance: ${balance}")
            else:
                print("Insufficient funds.")
        
        elif choice == '3':
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")
