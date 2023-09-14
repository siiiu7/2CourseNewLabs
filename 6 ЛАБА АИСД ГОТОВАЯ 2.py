'''
Лабораторная работа №6

2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

Вариант 24.

У няни неограниченное количество  фруктов К разных названий (ф1,…фК).
Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю.
'''

import random

while True:
    num_fruits = int(input('Введите количество разных фруктов: '))
    fruits = []

    if num_fruits == 0:
        print('Фруктов нет в наличии')
    else:
        for i in range(num_fruits):
            fruit_name = f'ф{i+1}'
            fruit_calories = random.randint(20, 100)
            fruit = f'{fruit_name}: {fruit_calories} ккал'
            fruits.append(fruit)

        fruit_combinations = []

        for fruit1 in fruits:
            for fruit2 in fruits:
                for fruit3 in fruits:
                    for fruit4 in fruits:
                        for fruit5 in fruits:
                            for fruit6 in fruits:
                                for fruit7 in fruits:
                                    combination = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7]
                                    fruit_combinations.append(combination)

        max_calories = 0
        optimal_combination = None

        # Все возможные комбинации фруктов
        for combination in fruit_combinations:
            total_calories = sum(int(fruit.split(': ')[-1].split(' ')[0]) for fruit in combination)
            print(' '.join(combination), f'({total_calories} ккал)')

            if total_calories > max_calories:
                max_calories = total_calories
                optimal_combination = combination
        break

print('\nСамая большая по сумме калорийности комбинация:')
print(' '.join(optimal_combination), f'({max_calories} ккал)')
