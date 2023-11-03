class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Initializes a bank account with an account number and optional initial balance.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits the given amount into the account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the given amount from the account if sufficient balance is available.
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def transfer(self, recipient_account, amount):
        """
        Transfers the given amount from this account to the recipient account.
        """
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.deposit(amount)
        else:
            print("Insufficient funds for transfer!")

    def check_balance(self):
        """
        Returns the current balance of the account.
        """
        return self.balance


class Bank:
    def __init__(self):
        """
        Initializes a bank with an empty list of accounts.
        """
        self.accounts = []

    def create_account(self, account_number, initial_balance=0):
        """
        Creates a new bank account and adds it to the bank's account list.
        """
        account = BankAccount(account_number, initial_balance)
        self.accounts.append(account)
        return account

    def find_account(self, account_number):
        """
        Finds and returns the bank account with the given account number.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None


# Sample usage of the banking system
if __name__ == "__main__":
    # Creating a bank
    bank = Bank()
    

    # Creating accounts
    account1 = bank.create_account(1001, 500)
    account2 = bank.create_account(1002, 1000)
    account3 = bank.create_account(1003, 1500)
    account4 = bank.create_account(1004, 2000)
    account5 = bank.create_account(1005, 2500)
    account6 = bank.create_account(1006, 3000)
    account7 = bank.create_account(1007, 3500)
    account8 = bank.create_account(1008, 4000)
    account9 = bank.create_account(1009, 4500)
    account10 = bank.create_account(1010, 5000)
    account11 = bank.create_account(1011, 5500)
    account12 = bank.create_account(1012, 6000)


    # Performing transactions
    account1.deposit(200)
    account2.withdraw(300)
    account1.transfer(account2, 100)
    account3.deposit(250)
    account4.withdraw(50)
    account5.withdraw(100)
    account6.deposit(75)
    account7.withdraw(200)
    account8.deposit(300)
    account9.withdraw(450)
    account10.deposit(500)
    account11.withdraw(340)
    account12.deposit(890)
            

    # Checking account balances
    print("Account 1001 Balance:", account1.check_balance())
    print("Account 1002 Balance:", account2.check_balance())
    print("Accoumt 1003 Balance:", account3.check_balance())
    print("Account 1004 Balance:", account4.check_balance())
    print("Account 1005 Balance:", account5.check_balance())
    print("Account 1006 Balance:", account6.check_balance())
    print("Account 1007 Balance:", account7.check_balance())
    print("Account 1008 Balance:", account8.check_balance())
    print("Account 1009 Balance:", account9.check_balance())
    print("Account 1010 Balance:", account10.check_balance())
    print("Account 1011 Balance:", account11.check_balance())
    print("Account 1012 Balance:", account12.check_balance())
