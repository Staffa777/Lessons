from operator import floordiv
from sys import implementation


class House:
    def __init__(self,name,namber_of_floors = 0):
        self.name = name
        self.namber_of_floors = namber_of_floors
    def setnew_namber_of_floors(self,floors):       # Метод для изменения количества этажей.
        self.namber_of_floors = floors
        print(self.namber_of_floors)
    def __eq__(self, other):                        #Метод сравнения на равенство (==)
        if isinstance(other , House):
            return self.namber_of_floors == other.namber_of_floors
        return False
    def __lt__(self, other):                        #Метод сравнения на меньше (<)
        if isinstance(other , House):
            return self.namber_of_floors < other.namber_of_floors
        return NotImplemented
    def __le__(self, other):                        #Метод сравнения на меньше или равно (<=)
        if isinstance(other , House):
            return self.namber_of_floors <= other.namber_of_floors
        return NotImplemented
    def __gt__(self, other):                        #Метод сравнения на больше (>)
        if isinstance(other , House):
            return self.namber_of_floors > other.namber_of_floors
        return NotImplemented
    def __ge__(self, other):                        #Метод сравнения на больше или равно (>=)
        if isinstance(other , House):
            return self.namber_of_floors >= other.namber_of_floors
        return NotImplemented
    def __ne__(self, other):                        #Метод сравнения на неравенство (!=)
        if isinstance(other , House):
            return self.namber_of_floors != other.namber_of_floors
        return True
    def __add__(self, value):                       #Метод сложения для увеличения этажей (+)
        if isinstance(value , int):
            return House(self.namber_of_floors + value)
        elif isinstance(House, value):
            return House(self.name , self.namber_of_floors + value.namber_of_floors)
        return NotImplemented
    def __radd__(self, value):                      #Метод обратного сложения (слева от +)
        return self.__add__(value)                  # Используем логику __add__
    def __iadd__(self, value):
        return self.__add__(value)
    def __str__(self):                              #Метод строкового представления объекта
        return f'Название: {self.name} , Количество этажей: {self.namber_of_floors}'
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
