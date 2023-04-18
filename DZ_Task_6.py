a = int(input())
b = int(input())
for i in range(a):
  for j in range(b):
    if a == i + j and b == i * j:
      print(i, j)