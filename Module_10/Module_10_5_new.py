import multiprocessing as mp

class My:

    def __init__(self):
        self.data = {}
        self.proceses = []

    def in_proc(self, a, b):
        self.data[a] = b
        print(f'Печатаем ВЕСЬ!!!!!!!! словарь : {self.data}')

    def my_run(self, req_):
        if __name__ == '__main__':
            for i in req_:
                p = mp.Process(target=self.in_proc, args=(*i,))
                self.proceses.append(p)
                p.start()
                print('запущен процесс', p.name)
                print(f'Словарь : {self.data}')

            for i in self.proceses:
                i.join()
                print('Закончился процесс', i.name)


my = My()
request = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
my.my_run(request)
print(f'И вот в итоге ВЕЕЕЕСЬ !!!! словарь: {my.data}')
