
# N = int(input('Введите число элементов списка А-   '))
# items = input("Введите элементы списка А через пробел-  ").split()
# value = int(input(" Введите целое число "))
items = [4, 5, 9, 6, 5, 4]
value = 7
def nearest_value(items, value):
    found = items[0]
    for tax in items:
      if abs(tax -value) < abs(found - value):
        found = tax
        return found
print (f'Ближайшее число к {value} в списке {items} является {nearest_value(items, value)}')

