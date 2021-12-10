from model.book import Book
from model.library import Library

if __name__ == '__main__':
  
  lib = Library()
  lib.add_book(Book('Божествина комедія', 'Альгельері Данте', 'Поема', 150))
  lib.add_book(Book('Кобзар', 'Тарас Григорович Шевченко', 'Збірник віршів', 200))
  lib.add_book(Book('Війна і мир', 'Л. Толстой', 'Історичний', 250))
  lib.add_book(Book('Алхімік', 'Пауло Куельйо', 'Роман', 115))
  lib.display_book()

  lib.change_book('Кобзар', 300)
  
  lib.del_book('Алхімік')
  lib.display_book()
