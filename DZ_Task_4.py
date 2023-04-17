print("Введите размер шоколадки n ")
n = int(input())
print("Введите размер шоколадки m ")
m = int(input())
print("Введите количество долек к ")
k = int(input())
if k < m*n and (k%m == 0 or k%n ==0):
  print("Можно разломить! ")
else:
  print("Нельзя...")
  