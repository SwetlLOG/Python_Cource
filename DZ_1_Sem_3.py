
"""
 Дан список повторяющихся элементов. 
   Вернуть список с дублирующимися элементами.
   В результирующем списке не должно быть дубликатов.
"""


lst = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

def find_dupl(lst):
    return list(set([i for i in lst if lst.count(i) > 1]))


print(find_dupl(lst))