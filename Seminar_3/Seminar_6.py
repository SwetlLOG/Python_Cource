# задача с семинара о парах одинаковых чисел в списке Задача 3
import random as ra
a = [int(i) for i in input().split()]
count = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            count += 1
print(count)


# копирование списков
a = [1, 43, 86]
b = a  # так нельзя!
# лучше так
b = a.copy()
# или так
b = [i for i in a]

# Задача 1

# Метод который позволяет производить input() для переменной и массива и принимает на как параметр значение
# "message" и "arrayIndex" - нужен для определения что данный метод будет заполнять.
# Если "arrayIndex" = True то будет произведен


# def data_entry_method(message="", arrayIndex=False):
#     if arrayIndex:
#         print(message)
#     return [int(i) for i in input().split()]
#     else: 
#     return input(message)
# Метод создает массив заполненный случайными числами от 1 до 10 при помощи метода randrange()
# и принимает на вход размер массива.


def array_create_method(array_size):
    return list([ra.randrange(1, 10) for _ in range(array_size)])
# метод находит элементы которые есть в 1-м массиве но нет во 2-м массиве.


def find_intersections_method(first_array, second_array):
    return [i for i in first_array
            if not (i in second_array)]


def my_comparison(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            arr3.append(arr1[i])
    return arr3


arr1 = input('arr1: ').split()
arr2 = input('arr2: ').split()
arr3 = my_comparison(arr1, arr2)

print('Первый массив: ', *arr1)
print('Второй массив: ', *arr2)
print('Элементов, которых нет во втором массиве: ', *arr3)


# def find_neighbors_of_number(number, array):
#   count_of_neighbors = 0
# for i in range(1,len(array)-1):
#    if (array[i-1]<number) and (array[i+1]<number):
#      count_of_neighbors = count_of_neighbors+1
#     return count_of_neighbors


