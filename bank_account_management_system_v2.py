class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля!")
        self.__balance += amount
        print(f"Баланс успешно пополнен на сумму: {amount}$")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля!")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на балансе для выполнения операции!")
        self.__balance -= amount
        print(f"Снятие средств на сумму: {amount}$")

    def get_balance(self):
        return self.__balance

    def _adjust_balance(self, delta):
        self.__balance += delta

    def show_balance(self):
        print(f"Текущий баланс: {self.__balance}$")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self._adjust_balance(interest)
        print(f"Начислены проценты на остаток по счету: {interest}$"
              f"\nОбновленный баланс: {self.get_balance()}$")


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля!")
        self._adjust_balance(-amount)
        print(f"Снятие на сумму {amount}$. Текущий баланс: {self.get_balance()}$")
        if self.get_balance() < 0:
            print(f"Ваш долг составляет: {-self.get_balance()}$")


user_operations = BankAccount("Artur")
user_operations.show_balance()
user_operations.deposit(500)
user_operations.show_balance()
user_operations.withdraw(100)
user_operations.show_balance()

user_interests = SavingsAccount(user_operations.owner, user_operations.get_balance())
user_interests.apply_interest()

user_checking = CheckingAccount(user_interests.owner, user_interests.get_balance())
user_checking.withdraw(500)

