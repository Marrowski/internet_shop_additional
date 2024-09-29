from main import orders, client
from module_products import tovar

class Order:
    def add_order(self):
        orders['Номер'] = int(input('Введіть номер замовлення'))
        orders['Список товарів'] = tovar
        orders['Клієнт'] = client
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

order1 = Order()

def main():
    while True:
        print('Вітаю в застосунку')
        print('------------------------')
        print('1 - Створити замовлення')
        print('2 - Редагувати замовлення')
        print('3 - Видалити замовлення')
        print('4 - Знайти замовлення за номером')
        print('5 - Завершити роботу')
        print('------------------------')
        action = int(input('Оберіть дію:'))
        if action == 1:
            order1.add_order()
        elif action == 2:
            order1.update_order()
        elif action == 3:
            del_order = int(input('Введіть номер товару для видалення:'))
            try:
                if del_order == orders['Номер']:
                    orders.clear()
            except:
                ValueError('Невідомий номер замовлення')

        elif action == 4:
            num_order = int(input('Введіть номер замовлення:'))
            if num_order == orders['Номер']:
                print(f'Знайдені замовлення:{orders}')
            else:
                print('Замовлення за таким номером не знайдено.')
                continue
        elif action == 5:
            print('Допобачення!')
            break


main()

