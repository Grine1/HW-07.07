class Book(object):

  def __init__(self, name: str, writer: str, category: str, price: float):
    self._name = name
    self._writer = writer
    self._category = category
    self._price = price

  def __str__(self):
    info = f'\n Назва {self._name}'
    info += f'\n Письменник {self._writer}'
    info += f'\n Жанр {self._category}'
    info += f'\n Ціна {self._price}'
    return info

  @property
  def name(self):
    return self._name

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, new_price: float):
    self._price = new_price
  