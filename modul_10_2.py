from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power
        print(f'Привет, меня зовут {self.name}, моя сила равна {self.power}, я помогу вам! ')
        self.warrior = 100

    def run(self):
        warrior = 100
        print(f'{self.name} на нас напали!')

        for i in range(warrior):
            self.res = warrior - self.power
            print(f'{self.name} сражается {i-1} день (дня)..., осталось {self.res} воинов')
            sleep(i)
            warrior = self.res
            if warrior <= 0:
                return print(f'{self.name} одержал победу спустя {i+1} дня(дней)!')
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились')

print('_______________________________________________________________________________')