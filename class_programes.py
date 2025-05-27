# bank withdrawal, deposit using class and instance method just below(example):



# class Bank:

#     def __init__(self, balance):
#         self.balance = balance

    
#     def withdrawal(self, amount):
#         self.balance -= amount
#         return self.balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    



# obj = Bank(5000)
# print(obj.balance)

# withdrawal_amt=obj.withdrawal(1000)
# print(withdrawal_amt)

# deposit_amt = obj.deposit(3000)
# print(deposit_amt)


# class method

# class Bank:
#     bank_name = "PNB"

#     @classmethod
#     def change_bank_name(cls, name):
#         cls.bank_name = name
#         return cls.bank_name
    

# output_one =Bank.bank_name
# print(output_one)

# output_two =Bank.change_bank_name("SBI")
# print(output_two)


# Static method

# class Mathutility:
#     @staticmethod
#     def add(a,b):
#         return a+b
    
#     @staticmethod
#     def even(num):
#         return num % 2 == 0
    
# print(Mathutility.add(4,4))
# print(Mathutility.even(8))

#  Class with Instance and Static Method Interaction

# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     # Instance method to perform transactions
#     def perform_transaction(self, amount, transaction_type):
#         if self.validate_transaction(amount, transaction_type):
#             if transaction_type == "deposit":
#                 self.balance += amount
#                 print(f"{amount} deposited. New Balance: {self.balance}")
#             elif transaction_type == "withdraw":
#                 self.balance -= amount
#                 print(f"{amount} withdrawn. New Balance: {self.balance}")
#             self.log_transaction(transaction_type, amount)
#         else:
#             print("Transaction failed due to validation error.")

#     # Static method to validate transaction
#     @staticmethod
#     def validate_transaction(amount, transaction_type):
#         if amount <= 0:
#             print("Invalid amount. Transaction amount should be greater than zero.")
#             return False
#         if transaction_type not in ["deposit", "withdraw"]:
#             print("Invalid transaction type. Choose 'deposit' or 'withdraw'.")
#             return False
#         return True

#     # Instance method to log transactions (called by static method)
#     def log_transaction(self, transaction_type, amount):
#         print(f"Transaction Log: {transaction_type.capitalize()} of {amount} by {self.account_holder}")

#     # Static method to display account details using instance
#     @staticmethod
#     def display_account_details(account):
#         print(f"Account Holder: {account.account_holder}, Balance: {account.balance}")

# # Create an account
# account = BankAccount("John Doe", 1000)

# # Perform transactions
# account.perform_transaction(500, "deposit")
# account.perform_transaction(300, "withdraw")
# account.perform_transaction(1500, "withdraw")  # Invalid due to insufficient balance

# # Static method accessing instance data
# BankAccount.display_account_details(account)


# class BankAccount:

#     def __init__(self, account_holder, balance = 0):

#         self.account_holder = account_holder
#         self.balance = balance


# class Statement(BankAccount):
    
#     def withdrawal(self, amount_with):
#         if self.balance >= amount_with:
#             Remaining_bal = self.balance - amount_with
#             print(Remaining_bal)
#             print(amount_with)
#         else:
#             print("Inefficient balance")

#     def deposit(self, amount_dep):
#         remaining_bal = self.balance + amount_dep
#         print(remaining_bal)
#         print(amount_dep)
    


# obj = Statement("Rahul", 5000)

# obj.withdrawal(1000)

# obj.deposit(2000)


# Diamond Problem(Multiple inheritence)



class Person:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def person_info(self):
        print(f"{self.name} and {self.age}")

class Employee:

    def __init__(self, emp_id):
        self.emp_id = emp_id

    def emp_info(self):
        print(f"{self.emp_id}")


class details(Person, Employee):

    def __init__(self, age, name, emp_id, team_name):
        Person.__init__(self, age, name)
        Employee.__init__(self, emp_id)
        self.team_name = team_name
    
    def details_info(self):
        self.person_info()
        self.emp_info()
        print(f"Team name {self.team_name}")


obj = details(12, 'Rao', 5678, 'FFF')

obj.details_info()


        
        




