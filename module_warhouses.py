import json

from main import warehouse

class Warehouse:
    def add_warehouse(self):
        warehouse['ID'] = int(input('Введіть ID складу:'))
        warehouse['Назва складу'] = input('Введіть назву складу:')
        warehouse['Місткість'] = float(input('Введіть максимальну місткість складу:'))
        warehouse['Товари'] = input('Введіть товари наявні на складі:')

    def update_warehouse(self):
        sklad = int(input('Введіть ID складу:'))
        if sklad == warehouse['ID']:
            warehouse['Товари'] = input('Введіть товари, розділені комою').strip().split(',')
        else:
            print('Складу за таким ID не знайдено.')

    def show_info(self):
        print(f'Доступні товари: {warehouse['Товари']}')

    def save_json(self):
        with open('warehouse.json', 'w', encoding='utf-8') as war:
            json.dump(warehouse, war, ensure_ascii=False, indent=4)

    def load_json(self):
        try:
            with open('warehouse.json','r',encoding='utf-8') as war1:
                wareh = json.load(war1)
                json.load(wareh)
                return wareh
        except FileNotFoundError:
            print('Файл з даними не знайдено.')

    def delete_warehouse(self):
        delete_wareh = int(input('Введіть ID складу для видалення:'))
        if delete_wareh == warehouse['ID']:
            warehouse.clear()
        else:
            print('Складу за таким ID не знайдено.')

