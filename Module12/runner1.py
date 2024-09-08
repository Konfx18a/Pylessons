import logging
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            # logging.warning("Name = int", exc_info=True)
            raise TypeError(f'Имя не может быть только числом, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            # logging.warning("Speed<0", exc_info=True)
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')



    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
logging.basicConfig(level=logging.INFO, filemode='w', filename='test.log',
                format='%(asctime)s | %(levelname)s | %(message)s')
# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)

# t = Tournament(101, first, second)
# print(t.start())