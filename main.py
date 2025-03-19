from Bank import Bank
from Calculator import Calculator
from Money import Money
bank = Bank()
calculator = Calculator()

bank.addMoney(Money(1))
bank.addMoney(Money(5))
bank.addMoney(Money(5))
bank.addMoney(Money(10))


givenList = [1, 1, 5, 10]
result = calculator.exchangeMoney(givenList, bank)

print("Exchanged money:", result)
