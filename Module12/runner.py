#
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
        # сортируем сразу, чтоб при дистанции <= скорости самого медленного
        # порядок бегунов в забеге не влиял на результат и первый бежал по первой дорожке
        self.participants = sorted(self.participants, key=lambda x: x.speed, reverse=True)

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
                    break # чтобы в цикле был итератор урезанного списка

        return finishers

p = []
p.append(Runner('q',10))
p.append(Runner('w',5))
p.append(Runner('e',3))
secound_tour = Tournament(6, *p)
print(secound_tour)