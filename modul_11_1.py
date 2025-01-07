
import numpy as np
import matplotlib.pyplot as plt


# Библиотека numpy
# Создаем массивы

a = np.array([1, 2, 3])
a_multiplication = a * 2  # Умножение массива на число
print(f'a = {a}')
print(f'a_multiplication={a_multiplication}')
print(a.size)  # выводим кол-во элементов массива a

# Создаем массивы из целых случайных чисел
b = np.random.randint(5, size=4)
c = np.random.randint(1, 10, size=(2, 5))

print(f'b = {b}')
print(f'c = {c}')

#  Перемножаем матрицы

d = np.arange(1, 10).reshape(3, 3)
print(f'd = {d}')
x = np.dot(a, d)  # Умножаем вектор на матрицу
y = np.dot(d, a)  # Умножаем матрицу на вектор

print(f'x = {x}')

print(f'y = {y}')



# matplotlib

#создаем 3 координатных оси и 3 графика со случайными значениями
ax1 = plt.subplot(2, 3, 1)
ax1.plot(np.random.random(10))
ax2 = plt.subplot(2, 3, 2)
ax2.plot(np.random.random(10))
ax3 = plt.subplot(2, 3, 3)
ax3.plot(np.random.random(10))
ax4 = plt.subplot(2, 1, 2)
ax4.plot(np.arange(0, 5, 0.25), '--o', label='line 1', color='r')
ax4.legend()

plt.suptitle('Графики', fontsize=24, color='g')

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()

plt.show()