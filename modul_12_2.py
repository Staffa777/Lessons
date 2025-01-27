class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __eq__(self, other):
        if isinstance(other, Runner):
            return self.name == other.name
        return False

    def run(self, distance):
        return distance / self.speed  # Время, которое нужен бегуну для пробежки дистанции

    def walk(self, distance):
        return distance / self.speed  # Мы предположим, что скорость не меняется при ходьбе


class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        for i, runner in enumerate(self.runners):
            # Мы должны отсортировать участников по времени, которое они тратят на дистанцию
            time = runner.run(self.distance)
            results[i + 1] = (runner.name, time)

        # Сортируем по времени, затем по имени
        sorted_results = dict(sorted(results.items(), key=lambda x: x[1][1]))  # Сортировка по времени
        return {key: runner[0] for key, runner in sorted_results.items()}


import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Словарь для хранения результатов всех тестов

    def setUp(self):
        # Создаем бегунов
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов
        for result in cls.all_results.values():
            print(result)

    def test_tournament_1(self):
        # Забег: Усэйн и Ник
        tournament = Tournament(90, [self.runner1, self.runner3])
        results = tournament.start()
        self.all_results["test_tournament_1"] = results
        self.assertTrue(results[2] == "Ник")

    def test_tournament_2(self):
        # Забег: Андрей и Ник
        tournament = Tournament(90, [self.runner2, self.runner3])
        results = tournament.start()
        self.all_results["test_tournament_2"] = results
        self.assertTrue(results[2] == "Ник")

    def test_tournament_3(self):
        # Забег: Усэйн, Андрей и Ник
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        results = tournament.start()
        self.all_results["test_tournament_3"] = results
        self.assertTrue(results[3] == "Ник")