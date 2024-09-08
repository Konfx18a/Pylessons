import unittest
import runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        peshehod = runner.Runner('пешеход')
        for _ in range(1, 11):
            peshehod.walk()
        self.assertEquals(peshehod.distance, 50)

    def test_run(self):
        begun = runner.Runner('бегун')
        for _ in range(1,11):
            begun.run()
        self.assertEquals(begun.distance, 100)

    def test_challenge(self):
        peshehod = runner.Runner('пешеход')
        begun = runner.Runner('бегун')
        for _ in range(1,11):
            begun.run()
            peshehod.walk()
        self.assertNotEquals(begun.distance, peshehod.distance)

if __name__ == '__main__':
    unittest.main()