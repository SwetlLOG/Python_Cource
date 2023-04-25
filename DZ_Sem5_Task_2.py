
a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))
 
 
def summa(a, b):
    if b == 0:
        return a
    return summa(a+1, b-1)
 
 
print(summa(a, b))