class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0: raise ValueError("Deposit must be positive.")
        self.balance += amount
        print(f"Deposited GHS{amount:.2f}. Balance: GHS{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0: raise ValueError("Withdrawal must be positive.")
        if amount > self.balance: raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew GHS{amount:.2f}. Balance: GHS{self.balance:.2f}")

    def check_balance(self):
        print(f"Balance: GH₵{self.balance:.2f}")
        return self.balance

if __name__ == "__main__":
    acc = BankAccount(100)
    acc.deposit(50)
    try: acc.withdraw(200)
    except InsufficientFundsError as e: print(e)
