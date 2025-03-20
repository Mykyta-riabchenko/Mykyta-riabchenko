from Bank import Bank
from Calculator import Calculator
bank = Bank()
calculator = Calculator()


bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(1)
bank.addMoney(5)
bank.addMoney(10)
bank.addMoney(10)
bank.addMoney(20)


givenList = [5, 5, 10]
result = calculator.exchangeMoney(givenList, bank)

print("Exchanged money:", result)



  
