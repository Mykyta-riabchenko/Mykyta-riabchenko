class Money():
  def __init__(self, nominal : int):
    self._nominal = nominal
  def getNominal(self) -> int:
    return self._nominal
