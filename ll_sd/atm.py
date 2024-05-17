from abc import ABC, abstractmethod
from typing import Dict

class ATMState(ABC):
    """
    The base State class declares methods that all Concrete State classes
    should implement and provides a default implementation of a state
    transition method.
    """

    # @abstractmethod
    def insert_card(self, atm):
        pass

    # @abstractmethod
    def authenticate_pin(self, atm, pin):
        pass

    # @abstractmethod
    def select_transaction(self, atm, transaction_type):
        pass

    # Can be clubbed into 1
    # @abstractmethod
    def deposit_cash(self, atm, amount):
        pass

    # @abstractmethod
    def enter_withdrawal_amount(self, atm, amount):
        pass

    # @abstractmethod
    def display_balance(self, atm):
        pass

    # @abstractmethod
    def transact_again(self, atm):
        pass

    # @abstractmethod
    def exit(self, atm):
        pass

    # @abstractmethod
    def return_card(self, atm):
        pass

    def next_state(self, atm, state):
        atm.state = state

class NoCardState(ATMState):
    def insert_card(self, atm):
        print("NoCardState :: Card inserted")
        self.next_state(atm, AuthenticatePinState())

    # def return_card(self, atm):
    #     print("No card inserted")

class AuthenticatePinState(ATMState):
    # def insert_card(self, atm):
    #     print("AuthenticatePinState :: Card already inserted")

    def authenticate_pin(self, atm, pin):
        if pin == atm.pin:
            print("Pin authenticated")
            self.next_state(atm, SelectTransactionState())
        else:
            print("Invalid pin")
            self.next_state(atm, NoCardState())

    def exit(self, atm):
        print("Pin not authenticated")
        self.next_state(atm, NoCardState())

    def return_card(self, atm):
        print("Pin not authenticated")
        self.next_state(atm, NoCardState())

class SelectTransactionState(ATMState):
    # def insert_card(self, atm):
    #     print("SelectTransactionState :: Card already inserted")

    # def authenticate_pin(self, atm, pin):
    #     print("Pin already authenticated")

    def select_transaction(self, atm, transaction_type):
        if transaction_type == "deposit":
            self.next_state(atm, DepositCashState())
        elif transaction_type == "withdrawal":
            self.next_state(atm, WithdrawalState())
        elif transaction_type == "balance":
            self.display_balance(atm)
            self.exit(atm)
        else:
            print("Invalid transaction type")

    # def deposit_cash(self, atm, amount):
    #     print("Transaction not selected")

    # def enter_withdrawal_amount(self, atm, amount):
    #     print("Transaction not selected")

    def display_balance(self, atm):
        print(f"Current balance: ${atm.balance}")

    def transact_again(self, atm):
        choice = input("Would you like to perform another transaction? (y/n): ").lower()
        if choice == "y":
            self.next_state(atm, SelectTransactionState())
        else:
            self.exit(atm)

    def exit(self, atm):
        print("Exiting...")
        self.next_state(atm, NoCardState())

    def return_card(self, atm):
        print("Returning card")
        self.next_state(atm, NoCardState())

class DepositCashState(ATMState):
    # def insert_card(self, atm):
    #     print("DepositCashState :: Card already inserted")

    # def authenticate_pin(self, atm, pin):
    #     print("Pin already authenticated")

    # def select_transaction(self, atm, transaction_type):
    #     print("Transaction already selected")

    def deposit_cash(self, atm, amount):
        if amount > 0:
            atm.balance += amount
            print(f"Deposited ${amount}. New balance: ${atm.balance}")
            self.transact_again(atm)
        else:
            print("Invalid deposit amount")
            self.transact_again(atm)

    # def enter_withdrawal_amount(self, atm, amount):
    #     print("Deposit transaction in progress")

    # def display_balance(self, atm):
    #     print("Deposit transaction in progress")

    def transact_again(self, atm):
        choice = input("Would you like to perform another transaction? (y/n): ").lower()
        if choice == "y":
            self.next_state(atm, SelectTransactionState())
        else:
            self.exit(atm)

    def exit(self, atm):
        print("Exiting...")
        self.next_state(atm, NoCardState())

    def return_card(self, atm):
        print("Returning card")
        self.next_state(atm, NoCardState())

class WithdrawalState(ATMState):
    # def insert_card(self, atm):
    #     print("WithdrawalState :: Card already inserted")

    # def authenticate_pin(self, atm, pin):
    #     print("Pin already authenticated")

    # def select_transaction(self, atm, transaction_type):
    #     print("Transaction already selected")

    # def deposit_cash(self, atm, amount):
    #     print("Withdrawal transaction in progress")

    def enter_withdrawal_amount(self, atm, amount):
        if amount > 0 and amount <= atm.balance:
            atm.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${atm.balance}")
            self.transact_again(atm)
        else:
            print("Invalid withdrawal amount or insufficient balance")
            self.transact_again(atm)

    def display_balance(self, atm):
        print("Withdrawal transaction in progress")

    def transact_again(self, atm):
        choice = input("Would you like to perform another transaction? (y/n): ").lower()
        if choice == "y":
            self.next_state(atm, SelectTransactionState())
        else:
            self.exit(atm)

    def exit(self, atm):
        print("Exiting...")
        self.next_state(atm, NoCardState())

    def return_card(self, atm):
        print("Returning card")
        self.next_state(atm, NoCardState())

class ATM:
    def __init__(self, pin: int, balance: int):
        self.pin = pin
        self.balance = balance
        self.state = NoCardState()

    def insert_card(self):
        self.state.insert_card(self)

    def authenticate_pin(self, pin):
        self.state.authenticate_pin(self, pin)

    def select_transaction(self, transaction_type):
        self.state.select_transaction(self, transaction_type)

    def deposit_cash(self, amount):
        self.state.deposit_cash(self, amount)

    def enter_withdrawal_amount(self, amount):
        self.state.enter_withdrawal_amount(self, amount)

    def display_balance(self):
        self.state.display_balance(self)

    def transact_again(self):
        self.state.transact_again(self)

    def exit(self):
        self.state.exit(self)

    def return_card(self):
        self.state.return_card(self)

# Usage example
if __name__ == "__main__":
   atm = ATM(pin=1234, balance=1000)

   # Insert card
   atm.insert_card()

   # Authenticate PIN
   atm.authenticate_pin(1234)  # Correct PIN
   atm.authenticate_pin(4321)  # Incorrect PIN

   # Select transaction
   atm.select_transaction("balance")

   atm.insert_card()
   atm.authenticate_pin(1234)
   atm.select_transaction("deposit")
   # Deposit cash
   atm.deposit_cash(500)

   atm.select_transaction("deposit")
   atm.deposit_cash(-100)  # Invalid deposit amount

   # Select transaction again
   atm.select_transaction("withdrawal")
   atm.enter_withdrawal_amount(300)

   atm.select_transaction("withdrawal")
   atm.enter_withdrawal_amount(1500)  # Insufficient balance

#   # Display balance
#   atm.display_balance()

#   # Transact again
#   atm.transact_again()  # Select 'n'

   # Exit
   atm.exit()

   # Return card
   atm.return_card()
