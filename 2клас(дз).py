import random

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def __str__(self):
        return f"{self.account_number}: {self.balance:.2f} грн"


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_account(self, number, balance=0):
        acc = BankAccount(number, balance)
        self.accounts.append(acc)

    def total_balance(self):
        return sum(a.balance for a in self.accounts)

    def random_action(self):
        if not self.accounts:
            return
        acc = random.choice(self.accounts)
        action = random.choice(["deposit", "withdraw"])
        amount = random.randint(50, 300)
        if action == "deposit":
            acc.deposit(amount)
            print(f"{self.name} вніс {amount} грн на {acc.account_number}")
        else:
            acc.withdraw(amount)
            print(f"{self.name} зняв {amount} грн з {acc.account_number}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def simulate(self, days):
        for day in range(1, days + 1):
            print(f"\nДень {day}")
            for c in self.customers:
                c.random_action()
            for c in self.customers:
                print(f"{c.name} має {c.total_balance():.2f} грн")


if __name__ == "__main__":
    random.seed(1)
    bank = Bank("MyBank")

    c1 = Customer("Олег")
    c1.open_account("UA001", 500)

    c2 = Customer("Андрій")
    c2.open_account("UA002", 300)

    bank.add_customer(c1)
    bank.add_customer(c2)

    bank.simulate(5)
