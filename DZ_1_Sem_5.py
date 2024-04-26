"""Task 1 Напишите функцию, которая принимает на вход строку - 
абсолютный путь до файла. Функция возвращает кортеж из 
трёх элементов: путь, имя файла, расширение файла."""

import os


def parse_path(path):
    filepath, file_extention = os.path.splitext(path)
    filepath, filename = os.path.split(filepath)
    return (filepath, filename, file_extention)

path = str(input("Введите абсолютный путь до файла: "))
print(parse_path(path))


