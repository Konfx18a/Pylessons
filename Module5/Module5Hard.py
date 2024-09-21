from time import sleep
class User:
    def __init__(self, name, pswd, age):
        self.nickname = name
        self.password = hash(pswd)
        self.age = age

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        else:
            print('Типы объектов не совпадают')

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        else:
            print('Типы объектов не совпадают')

    def __str__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, item):
        if isinstance(item, User):
            for i in self.users:
                if i == item:
                    return item
        if isinstance(item, Video):
            for i in self.videos:
                if i == item:
                    return item

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname:
                if i.password == hash(password):
                    self.current_user = i
                else:
                    print('для пользователя ' + nickname + ' введен не верный пароль')

    def register(self, nickname, password, age):
        if User(nickname, password, age) in self.users:
                print('Пользователь ником {0} существует!'.format(nickname))
                return
        self.users.append(User(nickname, password, age))
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for i in video:
            if not i in self.videos:
                self.videos.append(i)
                # print(i.title)

    def get_videos(self, v_title):
        ret_v = []
        for i in self.videos:
            if i.title.upper().count(v_title.upper()):
                ret_v.append(i.title)
        return ret_v

    def play_video(self):
        for i in range(1,11):
            print(i)
            sleep(1)
        print('Конец видео')


    def watch_video(self, video):
        if not self.current_user:
            print('Войдите в аккаунт, чтоб смотреть видео')
            return
        for i in self.videos:
            if i.title == video:
                if not i.adult_mode:
                    self.play_video()
                elif self.current_user.age > 18:
                    self.play_video()
                else:
                    print(' Вам нет 18 лет, пожалуйста покиньте страницу ')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# uR = UrTube()
# v1=Video('qw',10, adult_mode=False)
# v2=Video('er',10, adult_mode=True)
# v3=Video('qw',10, adult_mode=False)
# uR.add(v1, v2, v3)
#
# uR.register('oleg', '12345', 45)
# print(uR.users[0])
# uR.register('oleg', '123', 35)
# uR.register('alex', '1234', 15)
# uR.register('oleg', '12345', 25)
# uR.log_in('oleg', '12345')
# print(uR.current_user.nickname)
# uR.log_in('alex', '12345')
# print(uR.current_user.nickname)
# print(uR.get_videos('qw'))
# uR.print_u()
# uR.print_v()


