

n = int(input('Введите число кустов n = '))
list = [int(x) for x in input('Введите кол-во ягод с куста-> ').split()]
n = len(list)
list = list + list[:2]
na = 0
for i in range(n):
    na = max(na, list[i] + list[i+1] + list[i+2])
print(na)
