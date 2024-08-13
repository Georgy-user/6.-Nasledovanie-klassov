class Vehicle:
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    __COLOR_VARIANTS = ['yellow', 'peat', 'gold', 'khaki', 'brown']

    def get_model(self):
        return f'Модель: {self.__model}.'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}.'
    def get_color(self):
        return f'Цвет: {self.__color}.'


    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horsepower()} '
              f'\n{self.get_color()} \nВладелец: {self.owner}.')
    def set_color(self, new_color):
        new_color = new_color.lower()
        for color in self.__COLOR_VARIANTS:
            if color == new_color:
                self.__color = new_color
                break
        if self.__color != new_color:
            print("Нельзя сменить цвет на new_color.")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Шеф', 'Toyota Mark II', 'peat', 500)
vehicle1.print_info()
print()
vehicle1.set_color('Pink')
print()
vehicle1.set_color('GOLD')
vehicle1.owner = 'Бродяга'
print()
vehicle1.print_info()

