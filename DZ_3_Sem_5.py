""" Создайте функцию генератор чисел Фибоначчи"""


def fibonacci(num:int):
    a, b = 0, 1
    for _ in range(num):
        yield a + b
        a, b = b, a + b


num = int(input('Введите число необходимое число:  '))
res = [i for i in range(1, num+1)]
print(res)


