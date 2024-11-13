class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name} , {self.weight} , {self.category}'

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        # Метод get_products(self), который считывает всю информацию из файла __file_name,
        # закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        try:
            with open(self.__file_name , 'r') as file:
                return file.read()
        except FileNotFoundError:
            return 'Ошибка "Файл не найден:"'
    def add(self , *products):
        # Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
        existing_products = self.get_products().split('\n')
        # Имена продуктов записываются в existing_product_names. Так как строки в файле имеют формат
        # '<название>, <вес>, <категория>', то берется первая часть [0]. В качестве разделителя используется ', '.
        # Для добавления, если строка line не пустая, цикл for перебирает все строки из списка existing_products
        existing_products_names = {line.split(',') [0] for line in existing_products if line}
        with open(self.__file_name , 'a') as file:
            for product in products:
                if product.name is existing_products_names:
                    # Если такой продукт уже есть, то не добавляет и выводит строку
                    # 'Продукт <название> уже есть в магазине'.
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    # Добавляет в файл __file_name каждый продукт из products,
                    # если его ещё нет в файле (по названию)
                    file.write(str(product) + '\n')
                    existing_products_names.add(product.name)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
