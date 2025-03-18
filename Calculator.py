import Bank

class Calculator():

  def __count(self, list):
    sum = 0
    for i in list:
      sum += i
    return sum

  def exchangeMoney(self, inputedMoney: list, bank: Bank):
    changedMoney = []
    inputedSum = self.__count(inputedMoney)
    for i in bank.getNominals():
      while  bank.getCountOfMoney(i) <= inputedSum:
        changedMoney =+ i 
        inputedSum =- i
    return changedMoney
