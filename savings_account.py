"""Import the Account class from the Account.py file."""
from Account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance."""
    # Create an instance of the `Account` class
    savings_account = Account(balance, interest_rate)

    # Calculate interest earned
    interest_earned = balance * (interest_rate * months/12)


    # Update the savings account balance
    updated_balance = balance + interest_earned

    # Set the updated balance
    savings_account.set_balance(updated_balance)

    # Set the interest earned
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned
    return updated_balance, interest_earned