"""Возьмите задачу о банкомате из семинара 2. Разбейте 
её на отдельные операции — функции. Дополнительно сохраняйте 
все операции поступления и снятия средств в список
"""
        
        

from decimal import Decimal

MIN_SUM = 50
PROSENT_COMISSION = Decimal(0.015)
MIN_COMISSION = 30
MAX_COMISSION = 600
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX = 5_000_000
TAX_RATE = Decimal(0.1)

def menu(balance: Decimal, count: int, is_flag: bool):
  dct = {'comand': 'Выберите команду:',
         '1': 'Пополнить счет',
         '2': 'Снять со счета',
         '3': 'Выйти из программы'}


  for k , v in dct.items():
    if k.isdigit():
     print(f'{k}: {v}')
    else:
      print(v)
      
  if balance > LIMIT_BEFORE_TAX:
    balance *= (1 - TAX_RATE)
  choice = input('Введите команду:  ')
  if choice == '3':
    print(balance)
    return balance, is_flag
  elif choice == '1':
      balance = give_money(balance)
      count += 1
  elif choice == '2':
      balance = get_money(balance)
      count += 1
  else:
    print('Неверная команда')
  if count % 3 == 0:
      balance *= (1 + BONUS)
  print (balance)
  return balance, is_flag
  
def get_money(balance: Decimal):
  money_to_get = Decimal(input('Введите сумму снятия:  '))
  procent = money_to_get * PROSENT_COMISSION
  
  if money_to_get % MIN_SUM == 0:
    if procent < MIN_COMISSION:
      procent = MIN_COMISSION
    elif procent > MAX_COMISSION:
      procent = MAX_COMISSION
      
    if money_to_get + procent <= balance:
      return balance - (money_to_get + procent)
    else:
      print('Недостаточно средств для снятия')
      return balance
        
    
  else:
   print('Ошибка снятия денег, сумма должна быть кратна 50 ')
   return balance
    
    


def give_money(balance: Decimal):
  money_to_give = Decimal(input('Введите сумму пополнения:  '))
   
  if money_to_give % MIN_SUM == 0:
       return balance + money_to_give 
  else:
       print('Ошибка пополнения, сумма не кратная 50')
       return balance
        

if __name__ == '__main__':
  print('Добро пожаловать в программу банкомат')
  balance = 0
  count = 1
  is_flag = True
  while is_flag:
    balance, is_flag = menu(balance, count, is_flag)


