from random import randint

lst = []
for i in range(int(input("Введите натуральное  число  "))):
    n = randint(1, 10)
    lst.append(n)
print(lst)
find = int(input("Введите искомое число "))
cont = 0
if find in lst:
    cont += 1
print(cont)
