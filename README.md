# 🏦 Banking System Project

## 📚 Table of Contents
- [Overview](#overview)
- [File Structure](#file-structure)
- [Detailed Explanation](#detailed-explanation)
  - [account.py](#accountpy)
  - [cd_account.py](#cd_accountpy)
  - [savings_account.py](#savings_accountpy)
  - [customer_banking.py](#customer_bankingpy)
- [Usage](#usage)
- [Contributing](#contributing)

## 🌟 Overview

This project implements a simple banking system that allows users to create and manage savings and CD (Certificate of Deposit) accounts. It demonstrates object-oriented programming principles and modular design in Python.

## 📂 File Structure
```python
banking_system/
│
├── account.py
├── cd_account.py
├── savings_account.py
└── customer_banking.py
```

## 🔍 Detailed Explanation

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
