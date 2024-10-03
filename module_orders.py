import json
from main import orders, tovar
from module_clients import client1

class Order:
    def add_order(self):
        orders['Номер'] = int(input('Введіть номер замовлення'))
        orders['Список товарів'] = tovar
        orders['Клієнт'] = client1.list_clinets()
        orders['Загальна сума'] = sum(tovar['Ціна'])
        orders['Статус'] = input('Введіть статус замовлення:').title().strip()

    def update_order(self):
        updated_order = int(input('Введіть номер замовлення для оновлення інформації:').strip())
        if updated_order == orders['Номер']:
            orders['Номер'] = int(input('Введіть новий номер:').strip())
        elif updated_order == orders['Список товарів']:
            orders['Список товарів'] = int(input('Введіть новий ID товару:').strip())
        elif updated_order == orders['Клієнт']:
            pass
        elif updated_order == orders['Статус']:
            orders['Статус'] = input('Введіть новий статус:').title().strip()
        else:
            print('Заданого номеру не знайдено.')

    def delete_order(self):
        del_order = int(input('Введіть номер товару для видалення:'))
        try:
            if del_order == orders['Номер']:
                orders.clear()
        except:
            ValueError('Невідомий номер замовлення')

    def find_order(self):
        num_order = int(input('Введіть номер замовлення:'))
        if num_order == orders['Номер']:
            print(f'Знайдені замовлення:{orders}')
        else:
            print('Замовлення за таким номером не знайдено.')


    def write_json(self):
        with open('orders.json', 'w', encoding='utf-8') as file:
            json.dump(orders, file, ensure_ascii=False, indent=4)

    def read_json(self):
        try:
            with open('orders.json', 'r') as f:
                order_load = json.load(f)
                json.loads(order_load)
                return order_load
        except FileNotFoundError:
            print('Файл з таким іменем не знайдено.')

order1 = Order()

def main():
    while True:
        print('Вітаю в застосунку!')
        print('------------------------')
        print('1 - Створити замовлення')
        print('2 - Редагувати замовлення')
        print('3 - Видалити замовлення')
        print('4 - Знайти замовлення за номером')
        print('5 - Зберегти файл')
        print('6 - Завантажити файл')
        print('7 - Створені замовлення')
        print('8 - Вихід з програми')
        print('------------------------')
        action = int(input('Оберіть дію:'))
        if action == 1:
            order1.add_order()
        elif action == 2:
            order1.update_order()
        elif action == 3:
            order1.delete_order()
        elif action == 4:
            order1.find_order()
        elif action == 5:
            order1.write_json()
        elif action == 6:
            order1.read_json()
        elif action == 7:
            if orders is not None:
                print(orders)
                print(order1.read_json())
        elif action == 8:
            print('Побачимось наступний раз!')
            break


main()

