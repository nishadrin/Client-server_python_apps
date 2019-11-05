# Задание на закрепление знаний по модулю json. Есть файл orders в
# формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
# его заполнение данными.
import json
import os

def write_order_to_json(item, quantity, price, buyer, date):
    json_path = os.path.abspath('orders.json')
    items = {
        'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer,
        'date': date
        }
    with open(json_path, 'w') as file:
        json.dump(items, file, indent=4)

if __name__ == '__main__':
    item = 2
    quantity = 2
    price = 350
    buyer = 'Vasya'
    date = '5 января 2020'
    write_order_to_json(item, quantity, price, buyer, date)
