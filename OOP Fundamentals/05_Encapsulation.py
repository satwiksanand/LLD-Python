# encapsulation is the first principle of the four pillars of OOP
# The practice of bundling data and the specific actions that operate on that data into a single unit,
# while simultaneously restricting direct external access to the internal state. It acts as a protective
# shield to prevent unauthorized or accidental modifications.

# a bank account example, where u are not allowed to directly manipulate balance

class BankAccount:
    __balance: float

    def __init__(self, initial_balance: float):
        self.__balance = initial_balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("deposit amount cannot be negative")
        self.__balance += amount
        print(f"current balance: {self.__balance}")

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("withdraw amount cannot be negative")
        elif amount > self.__balance:
            raise ValueError("withdraw amount cannot be greater than current balance")
        else:
            self.__balance -= amount

        print(f"current balance: {self.__balance}")

    @property
    def balance(self):
        return self.__balance

    def print_balance(self):
        print(f"current balance: {self.balance}")


if __name__ == "__main__":
    account = BankAccount(100)
    account.print_balance()
    account.deposit(100)
    account.print_balance()
    # trying to deposit negative amount
    try:
        account.deposit(-12.23)
    except ValueError as e:
        print(e)

    account.withdraw(23.23)
    account.print_balance()
    try:
        account.withdraw(-12.23)
    except ValueError as e:
        print(e)

    account.print_balance()
    try:
        account.withdraw(3000)
    except ValueError as e:
        print(e)