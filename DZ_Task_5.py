n = int(input())
count_0 = 0
count_1 = 0
for i in range(n):
    a = int(input())
    if a == 0:
      count_0 += 1
    else:
      count_1 += 1
if count_1 > count_0:
    print(count_0)
else:
    print(count_1)
