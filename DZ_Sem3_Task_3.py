
import re
def  Cyrillic(text):
  return bool(re.search('[а-я А-Я]', text))
count_en = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JX', 10:'QZ'}
count_ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЕЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
text = input('Введите слово на английском или русском языке    ').upper()
if   Cyrillic(text):
  print(sum([k for i in text for k, v in count_ru.items() if i in v]))
else:
   print(sum([k for i in text for k, v in count_en.items() if i in v]))