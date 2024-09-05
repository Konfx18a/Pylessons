from random import choice

first =  'Мама мыла раму'
second = 'Рамена мало было'
rezult = list(map(lambda x, y: x == y, first, second))
print(rezult)
def get_advanced_writer(file_name):

    def write_everything(*data_set):

        with open(file_name, 'a+') as file:
            for i in data_set:
                file.write(str(i)+'\n')

    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
rand_words = MysticBall('Yes','No','Maybe')
for i in range(1,5):
    print(rand_words())
