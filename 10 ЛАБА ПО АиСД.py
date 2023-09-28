from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title('Крестики-нолики')

game_run = True
field = []
cross_count = 0

# Начало игры
def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'azure3'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

# Обработка нажатия по кнопке на поле
def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')

        if game_run and cross_count < 5:
            computer_move()
            check_win('O')

# Проверка начилия победы
def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)
    if cross_count == 5:
        messagebox.showwarning('Ничья', 'Игра закончилась вничью!')
        global game_run
        game_run = False

# Проверка на победу комбинаций из трёх кнопок
def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        global game_run
        game_run = False
        if smb == 'X':
            messagebox.showinfo('Победа', 'Вы победили!')
        elif smb == 'O':
            a1['background'] = a2['background'] = a3['background'] = 'red'
            messagebox.showerror('Поражение', 'Компьютер победил!')

# Проверка, можно ли выиграть, заполнив одну из ячеек
def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

# Ходы компьютера
def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

# Поле для игры
for row in range(3):
    line = []
    for col in range(3):
        button = Button(window, text=' ', width=4, height=2, font=('Verdana', 20, 'bold'), bg='azure3', command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

# Начало новой игры
new_button = Button(window, text='Новая игра', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

# Отображение окна на середине экрана
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))

window.mainloop()
