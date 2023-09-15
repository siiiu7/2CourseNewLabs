'''
Лабораторная работа №8

Требуется для своего варианта второй части л.р. №6 (усложненной программы)
или ее объектно-ориентированной реализации (л.р. №7)
разработать реализацию с использованием графического интерфейса.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.

'''
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

import random

def combination():
    try:
        num_fruits = int(txt.get())
    except ValueError:
        messagebox.showerror('Ошибка', 'Введите число')
        return

    fruits = []

    if num_fruits > 0:
        res_text = f'Количество введённых фруктов: {num_fruits}'
    else:
        messagebox.showerror('Ошибка', 'Фруктов нет в наличии')
        return

    lbl.configure(text=res_text)

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

    # Очистка текстового поля для ввода другого числа фруктов
    result_text.delete('1.0', END)

    # Все возможные комбинации фруктов
    for combination in fruit_combinations:
        total_calories = sum(int(fruit.split(': ')[-1].split(' ')[0]) for fruit in combination)
        result_text.insert(END, ' '.join(combination) + f' ({total_calories} ккал)\n')
        result_text.update()  # Обновление окна вывода

        if total_calories > max_calories:
            max_calories = total_calories
            optimal_combination = combination

    messagebox.showinfo('Cамая калорийная комбинация фруктов', ' '.join(optimal_combination) + f' ({max_calories} ккал)')

    result_text.insert(END, f'\nКОНЕЦ')

window = Tk()
window.title('Лабораторная работа №8')
window.geometry('900x650')

lbl = Label(window, text='Введите количество доступных фруктов', font=('Times', 12))
lbl.place(relx=0.5, rely=0.05, anchor=CENTER)

txt = Entry(window, width=10)
txt.place(relx=0.5, rely=0.1, anchor=CENTER)

btn = Button(window, text='Сгенерировать комбинации', command=combination)
btn.place(relx=0.5, rely=0.15, anchor=CENTER)

result_text = scrolledtext.ScrolledText(window, width=100, height=20)
result_text.place(relx=0.5, rely=0.6, anchor=CENTER)

window.mainloop()
