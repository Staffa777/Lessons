#"Стиль кода часть II. Цикл While."
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len((my_list)):
    namber = my_list[i]
    if namber < 0:# Если элемент отрицательный, прерываем цикл
        break
    if namber > 0:
        print(namber)
    i += 1