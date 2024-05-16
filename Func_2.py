"""Напишите функцию, которая получает на вход директорию
и рекурсивно обходит её и все вложенные директории. Результаты
обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий
размер файлов в ней с учётом всех вложенных файлов и директорий.
3. Соберите из созданных на уроке и в рамках домашнего задания 
функций пакет для работы с файлами разных форматов.
"""
import os
import csv
import json
import pickle


def get_directory_size(path):
    """Функция для получения размера директории в байтах"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            f1 = os.path.join(dirpath, f)
            total_size += os.path.getsize(f1)
    return total_size

def directory_info(path):
    """ Функция для получения информации о директории и ее файлах"""
    res = []
    for root, dirs, files in os.walk(path):
        dirname = os.path.basename(root)
        dirsize = get_directory_size(root)
        res.append({
            'name': dirname,
            'type': 'directory',
            'size': dirsize,
            'parent_directory': os.path.dirname(root),
        })
   
        for file in dirs:
            full_path = os.path.join(root, file)
            res.append({"parent_directory": root, 
                            "is_file": False,
                            "name": file,
                            "size_in_bytes": get_directory_size(full_path)})

    with open("output.json", "w") as json_file:
        """ сохраняем результат в формате Json"""
        json.dump(res, json_file)
        
    fieldnames = ['name','type','size','parent_directory']
    with open("output.csv", "w",newline='') as csv_file:
        """ сохраняем результат в формате csv"""
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(res)

    with open("output.pickle", "wb") as pickle_file:
        pickle.dump(res, pickle_file)

directory_info("./my_folder")
      
           
   
  
  
  
