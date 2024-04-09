# Задача 2. Напишите программу, которая получает целое число и возвращает 
# его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата



def new_num(num):
    new_digits = "0123456789abcdef"
    new_str = ""
    while num > 0:
        new_str = new_digits[num % 16] + new_str
        num = num // 16
    return new_str
print ("{new_str}")

num = int(input('Введите число '))
new_str = new_num(num)
print(f"Шестнадцатеричное представление числа {num} = {new_str}")


