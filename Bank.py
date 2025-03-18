from Money import Money
class Bank():
  def __init__(self):
    self.__bank = {int : list}
  def addMoney(self, money : Money) -> None:
    self.__bank[money.getNominal()].append(money)
  def withdrawMoney(self, nominal : int, count : int) -> list:
    callback = []
    for i in range(count):
      callback.append(self.__bank.pop(i))
    return callback
  def getNominals(self) -> list:
    return self.__bank.keys()
  def getCountOfMoney(self, nominal : int) -> int:
    if nominal in self.__bank:
      return len(self.__bank.keys())
    return 0

100 100 50 50 50 50 50 20 20 20 20 10 10  5 5 5 3 3 3 2 2  1 
431
100 100 50 50 50 50 20 10 1
