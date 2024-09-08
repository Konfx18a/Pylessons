import unittest as ut
from pprint import pprint
import runner


class TournamentTest(ut.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results ={}

    def setUp(self):
        self.partisipations = []
        self.partisipations.append(runner.Runner('Усейн', 10))
        self.partisipations.append(runner.Runner('Александр', 9))
        self.partisipations.append(runner.Runner('Ник', 3))


    def test_tour1(self):
        first_tour = runner.Tournament(6, self.partisipations [0] , self.partisipations[2])
        rezult = first_tour.start()
        self.assertTrue(rezult[len(rezult)] == self.partisipations[-1])
        self.all_results['first_tour'] = rezult

    def test_tour2(self):
        secound_tour = runner.Tournament(6, self.partisipations[1], self.partisipations[2])
        rezult = secound_tour.start()
        self.assertTrue(rezult[len(rezult)] == self.partisipations[-1])
        self.all_results['secound_tour'] = rezult

    def test_tour3(self):
        third_tour = runner.Tournament(6, *self.partisipations)
        rezult = third_tour.start()
        self.assertTrue(rezult[len(rezult)] == self.partisipations[-1])
        self.all_results['third_tour'] = rezult

    @classmethod
    def tearDownClass(self):
       for key,value in self.all_results.items():
           print (f' {key} ')
           for i, j in value.items():
               print(f' {i} : {j}')


if __name__ == '__main__':
    ut.main()