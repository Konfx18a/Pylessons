import logging
import unittest
import runner1

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Пропущен по skip - true')
    def test_walk(self):
        try:
            peshehod = runner1.Runner('пешеход',-5)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(1,11):
                peshehod.walk()
            self.assertEquals(peshehod.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner',exc_info=True)


    @unittest.skipIf(is_frozen, 'Пропущен по skip - true')
    def test_run(self):
        try:
            begun = runner1.Runner(2)
            logging.info('"test_run" выполнен успешно')
            for _ in range(1,11):
                begun.run()
            self.assertEquals(begun.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner",exc_info=True)

    @unittest.skipIf(is_frozen, 'Пропущен по skip - true')
    def test_challenge(self):
        peshehod = runner1.Runner('пешеход')
        begun = runner1.Runner('бегун')
        for _ in range(1,11):
            begun.run()
            peshehod.walk()
        self.assertNotEquals(begun.distance, peshehod.distance)

if __name__ == '__main__':

    unittest.main()
