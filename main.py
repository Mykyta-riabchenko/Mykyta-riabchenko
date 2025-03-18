import Bank, Money
bank = Bank()
while 1:
  cin = input("Input > ")
  if(cin.isdigit()):
    bank.addMoney(Money(int(cin)))
