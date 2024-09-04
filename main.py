class Vehicle:
    """любой транспорт"""

    new_color = str
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'black', 'white', 'greyt']

    def __init__(self, onwer=str, __model=str, color=str, __engine_power=int):
        self.onwer = onwer  # владелец
        self.__model = __model  # модель(марка) транспорта
        self.__engine_power = __engine_power  # мощность двигателя
        self.color = color  # название цвета

    def get_model(self):
        print(f'Модель, {self.__model}, транспорта')

    def get_horsepoewr(self):
        print(f'Мощность двигателя {self.__engine_power}')

    def get_color(self):
        print(f'Цвет транспорта {self.color}')

    def print_info(self):
        print(
            f'Модель, {self.__model}\nМощность двигателя, {self.__engine_power} \nЦвет транспорта , {self.color} '
            f'\nВладелец , {self.onwer}')

    def set_color(self, new_color=str):
        if any(item in new_color.lower() for item in Vehicle.__COLOR_VARIANTS):
            self.color = new_color
        else:
            print(f'Нельзя изменить цвет на {new_color}')


class Sedan(Vehicle):
    """седны"""
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark ||', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('pink')
vehicle1.set_color('BLACK')
vehicle1.onwer = 'Vasya'
vehicle1.print_info()
