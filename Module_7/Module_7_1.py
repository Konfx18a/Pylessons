from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return '{0} , {1} , {2}'.format(self.name, self.weight, self.category)

class Shop:
    def __init__(self, name='products.txt', ):
        self.__file_name = name

    def get_products(self):
        file = open(self.__file_name, 'r')
        rezult = file.read()
        file.close()
        return rezult

    def add(self, *products):
        file = open(self.__file_name, 'a')
        line = self.get_products()
        for i in products:
            if line.find(i.name) == -1:
                file.write(str(i)+'\n')
            else:
                print('Продукт {0} уже есть в магазине'.format(i.name))
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
p1 = Product('Яблоко' , '100' , "Фрукты")
p2 = Product('Мороженное' , '250' , "Сладости")
p3 = Product('Торт', '1000' , "Сладости")
# s1 = Shop()
s1.add(p1, p2 , p3)
p4 = Product('Яблоко', '1000' , "Овощ")
s1.add(p4)

