class BankAccount:
    def __init__(self, intial_balance=0):
        self._account_balance = intial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be greater than 0.")    
        
    def withdraw(self,amount):
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                return True
            else:
                return False    
        else:
            print("Withdraw amount must be greater than 0.")
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")    