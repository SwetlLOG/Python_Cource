##. Программа загадывает число от 0 до 1000. Необходимо угадать 
# число за 10 попыток. Программа должна подсказывать “больше” или
# “меньше” после каждой попытки. Для генерации случайного числа
# используйте код:
## from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT


import random
randintnum = random.randint(1,1000)
usernum = -1
while usernum !=randintnum:
  usernum = int(input('Угадай число от 1 до 1000    '))
  if usernum > randintnum:
    print('Число должно быть меньше!     ')
  elif usernum < randintnum:
    print('Число должно быть больше!    ')
  else:
    print('Вы угадали! Это число =     ' + str(randintnum))
    
    break
    
