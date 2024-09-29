from main import tovar
import json

class Product:
    def add_tovar(self):
        tovar['ID'] = int(input('Введіть ID товару:').upper())
        tovar['Назва'] = input('Введіть назву товару:').title().strip()
        tovar['Категорія'] = input('Введіть категорію:').title().strip()
        tovar['Ціна'] = float(input('Введіть ціну:').strip())
        tovar['Кількість на складі'] = int(input('Введіть кількість на складі:').strip())
        tovar['Опис'] = input('Введіть опис:').title().strip()

    def change_tovar(self):
        update_tovar = input('Введіть ключ товару, який би ви хотіли оновити:')
        if update_tovar == 'ID'.upper():
            tovar['ID'] = int(input('Введіть новий ID:'))
        elif update_tovar == 'Назва'.title():
            tovar['Назва'] = input('Введіть нову назву товару:').title().strip()
        elif update_tovar == 'Категорія'.title():
            tovar['Категорія'] = input('Введіть нову категорію товару:').title().strip()
        elif update_tovar == 'Ціна'.title():
            tovar['Ціна'] = float(input('Введіть нову ціну товару:'))
        elif update_tovar == 'Кількість'.title().strip():
            tovar['Кількість на складі'] = input('Введіть кількість товару на складі:')
        elif update_tovar == 'Опис'.title().strip():
            tovar['Опис'] = input('Оновіть опис товару:').title().strip()

prod1 = Product()

def main():
    while True:
        print('Вітаю у системі!')
        print('------------------------')
        print('1 - Додати товар')
        print('2 - Видалити товар')
        print('3 - Змінити товар')
        print('4 - Зберегти товари')
        print('5 - Завантажити товари')
        print('6 - Продивитися товари')
        print('7 - Вийти із програми')
        print('------------------------')

        oper = int(input('Виберіть операцію:'))
        if oper == 1:
            prod1.add_tovar()

        elif oper == 2:
            print(f'Наявні товари: {tovar}')
            delete_tovar = int(input('Введіть ID товару для видалення:'))
            if delete_tovar == tovar['ID']:
                tovar.clear()
        elif oper == 3:
            prod1.change_tovar()
        elif oper == 4:
            with open('tovar.json', 'w', encoding='cp1251') as file:
                file.write(str(tovar))
        elif oper == 5:
            with open('tovar.json', 'r') as f:
                json.load(f)
        elif oper == 6:
            print(tovar)
        elif oper == 7:
            print('До зустрічі!')
            break
        else:
            print('Невідома дія. Спробуй ще раз.')
            continue

main()

