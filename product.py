from main import tovar

class Product:
    def __init__(self, add_tov: str, red_tov: str, del_tov: str):
        self.add_tov = add_tov
        self.red_tov = red_tov
        self.del_tov = del_tov


    def add_tovar(self):
        tovar['ID'] = input('Введіть ID товару:')
        tovar['Назва'] = input('Введіть назву товару:')
        tovar['Категорія'] = input('Введіть категорію:')
        tovar['Ціна'] = input('Введіть ціну:')
        tovar['Кількість на складі'] = input('Введіть кількість на складі:')
        tovar['Опис'] = input('Введіть опис:')
