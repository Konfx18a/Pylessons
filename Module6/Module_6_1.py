class Animal:

    def __init__(self, name, alive = True, fed = False):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food):
        if food.edible:
            self.fed = True
            print (' {0} съел {1} '.format(self.name, food.name))
        else:
            self.alive = False
            print(' {0} не стал есть {1} '.format(self.name, food.name))

class Plant:

    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):

    def __init__(self, name):
        super().__init__(name)
        self.edible = False

class Fruit(Plant):

    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(f'{a1.name} живой ли? {a1.alive}')
print(f'{a2.name} накормлен ли? {a2.fed}')
a1.eat(p1)
a2.eat(p2)
print(f'{a1.name} живой ли? {a1.alive}')
print(f'{a2.name} накормлен ли? {a2.fed}')
# print(a1.alive)
# print(a2.fed)