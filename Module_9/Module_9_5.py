class StepValueError(ValueError):
    def __init__(self, msg):
        self.msg = msg

class ConditionsError(ValueError):
    def __init__(self, msg):
        self.msg = msg


class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if (self.start < self.stop and self.step < 0) or (self.start > self.stop and self.step > 0):
            raise ConditionsError('Итератор генерирует расходящуюся последовательность')
        if self.step == 0:
            raise StepValueError('Шаг равен нулю. Мы никуда не идем')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.pointer == self.start:
            self.pointer += self.step
            return self.start
        self.pointer += self.step
        if (self.step < 0 and self.pointer < self.stop) or (self.step > 0 and self.pointer > self.stop):
            raise StopIteration()

        return self.pointer


input_data = [(100, 200, 0), (-5, 1), (6, 15, 2), (5, 1, -1), (10, 1), (0, 7, 1, 5)]
for i in input_data:
    if len(i) < 2 or len(i) >3:
        print('Не верное количество параметров')
        break
    try:
        iter = Iterator(*i)
        for j in iter:
            print(j, end=' ')
        print('\n')
    except (StepValueError, ConditionsError) as ex_in:
        if isinstance(ex_in, StepValueError):
            print('StepValueError: '+ ex_in.msg)
        if isinstance(ex_in, ConditionsError):
            print('ConditionsError: ', ex_in.msg)
