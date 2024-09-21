from random import randint


class House:
    def __init__(self, name, num_of_floor):
        self.name = name
        self.number_of_floor = num_of_floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor):
                print(i, 'Этаж')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return 'Название: ' + self.name + ' количество этажей: ', self.number_of_floor

new_house = House('ЖК Нью-Васюки', randint(1, 20))
new_house.go_to(randint(-2, 20))
print(new_house.__len__())
print(new_house.__str__())
