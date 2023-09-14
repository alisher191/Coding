import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    window.insert('end', digit)


def make_button(digit):
    return tk.Button(text=digit, command=lambda: add_digit(digit))


def calculate():
    value = window.get()
    if value[-1] in '/*+-':
        value = value[:-1]
    window.delete(0, tk.END)
    try:
        window.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Ошибка!", "Нужно вводить цифры!")
    except ZeroDivisionError:
        messagebox.showinfo('Ошибка', "На ноль делить нельзя!")


def calc_button(oper):
    return tk.Button(text=oper, command=calculate)


def add_oper(oper):
    value = window.get()
    if value[-1] in '/*+-.':
        value = value[:-1]
    elif '+' in value or "-" in value or '*' in value or '/' in value:
        calculate()
        value = window.get()
    window.delete(0, tk.END)
    window.insert(0, value + oper)


def make_op_button(oper):
    return tk.Button(text=oper, command=lambda: add_oper(oper))


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '/+-*.':
        add_oper(event.char)
    elif event.char == '\r':
        calculate()


win = tk.Tk()
# win['bg'] = '#7BC4A7'
# win.resizable(False, False)
win.minsize(220, 240)
win.maxsize(500, 600)
win.title("Калькулятор")
win.bind("<Key>", press_key)

# label1 = tk.Label(win, text='Hello!')
# label1.grid(row=0, column=0)

window = tk.Entry(win, justify=tk.RIGHT)
window.grid(row=0, column=0, columnspan=4)

make_button('1').grid(row=1, column=0, sticky='wens')
make_button('2').grid(row=1, column=1, sticky='wens')
make_button('3').grid(row=1, column=2, sticky='wens')
make_button('4').grid(row=2, column=0, sticky='wens')
make_button('5').grid(row=2, column=1, sticky='wens')
make_button('6').grid(row=2, column=2, sticky='wens')
make_button('7').grid(row=3, column=0, sticky='wens')
make_button('8').grid(row=3, column=1, sticky='wens')
make_button('9').grid(row=3, column=2, sticky='wens')
make_button('0').grid(row=4, column=0, sticky='wens')

make_op_button('/').grid(row=1, column=3, sticky='wens')
make_op_button('*').grid(row=2, column=3, sticky='wens')
make_op_button('-').grid(row=3, column=3, sticky='wens')
make_op_button('+').grid(row=4, column=3, sticky='wens')

calc_button('=').grid(row=4, column=2, sticky='wens')

delete = tk.Button(text='c', command=lambda: window.delete(len(window.get()) - 1))
delete.grid(row=4, column=1, sticky='wens')

clear = tk.Button(text='Очистить', command=lambda: window.delete(0, tk.END))
clear.grid(row=5, column=0, columnspan=4, sticky='wens')

win.mainloop()
