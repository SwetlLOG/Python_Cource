#Задача 34:Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
#Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
#Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
#в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
#то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает
#в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
#если с ритмом все не в порядке
#Пример:
#Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
#Вывод: Парам пам-пам



chant = "если-я-чешу-в-затылке-не-беда в-голове-моей-опилки-да-да-да но-кричалки-и-вопилки сочиняю-я-не-плохо-иногда-да"
#chant = "пара-ра-рам рам-пам-папам па ра  па-ри-ру-рам-ра-па-дам"
chant_spelled = chant.split()
 
print(chant_spelled)
 
list = [sum(x in 'аоуэыяеюи' for x in lst )
            for lst in chant_spelled]
 
if len(set(list)) == 1:
     res = "Парам пам-пам"  
else: res = "Пам парам"
 
print(res)

