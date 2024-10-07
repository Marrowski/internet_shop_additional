from module_clients import client1

def generate_report():
    with open()

def generate_orders()

def main():
    while True:
        print('Вітаю у системі.')
        print('------------------------')
        print('1 - Сгенерувати звіт про найпопулярніші товари')
        print('2 - Згенерувати звіт про загальну кількість замовлень')
        print('3 - Вийти з програми')
        print('------------------------')

        action = int(input('Виберіть дію:'))
        match action:
            case 1:
                generate_report()
            case 2:
                generate_orders()
            case 3:
                print('Допобачення!')
                break
            case _:
                print('Невідома дія, спробуйте ще раз.')
                continue