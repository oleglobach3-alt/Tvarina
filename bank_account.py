class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" На рахунок {self.account_number} внесено {amount} грн. Поточний баланс: {self.balance} грн.")
        else:
            print(" Сума для внесення має бути більшою за 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print(" Сума для зняття має бути більшою за 0.")
        elif amount > self.balance:
            print(f" Недостатньо коштів. Поточний баланс: {self.balance} грн.")
        else:
            self.balance -= amount
            print(f" З рахунку {self.account_number} знято {amount} грн. Поточний баланс: {self.balance} грн.")

account = BankAccount("UA123456789", 500)
account.deposit(300)
account.withdraw(200)
account.withdraw(700)
