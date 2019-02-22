class Account():
    def __init__(self):
        self.savings = 0
        self.transactions = []

    def deposit(self, v):
        self.savings += v
        self.transactions.append(['deposit', v])

    def withdraw(self, v):
        if self.savings - v >= 10000:
            self.savings -= v
            self.transactions.append(['withdraw', v])
            return 'Success'
        else:
            return 'Failure'


class ShortTermDeposit(Account):
    def __init__(self, r):
        super().__init__()
        self.rate = r

    def add_profit(self):
        self.savings *= (1 + self.rate / 100)

    def __str__(self):
        return 'Savings: {}, Withdrawable: {}'.format(self.savings, self.savings - 10000)

    def __le__(self, other):
        return self.savings <= other.savings

    def top_two(self):
        return self.transactions[-1:-3:-1]


a1 = Account()
a1.deposit(50000)
a1.withdraw(40000)
a1.deposit(100000)
s1 = ShortTermDeposit(10)
s1.deposit(10000)
s1.add_profit()
print(s1)

# print(a1)
# for x in a1.top_two():
#     print(x)

