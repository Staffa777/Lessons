from tkinter.font import names


class Animal:                                   # Создаём класс родитель для животных - Animal
    def __init__(self , name):                  # Устанавливаем начальное состояние: животное живое и не накормленное
        self.alive = True                       # Животное живое
        self.fed = False                        # Животное не накормлено
        self.name = name                        # Индивидуальное название животного
class Plant:                                    # Создаём класс родитель для растений - Plant
    def __init__(self, name, edible=False):     # Устанавливаем начальное состояние: растение съедобное или несъедобное
        self.edible = edible                    # По умолчанию растение несъедобное
        self.name = name                        # Индивидуальное название растения
class Mammal(Animal):                           # Создаём класс Млекопитающие - наследник для класса Животных.
    def eat(self, food):                        # Создаём метод eat для млекопитающих, позволяющий им есть растения
        if isinstance(food , Plant):            # Проверяем, является ли еда растением
            if food.edible:                     # Если растение съедобное
                print(f'{self.name} съел {food.name}')  # Животное съело растение
                food.fed = True                 # Животное наелось
            else:
                print(f'{self.name} не стало есть {food.name}') # Животное отказалось от еды
                self.alive = False               # Животное погибло из-за несъедобного растения
        else:
            print(f'{food.name} не является растением. {self.name} не может это съесть')# Если еда не является растением
class Predator(Animal):                         # Создаём класс Хищники - наследник для класса Животных
    def eat(self,food):                         # Создаём метод eat для хищников, позволяющий им есть растения
        if isinstance(food , Plant):            # Проверяем, является ли еда растением
            if food.edible:                     # Если растение съедобное
                print(f'{self.name} съел {food.name}')  # Хищник съел растение
                food.fed = True                # Хищник накормлен
            else:
                print(f'{self.name} не стало есть {food.name}') # Хищник отказался от еды
                self.alive = False              # Хищник погиб из-за несъедобного растения
        else:
            print(f'{food.name} не является растением. {self.name} не может это съесть')# Если еда не является растением
class Flower(Plant):                            # Создаём класс Цветы - наследник для класса Растений.
    def __init__(self,name):                    # Вызываем конструктор родительского класса Plant и устанавливаем,
                                                # что фрукты съедобные
        super().__init__(name , edible=False)   # Цветы по умолчанию несъедобные
class Fruit(Plant):                             # Создаём класс Фрукты - наследник для класса Растений
    def __init__(self,name):
        super().__init__(name , edible=True)    # Фрукты по умолчанию съедобные
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


