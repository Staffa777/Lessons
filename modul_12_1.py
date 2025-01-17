class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def walk(self):
        self.distance += 5

    def run(self):
        self.distance += 10

# Тесты для класса Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        # Создаем объект класса Runner
        runner = Runner("Вася")
        # Вызываем метод walk 10 раз
        for i in range(10):
            runner.walk()
        # Проверяем, что distance равен 50
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        # Создаем объект класса Runner
        runner = Runner("Вася")
        # Вызываем метод run 10 раз
        for i in range(10):
            runner.run()
        # Проверяем, что distance равен 100
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        # Создаем два объекта класса Runner
        runner1 = Runner("Вася")
        runner2 = Runner("Петя")
        # У первого объекта вызываем run, у второго - walk
        for i in range(10):
            runner1.run()
            runner2.walk()
        # Проверяем, что distance у двух объектов не равны
        self.assertNotEqual(runner1.distance, runner2.distance)

# Запуск тестов
if __name__ == "__main__":
    unittest.main()