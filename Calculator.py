from Bank import Bank
class Calculator():
  
  def _bankSize(self, bank: Bank):
     bankSize = sum(bank.getCountOfMoney(n) * n for n in bank.getNominals() if isinstance(n, int))
     return bankSize
  
  def exchangeMoney(self, inputedMoney: list, bank: Bank):
    changedMoney = []
    inputedSum = sum(inputedMoney)
    if inputedSum > self._bankSize(bank):
      return -1             #if given sum is larger then amount of money in the bank: return -1
    for i in [100, 50,20,10,5,2,1]:
        
      while  i <= inputedSum and bank.getCountOfMoney(i) != 0:
        changedMoney.append(i) 
        inputedSum -= i
        bank.withdrawMoney(i)
    return changedMoney
 
     #TODO:if give 100 it has to return smaller money
     #TODO:if the amount of needed coins is not enought the prog's ignoring it
          #example bank[1, 5, 5, 10] givenList[1, 1, 5, 10]




