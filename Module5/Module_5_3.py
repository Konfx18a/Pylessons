from random import randint


class House:
    def __init__(self, name, num_of_floor):
        self.name = name
        self.number_of_floor = num_of_floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(i, 'Этаж')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return 'Название: ' + self.name + ' количество этажей: ', self.number_of_floor

    def __eq__(self, other):
        if self.number_of_floor == other.number_of_floor:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor

    def isother(self, other):
        if not isinstance(other, House):
            print ('типы объектов не совпадают!!!')
        else:
            return True

    def __gt__(self, other):
        if self.isother(self, other):
            return self.number_of_floor > other.number_of_floor

    def __le__(self, other):
        if self.isother(self, other):
            return self.number_of_floor <= other.number_of_floor

    def __gt__(self,other):
        if self.isother(self, other):
            return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        if self.isother(self, other):
            return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        if self.isother(self, other):
            return self.number_of_floor <= other.number_of_floor

    def __add__(self, value):
        if isinstance(value, int):
            return self.number_of_floor + self.number_of_floor + value
        else:
            print(value + 'должно быть целым числом')

    def __radd__(self, other):
        if self.isother(self, other):
            return self.number_of_floor + other.number_of_floor

    def __iadd__(self, other):
        if self.isother(self, other):
            self.number_of_floor += other.number_of_floor
            return self.number_of_floor

new_house = House('ЖК Нью-Васюки', 10)
new_house1 = House('ЖК Нищеброд', 10)
new_house.go_to(9)
print(new_house + new_house1)
print(new_house.__str__())
