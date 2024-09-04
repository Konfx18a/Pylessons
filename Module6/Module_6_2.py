class Vehicle:

    __COLOR_VARIANTS = ['red', 'green', 'black']

    def __init__(self, owner, model, engine_p, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_p
        self.__color = color

    def get_model(self):
        print('Модель: {0}'.format(self.__model))

    def get_horsepower(self):
        print('Мощность: {0}'.format(self.__engine_power))

    def get_color(self):
        print('Цвет: {0}'.format(self.__color))

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print('Владелец: {0}'.format(self.owner))

    def set_color(self, new_color):
        for i in self.__COLOR_VARIANTS:
            if i.upper() == new_color.upper():
                self.__color = new_color
                return
        print('Нельзя сменить цвет на {0}'.format(new_color))

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
car = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
car.print_info()

# Меняем свойства (в т.ч. вызывая методы)
car.set_color('Pink')
car.set_color('BLACK')
car.owner = 'Vasyok'

# Проверяем что поменялось
car.print_info()

print(dir(Vehicle))

# Доступ к приватным аттрибутам объекта
print(car._Vehicle__color)

