
import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем TestSuite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))  # Добавляем тесты из RunnerTest
    suite.addTest(unittest.makeSuite(TournamentTest))  # Добавляем тесты из TournamentTest
    return suite

if __name__ == "__main__":
    # Создаем объект TextTestRunner с verbosity=2
    runner = unittest.TextTestRunner(verbosity=2)
    # Запускаем тесты
    runner.run(suite())

import functools
import unittest

def freeze_test(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print(f"Тест {func.__name__} пропущен: Тесты в этом кейсе заморожены")
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return func(self, *args, **kwargs)
    return wrapper

import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Здесь изменяем атрибут на False

    @freeze_test
    def test_challenge(self):
        self.assertEqual(1, 1)

    @freeze_test
    def test_run(self):
        self.assertTrue(True)

    @freeze_test
    def test_walk(self):
        self.assertEqual(2, 2)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Здесь изменяем атрибут на True

    @freeze_test
    def test_first_tournament(self):
        self.assertEqual("winner", "winner")

    @freeze_test
    def test_second_tournament(self):
        self.assertEqual(100, 100)

    @freeze_test
    def test_third_tournament(self):
        self.assertTrue(True)