from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Лабораторная работа № 9')
window.config(bg='azure3')
window.resizable(width=False, height=False)

f = ('Times', 14)

# Открытие нового окна
def open_welcome_window():
    name_value = name.get()
    password_value = password.get()

    if not name_value or not password_value:
        messagebox.showinfo('Ошибка', 'Пожалуйста, заполните все поля')
        return

    welcome_window = Toplevel(window)
    welcome_window.title('Успешная регистрация')
    welcome_window.config(bg='azure3')

    welcome_label = Label(welcome_window, text=f'Добро пожаловать, {name_value}!', font=f, bg='azure3')
    welcome_label.pack(pady=50)

    # Вычисление позиции окна по середине экрана
    window_width = welcome_window.winfo_width()
    window_height = welcome_window.winfo_height()
    screen_width = welcome_window.winfo_screenwidth()
    screen_height = welcome_window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    welcome_window.geometry(f'+{x_coordinate}+{y_coordinate}')

    welcome_window.transient(window)
    welcome_window.grab_set()
    window.wait_window(welcome_window)

# Закрытие окна
def on_close():
    if messagebox.askokcancel('Выход', 'Действительно хотите закрыть приложение?'):
        window.destroy()

window.protocol('WM_DELETE_WINDOW', on_close)

# Обработчик для флажка
def toggle_password():
    if show_password_var.get():
        password.config(show='')
    else:
        password.config(show='*')

left_frame = Frame(window, bd=2, bg='azure3', relief=SOLID, padx=10, pady=10)

Label(left_frame, text="Введите логин", bg='azure3', font=f).grid(row=0, column=0, sticky=W, pady=10)
Label(left_frame, text="Введите пароль", bg='azure3', font=f).grid(row=1, column=0, pady=10)

name = Entry(left_frame, font=f)
password = Entry(left_frame, font=f, show='*')

name.grid(row=0, column=1, pady=10, padx=20)
password.grid(row=1, column=1, pady=10, padx=20)

show_password_var = BooleanVar()
show_password_checkbox = Checkbutton(left_frame, text="Показать пароль", variable=show_password_var, bg='azure3', font=f, command=toggle_password)
show_password_checkbox.grid(row=2, columnspan=2, pady=10, padx=20)

login_btn = Button(left_frame, width=15, text='Войти', font=f, relief=SOLID, cursor='hand2', command=open_welcome_window)
login_btn.grid(row=3, columnspan=2, pady=10)

left_frame.pack()

# Вычисление позиции окна по середине экрана
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

window.geometry(f'+{x_coordinate}+{y_coordinate}')

window.mainloop()
