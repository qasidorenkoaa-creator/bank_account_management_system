class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Баланс успешно пополнен на сумму: {amount}$")
        else:
            raise ValueError("Неправильное значение!")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Снятие средств на сумму: {amount}$")
        else:
            raise ValueError("Недостаточно средств на балансе для выполнения операции!")

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def show_balance(self):
        print(f"Текущий баланс: {self.__balance}$")


class SavingsAccount(BankAccount):
    def __init__(self, bank_account, interest_rate=0.05):
        super().__init__(bank_account.owner, bank_account.get_balance())
        self.bank_account = bank_account
        self.interest_rate = interest_rate

    def apply_interest(self):
        current_balance = self.bank_account.get_balance()
        receiving_interest = current_balance * self.interest_rate
        new_balance = current_balance + receiving_interest
        self.bank_account.set_balance(new_balance)
        print(f"Начислены проценты на остаток по счету: {receiving_interest}$"
              f"\nОбновленный баланс: {self.bank_account.get_balance()}$")

    def get_saving_balance(self):
        return self.bank_account.get_balance()


class CheckingAccount(BankAccount):
    def __init__(self, bank_account, savings_account):
        super().__init__(bank_account.owner, savings_account.get_saving_balance())
        self.savings_account = savings_account

    def withdraw(self, amount):
        current_balance = self.savings_account.get_saving_balance()
        if current_balance < amount:
            debt = amount - current_balance
            print(f"Снятие на сумму {amount}$, превышающую баланс, ваш долг составляет: {debt}$")
        else:
            new_balance = current_balance - amount
            self.savings_account.bank_account.set_balance(new_balance)
            print(f"Снятие средств на сумму: {amount}$\nТекущий баланс: {self.savings_account.get_saving_balance()}$")


user_operations = BankAccount("Artur")
user_operations.show_balance()
user_operations.deposit(500)
user_operations.show_balance()
user_operations.withdraw(100)
user_operations.show_balance()

user_interests = SavingsAccount(user_operations)
user_interests.apply_interest()

user_checking = CheckingAccount(user_operations, user_interests)
user_checking.withdraw(500)
