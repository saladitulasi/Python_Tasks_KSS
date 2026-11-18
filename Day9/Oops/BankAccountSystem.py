class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Number:", self.acc_no)
        print("Balance:", self.balance)


# Creating object
b1 = BankAccount(67543, 6000)

b1.deposit(3500)
b1.withdraw(2000)
b1.display()