"""Напишите функцию для транспонирования матрицы"""

matrix = [[7, 6, 8], [5, 2, 3]]
"""Транспонирование матрицы"""
trans_matrix = [[matrix[j][i] for j in range (len(matrix))] 
                 for i in range(len(matrix[0]))]
  
print(matrix)
print(trans_matrix)


