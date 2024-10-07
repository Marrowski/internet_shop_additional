from main import client, orders
import json



class Client:
    def register_client(self):
         client['ID'] = int(input('Введіть ID :').strip())
         client['Ім`я'] = input('Введіть ваше ім`я:').title().strip()
         client['Електронна пошта'] = input('Введіть ваш email:').strip()
         client['Телефон'] = int(input('Введіть номер телефону в форматі(380):').strip())
         client['Адреса'] = input('Введіть адресу:').title().strip()
         client['Історія замовлень'] = orders

    def edit_client(self):
        red_client = int(input('Введіть ключ клієнта, якого ви хотіли би відредагувати:'))
        if red_client == client['Ім`я']:
            client['Ім`я'] = input('Введіть нове ім`я:').title().strip()
        elif red_client == client['Електронна пошта']:
            client['Електронна пошта'] = input('Введіть нову електронну пошту:').strip()
        elif red_client == client['Телефон']:
            client['Телефон'] = int(input('Введіть номер телефону у форматі(380):').strip())
        elif red_client == client['Адреса']:
            client['Адреса'] = input('Введіть нову адресу:').title().strip()
        else:
            print('Невідомий ключ. Спробуйте ще раз.')

    def list_clinets(self):
        if client is not None:
            print(client)
            print(Client.load_json(self))
        else:
            print('Наразі список пустий.')


    def delete_client(self):
        del_client = int(input('Введіть ID клієнта для видалення:').strip())
        if del_client == client['ID']:
            client.clear()
        else:
            print('Клієнта з таким ID не знайдено.')

    def save_json(self):
        with open('clients.json', 'w', encoding='utf-8') as new_client:
            json.dump(client, new_client, ensure_ascii=False, indent=4)

    def load_json(self):
        try:
            with open('clients.json', 'r') as new_client:
                clients_json = new_client.read()
                json.loads(clients_json)
                return clients_json
        except FileNotFoundError:
            print('Файл з даними не знайдено.')


client1 = Client()

def main():
    while True:
        print('Вітаю!')
        print('------------------------')
        print('1 - Створити нового клієнта.')
        print('2 - Змінити інформацію проо клієнта')
        print('3 - Переглянути клієнтів')
        print('4 - Видалити клієнта')
        print('5 - Зберегти інформацію')
        print('6 - Завантажити інформацію')
        print('7 - Вихід з програми')
        print('------------------------')
        action = int(input('Що би ви хотіли зробити:'))
        if action == 1:
            client1.register_client()
        elif action == 2:
            client1.edit_client()
        elif action == 3:
            client1.list_clinets()
        elif action == 4:
            client1.delete_client()
        elif action == 5:
            client1.save_json()
        elif action == 6:
            client1.load_json()
        elif action == 7:
            print('Допобачення!')
            break
        else:
            print('Невідома дія. Спробуйте будь ласка ще раз.')
            continue

main()