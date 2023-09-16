'''
Лабораторная работа №7
Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода.

Вариант 24.
У няни неограниченное количество  фруктов К разных названий (ф1,…фК).
Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю.
'''
import random

class FruitCombinationFinder:
    def __init__(self):
        self.fruits = []
        self.fruit_combinations = []
        self.max_calories = 0
        self.optimal_combination = None

    def generate_fruits(self, num_fruits):
        if num_fruits == 0:
            print('Фруктов нет в наличии')
        else:
            for i in range(num_fruits):
                fruit_name = f'ф{i+1}'
                fruit_calories = random.randint(20, 100)
                fruit = f'{fruit_name}: {fruit_calories} ккал'
                self.fruits.append(fruit)

    def generate_combinations(self):
        for fruit1 in self.fruits:
            for fruit2 in self.fruits:
                for fruit3 in self.fruits:
                    for fruit4 in self.fruits:
                        for fruit5 in self.fruits:
                            for fruit6 in self.fruits:
                                for fruit7 in self.fruits:
                                    combination = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7]
                                    self.fruit_combinations.append(combination)

    def find_optimal_combination(self):
        for combination in self.fruit_combinations:
            total_calories = sum(int(fruit.split(': ')[-1].split(' ')[0]) for fruit in combination)
            print(' '.join(combination), f'({total_calories} ккал)')

            if total_calories > self.max_calories:
                self.max_calories = total_calories
                self.optimal_combination = combination

    def print_optimal_combination(self):
        while True:
            if self.optimal_combination is not None:
                print('\nСамая большая по сумме калорийности комбинация:')
                print(' '.join(self.optimal_combination), f'({self.max_calories} ккал)')
            else:
                print('Комбинаций не найдено')
            break

    def find_optimal_fruit_combination(self):
        num_fruits = int(input('Введите количество разных фруктов: '))
        self.generate_fruits(num_fruits)
        self.generate_combinations()
        self.find_optimal_combination()

finder = FruitCombinationFinder()
finder.find_optimal_fruit_combination()
finder.print_optimal_combination()
