class Account(object):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        print("Deposit Accepted")

    def withdraw(self, withdraw):
        if withdraw <= self.balance:
            self.balance -= withdraw
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")


    def __str__(self):
        return "Account owner:   %s \nAccount balance: $%s " %(self.owner, self.balance)
