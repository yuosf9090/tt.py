from abc import ABC, abstractmethod

class ATM:
    def __init__(self):
        self.__accounts = {}    # Making accounts private

    def create_account(self, owner, account_type, balance=0):
        if account_type == "savings":
            self.__accounts[owner] = SavingsAccount(owner, balance)
        elif account_type == "checking":
            self.__accounts[owner] = CheckingAccount(owner, balance)
        else:
            print("Invalid account type.")

    def deposit(self, owner, amount):
        if owner in self.__accounts:
            self.__accounts[owner].deposit(amount)
        else:
            print("Account does not exist.")

    def withdraw(self, owner, amount):
        if owner in self.__accounts:
            self.__accounts[owner].withdraw(amount)
        else:
            print("Account does not exist.")

    def check_balance(self, owner):
        if owner in self.__accounts:
            self.__accounts[owner].check_balance()
        else:
            print("Account does not exist.")


class Account(ABC):
    def __init__(self, owner, balance=0):
        self.__owner = owner  # Making owner private
        self.__balance = balance  # Making balance private

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.__interest_rate = interest_rate  # Making interest rate private

    def deposit(self, amount):
        if amount > 0:
            self._Account__balance += amount
            print(f"{amount} deposited. Current balance: {self._Account__balance}.")
        else:
            print("Please enter a valid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._Account__balance:
            self._Account__balance -= amount
            print(f"{amount} withdrawn. Current balance: {self._Account__balance}.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance for account {self._Account__owner}: {self._Account__balance}.")

    def add_interest(self):
        interest = self._Account__balance * self.__interest_rate
        self._Account__balance += interest
        print(f"Interest of {interest:.2f} added. Current balance: {self._Account__balance:.2f}.")


class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=1000):
        super().__init__(owner, balance)
        self.__overdraft_limit = overdraft_limit  # Making overdraft limit private

    def deposit(self, amount):
        if amount > 0:
            self._Account__balance += amount
            print(f"{amount} deposited. Current balance: {self._Account__balance}.")
        else:
            print("Please enter a valid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= (self._Account__balance + self.__overdraft_limit):
            self._Account__balance -= amount
            print(f"{amount} withdrawn. Current balance: {self._Account__balance}.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance for account {self._Account__owner}: {self._Account__balance}.")


def main():
    atm = ATM()
    while True:
        print("\nChoose an operation:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '1':
            owner = input("Enter account owner's name: ")
            account_type = input("Enter account type (savings/checking): ")
            balance = float(input("Enter starting balance: "))
            atm.create_account(owner, account_type, balance)
        elif choice == '2':
            owner = input("Enter account owner's name: ")
            amount = float(input("Enter deposit amount: "))
            atm.deposit(owner, amount)
        elif choice == '3':
            owner = input("Enter account owner's name: ")
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(owner, amount)
        elif choice == '4':
            owner = input("Enter account owner's name: ")
            atm.check_balance(owner)
        elif choice == '5':
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





