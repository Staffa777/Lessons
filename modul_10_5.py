import time
import multiprocessing

# Функция для считывания данных из файла
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Выход из цикла, если строка пустая
                break
            all_data.append(line.strip())  # Добавление строки в список (без лишних символов)
    return all_data

# Список файлов для чтения
filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = time.time()
for filename in filenames:
    read_info(filename)  # Чтение данных по очереди
linear_time = time.time() - start_time
print(f'Время выполнения линейного вызова: {linear_time:.4f} секунд')

# Многопроцессный вызов
start_time = time.time()
with multiprocessing.Pool() as pool:
    pool.map(read_info, filenames)  # Параллельное выполнение чтения файлов
multi_time = time.time() - start_time
print(f'Время выполнения многопроцессного вызова: {multi_time:.4f} секунд')
