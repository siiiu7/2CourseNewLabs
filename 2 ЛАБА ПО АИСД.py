'''
Лабораторная работа № 2
Вариант 24
Шеснадцатиричные числа, не превышающие 1024_10 расположенные в порядке убывания.
Для каждой такой последовательности максимальное число вывести прописью.
'''

import re

max_hex = '0'
count = 0

slov = {
    0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть',
    7: 'семь', 8: 'восемь', 9: 'девять',
    'A': 'десять', 'B': 'одинадцать', 'C': 'двенадцать', 'D': 'тринадцать',
    'E': 'четырнадцать', 'F': 'пятнадцать', '.': 'точка'
}

pattern = re.compile(r'\b(?:[0-9A-Fa-f]+(?:\.[0-9A-Fa-f]*)?|\.[0-9A-Fa-f]+)(?:[Pp][-+]?[0-9]+)?\b')

with open("text.txt", 'r') as file:
    for line in file:
        for match in pattern.finditer(line):
            num = match.group()
            if num[0] == '0' and len(num) > 1:
                continue
            try:
                val = float.fromhex(num)
                if val <= 1024:
                    print(num, end=" ")
                    count += 1
                    if val > float.fromhex(max_hex):
                        max_hex = num
            except (TypeError, ValueError):
                pass

if max_hex == '0':
    print('В файле нет чисел, удовлетворяющих условию')
else:
    print('\nКоличество:', count)
    print('Максимальное число:', end=' ')
    for char in max_hex:
        for key in slov:
            if str(key) == char.upper():
                print(slov[key], end=' ')
                break
