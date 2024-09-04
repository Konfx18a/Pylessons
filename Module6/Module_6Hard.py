from math import pi

class Figure:
    side_count = 0
    def __init__(self, color, *sides, filled = False):
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.side_count
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = 0, 0, 0
        self.filled = filled

    def __len__(self):
        return sum(self.__sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        if len(sides) != self.side_count:
            return False
        for i in sides:
            if not isinstance(i, int) and i < 0:
              return False
        return True

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


#----------------------------------------------------
class Circle(Figure):
    side_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / (2 * pi)


    def get_square(self):
        return (pi*self.__radius ** 2) / 4

#-------------------------------------------------
class Triangle(Figure):
    side_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        p = sum(sides) / 2
        a = sides[0]
        b = sides[1]
        c = sides[2]
        self.__height = 2 * (p*(p-a)*(p-b)*(p-c))**0.5 / a

    def get_square(self):
        return self.__height * self.get_sides()[0] / 2
#----------------------------------------------------------
class Cube(Figure):
    side_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        # Надеюсь это то, что от меня требуется. А то коробит приватные члены класса из потомков менять))))
        if len(sides) == 1 and isinstance(sides[0], int):
            self._Figure__sides = list(sides)*self.side_count




    def get_volume(self):
        return self.get_sides()[0] ** 3

# NB! Цвет оставил кортежем. Везде его вроде кортежем передают, если необходимо:
# 11             self.__color = list(color)
# 13             self.__color = [0] *3
# 30             self.__color = list(r, g, b)
cube1 = Cube((222, 35, 130), 6)
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())
