'''
Лабораторная работа №6
1 часть – написать программу в соответствии со своим вариантом задания.

Вариант 24.
У няни неограниченное количество  фруктов К разных названий (ф1,…фК).
Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю.
'''

while True:
    num_fruits = int(input('Введите количество доступных фруктов: '))

    if num_fruits == 0:
        print('Фруктов нет в наличии')
    else:
        # Список всех фруктов
        fruits = [f'ф{i+1}' for i in range(num_fruits)]

        week_fruits = []
        for _ in range(7):
            day_fruits = fruits.copy()
            week_fruits.append(day_fruits)

        fruit_combinations = []
        for fruit1 in week_fruits[0]:
            for fruit2 in week_fruits[1]:
                for fruit3 in week_fruits[2]:
                    for fruit4 in week_fruits[3]:
                        for fruit5 in week_fruits[4]:
                            for fruit6 in week_fruits[5]:
                                for fruit7 in week_fruits[6]:
                                    combination = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7]
                                    fruit_combinations.append(combination)

        for combination in fruit_combinations:
            print(*combination, sep='-')

        break
