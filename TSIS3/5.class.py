class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("\nEnter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance ")

    def display(self):
        print("\nNet Available Balance=", self.balance)


s = BankAccount()

s.deposit()
s.withdraw()
s.display()
