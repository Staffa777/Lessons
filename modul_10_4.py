import threading
import random
import time
from queue import Queue

# Класс Table
class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None     # Гость за столом (по умолчанию None)

# Класс Guest
class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # Имя гостя

    def run(self):
        # Ожидание случайное время от 3 до 10 секунд
        time.sleep(random.randint(3, 10))

# Класс Cafe
class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для гостей
        self.tables = tables  # Список столов в кафе

    def guest_arrival(self, *guests):
        # Принимаем гостей
        for guest in guests:
            # Ищем свободный стол
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest  # Садим гостя за стол
                guest.start()  # Запускаем поток
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)  # Если столов нет, гость идет в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        # Обслуживаем гостей, пока не пустая очередь или хотя бы один стол занят
        while any(table.guest is not None for table in self.tables) or not self.queue.empty():
            for table in self.tables:
                if table.guest and not table.guest.is_alive():  # Гость закончил приём пищи
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    # Если в очереди есть гости, сажаем одного за свободный стол
                    if not self.queue.empty():
                        guest = self.queue.get()
                        table.guest = guest
                        guest.start()
                        print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(1)  # Задержка, чтобы не перегружать процессор

# Пример работы программы
if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()