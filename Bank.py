from Money import Money
class Bank():
  def __init__(self):
    self.__bank = {int : list}
  def addMoney(self, money : Money) -> None:
    nominal = money.getNominal()
    if nominal not in self.__bank: 
      self.__bank[nominal] = []
    self.__bank[nominal].append(money)
  def withdrawMoney(self, nominal : int) -> list:
      self.__bank[nominal].pop()
  def getNominals(self) -> list:
    return self.__bank.keys()
  def getCountOfMoney(self, nominal : int) -> int:
    if nominal in self.__bank:
      return len(self.__bank[nominal])
    return 0
