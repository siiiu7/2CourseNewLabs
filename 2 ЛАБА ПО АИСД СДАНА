import re

max_hex = '0'
count = 0
hex_numbers = []

slov = {
    0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть',
    7: 'семь', 8: 'восемь', 9: 'девять',
    'A': 'десять', 'B': 'одинадцать', 'C': 'двенадцать', 'D': 'тринадцать',
    'E': 'четырнадцать', 'F': 'пятнадцать', '.': 'точка'
}

pattern = re.compile(r'\b(?:[0-9A-Fa-f]+(?:\.[0-9A-Fa-f]*)?|\.[0-9A-Fa-f]+)(?:[Pp][-+]?[0-9]+)?\b')

with open("text.txt", 'r') as file:
    for line in file:
        for match in pattern.finditer(line): # Поиск всех непересекающихся совпадений в шаблоне
            num = match.group() # Взятие всей строки
            if num[0] == '0' and len(num) > 1:
                continue
            try:
                val = float.fromhex(num) # Строка, содержащая шестнадцатеричные числа
                if val <= 1024:
                    hex_numbers.append(num)
                    count += 1
                    if val > float.fromhex(max_hex): # Строка, содержащая шестнадцатеричные числа
                        max_hex = num
            except (TypeError, ValueError):
                pass

# Сортировка последовательности чисел в обратном порядке
hex_numbers.sort(key=float.fromhex, reverse=True)

if max_hex == '0':
    print('В файле нет чисел, удовлетворяющих условию')
else:
    print('\nСписок последовательности по убыванию:', ' '.join(hex_numbers))
    print('Количество:', count)
    print('Максимальное число:', end=' ')
    for char in max_hex:
        for key in slov:
            if str(key) == char.upper():
                print(slov[key], end=' ')
                break

