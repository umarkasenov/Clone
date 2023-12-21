class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount
        print(f"Текущий баланс: {self._balance}")

    def _reset_balance(self):
        self._balance = 0
        print("Баланс обнулен")

    def _jackpot(self):
        self._balance *= 10
        print("У вас джекпот! Новый баланс:", self._balance)

    def _combine_balance(self, other_bank):
        self._balance += other_bank._balance
        print(f"Баланс объединен. Новый баланс: {self._balance}")

bank1 = Bank("Клиент 1", 100)
bank2 = Bank("Клиент 2", 100)

bank1.moneyX()
bank1._jackpot()
bank2._combine_balance(bank1)

bank1._reset_balance()
print(f"Баланс после обнуления: {bank1._balance}")