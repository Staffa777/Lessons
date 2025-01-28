import logging
import unittest
import rt_with_exceptions as re


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            hum1 = re.Runner('Степаныч', -2)
            hum1.walk()
            logging.info('"test_walk" выполнен успешно')

        except:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            hum1 = re.Runner(444, 3)
            hum1.run()
            logging.info('"test_run" выполнен успешно')

        except:
            logging.warning("Неверный тип данных для объекта Runner")


if __name__ == '__main__':
    unittest.main()

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(funcName)s | %(levelname)s | %(message)s')
