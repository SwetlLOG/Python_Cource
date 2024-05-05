
"""2. В модуль с проверкой даты добавьте возможность запуска 
    в терминале 
    с передачей даты на проверку
"""


import argparse
from datetime import datetime as dt
from calendar import isleap 

def check_date (date: str):
    try:
       t = dt.strptime(date, "%d.%M.%Y")
       _isleap(t.year)
       return True
    except:
      return False

def _isleap(year: int):
    print("Високосный" if isleap(year) else "Не высокосный")
    
if __name__ == "__main__":
  print(check_date("32.05.1993"))


parser = argparse.ArgumentParser(description='Проверка даты.')
parser.add_argument('date', type=str, help='Проверка даты в формате DD-MM-YYYY')

args = parser.parse_args()


print(check_date(args.date))
  
