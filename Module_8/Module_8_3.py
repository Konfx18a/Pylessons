class Car:
    def __init__(self, model, vin, number):
        self.model = model
        self.__vin = None
        self.__numbers = None
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(number):
            self.__numbers = number

    def __str__(self):
        return f'Модель: {self.model}, VIN: {self.__vin}, Номера: {self.__numbers}'

    def __is_valid_vin(self, vin_number):

        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(f'У {self.model} Некорректный тип vin номер')
        if (vin_number < 1000000) or (vin_number > 9999999):
            raise IncorrectVinNumber(f'У {self.model} Неверный диапазон для vin номера')

        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(f'У {self.model} Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers(f'У {self.model} Неверная длина номера')

        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


cars_data = [('Model1', 1000000, 'f1283dj'), ('Model2', 300, 'т001тр'), ('Model3', 1000000, 'f123dj'),
             ('Model4', 300, 'т001тр'), ('Model5', 2020202, 10)]
cars = []
for i in cars_data:
    try:
        c = Car(*i)
        cars.append(c)
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{c} успешно создан')

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second} успешно создан')
#пример из задания
try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third} успешно создан')

