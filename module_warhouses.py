import json
from main import warehouse

class Warehouse:
    def add_warehouse(self):
        warehouse['ID'] = int(input('Введіть ID складу:').strip())
        warehouse['Назва складу'] = input('Введіть назву складу:').strip().title()
        warehouse['Місткість'] = float(input('Введіть максимальну місткість складу:').strip())
        warehouse['Товари'] = input('Введіть товари наявні на складі:').strip().split(',')

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
        delete_wareh = int(input('Введіть ID складу для видалення:').strip())
        if delete_wareh == warehouse['ID']:
            warehouse.clear()
        else:
            print('Складу за таким ID не знайдено.')

wareh1 = Warehouse()

def main():
    while True:
        print('Вітаю в застосунку!')
        print('------------------------')
        print('1 - Додати склад')
        print('2 - Оновити товари на складі')
        print('3 - Показати доступні товари')
        print('4 - Зберегти файл')
        print('5 - Завантажити файл')
        print('6 - Видалити склад')
        print('7 - Вихід з програми')
        print('------------------------')
        action = int(input('Виберіть дію:'))

        match action:
            case 1:
                wareh1.add_warehouse()
            case 2:
                wareh1.update_warehouse()
            case 3:
                wareh1.show_info()
            case 4:
                wareh1.save_json()
            case 5:
                wareh1.load_json()
            case 6:
                wareh1.delete_warehouse()
            case 7:
                print('Допобачення!')
                break
            case _:
                print('Невідома дія. Спробуйте, будь ласка ще раз.')
                continue

main()


