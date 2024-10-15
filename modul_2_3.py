from modul_2.modul_2_2 import namber
#"Цикл for. Элементы списка. Полезные функции в цикле"
nambers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in nambers:
    if num == 1:
        continue
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
        break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
print('Primes: ' , primes)
print('Not_primes: ' , not_primes)
print('______________________________________________')


