# 🏦 Banking System Project

## 📚 Table of Contents
- [Overview](#Overview)
- [File Structure](#File-Structure)
- [Detailed Explanation](#Detailed-Explanation)
  - [account.py](#accountpy)
  - [cd_account.py](#cd_accountpy)
  - [savings_account.py](#savings_accountpy)
  - [customer_banking.py](#customer_bankingpy)
- [Usage](#usage)
- [Contributing](#contributing)

## 🌟 **Overview**

This project implements a simple banking system that allows users to create and manage savings and CD (Certificate of Deposit) accounts. It demonstrates object-oriented programming principles and modular design in Python.

## 📂 **File Structure**
```python
banking_system/
│
├── account.py
├── cd_account.py
├── savings_account.py
└── customer_banking.py
```

## 🔍 **Detailed Explanation**

### account.py

This file defines the base `Account` class, which serves as a template for different types of bank accounts.

**Key features:**
- Initializes an account with a balance and interest rate
- Provides methods to set balance and interest

```python
class Account:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        self.balance = balance

    def set_interest(self, interest):
        self.interest = interest
```
### cd_account.py

This file contains the `create_cd_account` function, which creates a CD account and calculates interest.

**Key features:**

Creates an instance of the Account class for a CD account
Calculates interest earned based on balance, interest rate, and term
Updates the account balance and sets the interest earned

```python
def create_cd_account(balance, interest_rate, months):
    cd_account = Account(balance, interest_rate)
    interest_earned = balance * (interest_rate * months/12)
    updated_balance = balance + interest_earned
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_earned)
    return updated_balance, interest_earned
```
### savings_account.py

This file contains the `create_savings_account` function, which is similar to the CD account function but for savings accounts.

**Key features:**

- Creates an instance of the Account class for a savings account
- Calculates interest earned based on balance, interest rate, and term
- Updates the account balance and sets the interest earned

```python
def create_savings_account(balance, interest_rate, months):
    savings_account = Account(balance, interest_rate)
    interest_earned = balance * (interest_rate * months/12)
    updated_balance = balance + interest_earned
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_earned)
    return updated_balance, interest_earned
```
### customer_banking.py

This is the main file that brings everything together and provides a user interface for the banking system.

**Key features:**

- Imports functions from other modules
- Implements input validation for user inputs
- Prompts user for account details
- Creates savings and CD accounts
- Displays account information and calculated interest

```python
def main():
    # ... (user input and function calls)
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    # ... (display results)

if __name__ == "__main__":
    main()
```

### 🚀 **Usage**

To use this banking system:

1. Ensure all files are in the same directory.
2. Run python customer_banking.py in your terminal.
3. Follow the prompts to enter account details.
4. View the calculated interest and updated balances for both savings and CD accounts.
