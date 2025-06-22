✅ Description of Basic ATM Simulation Code:
This Python program simulates a basic ATM system with simple functionalities:

PIN Verification:

The user is asked to enter a PIN to access the ATM.

If the entered PIN matches the preset one (1234), the user can continue; otherwise, the program exits.

Main Menu (Loop):

After successful login, a menu with three options is displayed:

Check Balance

Withdraw Money

Exit

The program uses a while loop to keep showing the menu until the user chooses to exit.

Options Handling (If-Else):

Check Balance: Displays the current balance.

Withdraw Money:

User enters the amount to withdraw.

Checks if sufficient balance is available.

Deducts the amount if possible; otherwise, shows an "Insufficient funds" message.

Exit: Ends the program with a thank-you message.

Invalid Input: If the user selects an unknown option, an error message is shown.

Initial Values:

Balance is set to $1000 initially.

PIN is hardcoded as 1234 for simplicity.

✅ Concepts Used:
Variables

if-else statements (decision making)

while loop (repetition)

Input/output using input() and print()

Basic arithmetic operations for balance management

