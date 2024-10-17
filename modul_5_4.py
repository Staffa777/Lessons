class House:
    houses_history = []             # атрибут будет хранить названия созданных объектов
    def __new__(cls, *args, **kwargs): # ,*args ,**kwarqs
        cls.houses_history.append(args[0])
        print(*cls.houses_history)
        return super().__new__(cls)
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
    def __del__(self):
        print(self.name , 'Cнесен, но он останется в истории')
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)