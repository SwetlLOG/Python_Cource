from random import randint

lst1 = [1, 1, 2, 0, -1, 3, 4, 4] # задать список чисел вручную

lst2 = list() # задать пустой список
for i in range(5):
    n = int(input())
    lst2.append(n) # в цикле заполнить список числами вводом с клавиатуры

lst3 = [] # задать пустой список
for i in range(10):
    n = randint(1, 5)
    lst3.append(n) # в цикле заполнить список случайными числами

# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
unique_list = []
print(lst3)
for elem in lst3:
    if elem not in unique_list:
        unique_list.append(elem)
print(len(unique_list)) # выводим количество уникальных элементов

# Задача №19. 
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

# Первый способ решения - циклически с помощью pop и insert
print(lst3)
k = int(input('введите сдвиг '))
for i in range(k):
    a = lst3.pop() # выдернули последний элемент из списка
    lst3.insert(0, a) # вставили этот элемент в начало
print(lst3)

# Второй способ - через срезы
print(lst1)
k = 3
lst_a = lst1[-k:]
lst_b = lst1[:-k]
print(lst_a + lst_b)