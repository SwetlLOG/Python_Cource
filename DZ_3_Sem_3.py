""" Задача 3 Создайте словарь со списком вещей для похода в качестве 
ключа и их массой в качестве значения. Определите какие вещи влезут
 в рюкзак передав его максимальную грузоподъёмность. Достаточно 
 вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

dic = {'палатка': 5, 'спальник': 3, 'еда': 4, 'вода': 2, 'личные вещи': 1}

max_weight = 12
def baskpack(dic, max_weight):
     possible_items = []
     for dic, weight in dic.items():
         if weight <= max_weight:
             possible_items.append(dic)
             max_weight -= weight
     return possible_items


print(f'Возможный вариант комплектации рюкзака ', baskpack(dic, max_weight))