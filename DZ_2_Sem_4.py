"""2. Напишите функцию принимающую на вход только ключевые
  параметры и возвращающую словарь, где ключ — значение переданного 
  аргумента, а значение — имя аргумента. Если ключ не хешируем, 
  используйте его строковое представление.
"""



def my_dict(**kwargs):
    temp_dict = {}
    temp_dict = kwargs
    print(temp_dict)
    res = {}
    for i in range(len(temp_dict)):
        for item,value in temp_dict.items():
            if hash(value):
                value
            else:
               value = ','.join(value)
               
            res[value] = item
    print(res)
            
 
    
print(my_dict(arg1="Day",arg2=5,arg3="587"))


