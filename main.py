import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale 

DSN  ='postgresql://postgres:postgres@localhost:5432/Test_shop'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

#publisher = [Publisher(name = 'Пушкин'), Publisher(name = 'Толстой'), Publisher(name = 'Булгаков')] 
#book = [Book(title = 'Капитанская дочка', id_publisher = 1), Book(title = 'Руслан и Людмила', id_publisher = 1), Book(title = 'Евгений Онегин', id_publisher = 1), 
#        Book(title = 'Война и мир', id_publisher = 2), Book(title = 'Анна Каренина', id_publisher = 2), 
#        Book(title = 'Мастер и Маргарита', id_publisher = 3), Book(title = 'Собачье сердце', id_publisher = 3)]
#shop = [Shop(name = 'Буквоед'), Shop(name = 'Лабиринт'), Shop(name = 'Книжный дом')]
#stock = [Stock(id_book = 1, id_shop = 1, count = 10), Stock(id_book = 2, id_shop = 1, count = 5), Stock(id_book = 3, id_shop = 2, count = 10),
#         Stock(id_book = 4, id_shop = 3, count = 3), Stock(id_book = 5, id_shop = 1, count = 5), Stock(id_book = 6, id_shop = 3, count = 10),
#         Stock(id_book = 6, id_shop = 1, count = 5), Stock(id_book = 7, id_shop = 3, count = 2), Stock(id_book = 2, id_shop = 3, count = 5)]
#sale = [Sale(id_stock = 1, price = 500.5, date_sale = '2023-04-20', count = 2), Sale(id_stock = 3, price = 700, date_sale = '2023-04-21', count = 1), Sale(id_stock = 5, price = 1000, date_sale = '2023-04-23', count = 1),
#        Sale(id_stock = 4, price = 1500, date_sale = '2023-04-25', count = 1), Sale(id_stock = 6, price = 950, date_sale = '2023-04-25', count = 1), Sale(id_stock = 7, price = 650, date_sale = '2023-04-23', count = 1)] 

#session.add_all(publisher)
#session.commit()
#session.add_all(book)
#session.commit()
#session.add_all(shop)
#session.commit()
#session.add_all(stock)
#session.commit()
#session.add_all(sale)
#session.commit()

name_id_publisher = input('Введите id или имя автора:')

sale_list = session.query(
         Sale, Stock, Shop, Book, Publisher
    ).filter(
         Sale.id_stock == Stock.id,
    ).filter(
         Stock.id_shop == Shop.id,
    ).filter(
         Stock.id_book == Book.id,
    ).filter(
         Book.id_publisher == Publisher.id,
    ).filter(
        Publisher.name == name_id_publisher or Publisher.id == name_id_publisher,
    ).all()

for s in sale_list:
    print(f'{s.Book.title} | {s.Shop.name} | {s.Sale.price} | {s.Sale.date_sale}')

session.close()
