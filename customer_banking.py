# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    """This function prompts the user to enter the savings and cd account details."""
    # Prompt the user for savings account details
    savings_balance = check_valid_num("Enter the savings account balance: ", 'float')
    savings_interest = check_valid_interest("Enter the savings account interest rate: ")
    savings_maturity = check_valid_num("Enter the number of months for the savings account: ", 'int')

    # Call the create_savings_account function
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print savings account details
    print(f"\nSavings Account:")
    print(f"Interest earned: ${savings_interest_earned:,.2f}")
    print(f"Updated balance: ${updated_savings_balance:,.2f}")

    # Prompt the user for CD account details
    cd_balance = check_valid_num("\nEnter the CD account balance: ", 'float')
    cd_interest = check_valid_interest("Enter the CD account interest rate: ")
    cd_maturity = check_valid_num("Enter the number of months for the CD account: ", 'int')

    # Call the create_cd_account function
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print CD account details
    print(f"\nCD Account:")
    print(f"Interest earned: ${cd_interest_earned:,.2f}")
    print(f"Updated balance: ${updated_cd_balance:,.2f}")

def check_valid_interest(question):
    while True:
        user_input = input(question).strip()

        try:
            if user_input.endswith("%"):
                # Handle percentage input
                interest = float(user_input[:-1]) / 100
            else:
                # Handle decimal input
                interest = float(user_input)

            if 0 <= interest < 1:
                return interest
            else:
                print("Invalid input. Please enter a valid interest rate (0-100% or 0-1).\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

        print("For example: '10%' or '0.10'\n")

def check_valid_num(question, type='float'):
    while True:
        number = input(question)
        if number.isdigit() and int(number) > 0:
            if type == 'float':
                return float(number)
            else:
                return int(number)
        print("Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    main()