##3. Напишите код, который запрашивает число и сообщает является
# ли оно простым или составным. Используйте правило для проверки: 
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел
# больше 100 тысяч.



def choice():
   num = int(input("Введите число on 0 до 100000 "))

   if num < 0 or num > 100000:
      return "Введено недопустимое число. Допустимы числа от 0 до 100000."

   if num == 1 or num == 0:
      return "Число не является ни простым, ни составным."
   
   for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
       return "Число составное."
   return "Число простое."

print(choice())