from model.book import Book

class Library(object):

  def __init__(self):
    self._book = []

  def add_book(self, new_book: Book):
    self._book.append(new_book)

  def display_book(self):
    if len(self._book) == 0:
      print('Немає товарів в бібліотеці')
    else:
      for b in self._book:
        print(b)

  def change_book(self, name: str, price: float):
    for b in self._book:
      if b.name == name:
        b.price = price


  def del_book(self, name: str):
    for b in self._book:
      if b.name == name:
        self._book.remove(b)

