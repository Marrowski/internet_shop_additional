from main import tovar
import json

class Product:
    def add_tovar(self):
        tovar['ID'] = input('Введіть ID товару:')
        tovar['Назва'] = input('Введіть назву товару:')
        tovar['Категорія'] = input('Введіть категорію:')
        tovar['Ціна'] = input('Введіть ціну:')
        tovar['Кількість на складі'] = input('Введіть кількість на складі:')
        tovar['Опис'] = input('Введіть опис:')

    def change_tovar(self):
        tovar['ID'].append(int(input('Введіть ID товару:')))
        tovar['Назва'].append(input('Введіть назву товару').title().strip())
        tovar['Категорія'].append(input('Введіть категорію товару').title().strip())
        tovar['Ціна'].append(float('Введіть ціну товару')).strip()
        tovar['Кількість на складі'].append(int(input('Введіть кількість товару').strip()))
        tovar['Опис'].append(input('Введіть опис товару').title().strip())


prod1 = Product()

def main():
    while True:
        print('1 - Додати товар')
        print('2 - Видалити товар')
        print('3 - Змінити товар')
        print('4 - Знайти товар')
        print('5 - Зберегти товари')
        print('6 - Завантажити товари')
        print('7 - Продивитися товари')
        print('8 - Вийти із програми')
        print('------------------------')
        oper = int(input('Вітаю, виберіть операцію:'))
        if oper == 1:
            prod1.add_tovar()

        elif oper == 2:
            delete_tovar = input('Введіть ключ товару для видалення:')
            if delete_tovar == 'ID'.upper():
                del tovar['ID']
            elif delete_tovar == 'Назва'.title():
                del tovar['Назва']
            elif delete_tovar == 'Категорія'.title():
                del tovar['Категорія']
            elif delete_tovar == 'Ціна'.title():
                del tovar['Ціна']
            elif delete_tovar == 'Кількість'.title():
                del tovar['Кількість на складі']
            elif delete_tovar == 'Опис'.title():
                del tovar['Опис']
            else:
                raise ValueError('Невідоме значення.')

        elif oper == 3:
            prod1.change_tovar()

        elif oper == 4:
            search_tov = tovar[input('Введіть категорію товару:')]
            try:
                if search_tov == tovar['Категорія'] == 'Комп`ютерна техніка'.title():
                    print(f'За співпадінням знайдено(і): {tovar['Категорія']}')
            except ValueError:
                print('Не знайдено товарів за такою категорією.')
            else:
                print('Товарів не знайдено.')
        elif oper == 5:
            with open('tovar.json', 'w') as file:
                json.dump(tovar, ensure_ascii=False, indent=4)
        elif oper == 6:
            with open('tovar.json', 'r') as f:
                json.load(f)

        elif oper == 7:
            print(tovar)
        elif oper == 8:
            print('До зустрічі!')
            break
        else:
            print('Невідома дія. Спробуй ще раз.')
            continue

main()

