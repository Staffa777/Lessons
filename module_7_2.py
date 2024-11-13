def custom_write(file_name, strings):
    strings_positions = {}                              # Создаем пустой словарь strings_positions
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings , start=1):
            # Для получения номера байта начала строки используется метод tell() перед записью
            position = file.tell()                      # Получаем текущую позицию в файле
            # Функция записывает в файл file_name все строки из списка strings, каждая на новой строке
            file.write(string + '\n')                  # Записываем строку и переходим на новую строку
            # Создаем словарь strings_positions, где ключом будет кортеж
            # (<номер строки>, <байт начала строки>), а значением - записываемая строка
            strings_positions[(i , position)] = string  # Добавляем информацию о строке в словарь
    return strings_positions                            # Возвращаем словарь strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)