import tkinter as tk
from tkinter import messagebox


def calculate():
    value = window.get()
    if value[-1] in '/+-*':
        value = value+value[:-1]
    window.delete(0, tk.END)
    try:
        window.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Error", 'Нужно вводить только цифры!')
    except ZeroDivisionError:
        messagebox.showinfo('Error', 'На ноль делить нельзя!')


def add_digit(digit):
    window.insert('end', digit)


def add_op(op):
    value = window.get()
    if value[-1] in '/+-*.':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = window.get()
    window.delete(0, tk.END)
    window.insert(0, value+op)


def make_digit_button(digit):
    return tk.Button(text=digit, command=lambda: add_digit(digit))


def make_oper_button(op):
    return tk.Button(text=op, command=lambda: add_op(op))


def make_calc_button(op):
    return tk.Button(text=op, command=calculate)


win = tk.Tk()
win.title('Калькулятор')
# win.resizable(False, False)
# win['bg'] = 'white'
# win.minsize(240, 280)
# win.maxsize(400, 480)
window = tk.Entry(win, justify=tk.RIGHT)
window.grid(row=0, column=0, columnspan=4)

make_digit_button('1').grid(row=1, column=0, sticky='wens')
make_digit_button('2').grid(row=1, column=1, sticky='wens')
make_digit_button('3').grid(row=1, column=2, sticky='wens')
make_digit_button('4').grid(row=2, column=0, sticky='wens')
make_digit_button('5').grid(row=2, column=1, sticky='wens')
make_digit_button('6').grid(row=2, column=2, sticky='wens')
make_digit_button('7').grid(row=3, column=0, sticky='wens')
make_digit_button('8').grid(row=3, column=1, sticky='wens')
make_digit_button('9').grid(row=3, column=2, sticky='wens')
make_digit_button('0').grid(row=4, column=1, sticky='wens')

make_oper_button('/').grid(row=1, column=3, sticky='wens')
make_oper_button('+').grid(row=2, column=3, sticky='wens')
make_oper_button('*').grid(row=3, column=3, sticky='wens')
make_oper_button('-').grid(row=4, column=3, sticky='wens')

# make_oper_button('.').grid(row=4, column=2, sticky='wens')

make_calc_button('=').grid(row=4, column=0, sticky='wens')
clear = tk.Button(text='c', command=lambda: window.delete(0, tk.END))
clear.grid(row=4, column=2, sticky='wens')

win.mainloop()
