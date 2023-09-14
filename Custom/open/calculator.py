import customtkinter
import tkinter
from tkinter import messagebox


customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.resizable(False, False)
app.geometry('201x176')
app.title('Calculator')

window = customtkinter.CTkEntry(app, width=200, height=35, border_width=3)
window.grid(row=0, column=0, columnspan=4)


def calculate():
    value = window.get()
    if value[-1] in '/+*-':
        value = value+value[:-1]
    window.delete(0, customtkinter.END)
    try:
        window.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Ошибка!", "Нужно вводить только цифры!")
    except ZeroDivisionError:
        messagebox.showinfo("Ошибка!", "На ноль делить нельзя!")


def add_oper(oper):
    value = window.get()
    if value[-1] in '/+-*.':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = window.get()
    window.delete(0, customtkinter.END)
    window.insert(0, value+oper)


def add_digit(digit):
    window.insert('end', digit)


def digit_button(digit):
    return customtkinter.CTkButton(
        master=app, text=digit, command=lambda: add_digit(digit),
        width=50, height=35, border_color='white', border_width=3
    )


def math_button(oper):
    return customtkinter.CTkButton(
        master=app, text=oper, command=lambda: add_oper(oper),
        width=50, height=35, border_color='white', border_width=3, fg_color='orange'
    )


def equal_button(oper):
    return customtkinter.CTkButton(
        master=app, text=oper, command=calculate,
        width=50, height=35, border_color='white', border_width=3, fg_color='green'
    )


digit_button('1').grid(row=1, column=0)
digit_button('2').grid(row=1, column=1)
digit_button('3').grid(row=1, column=2)
digit_button('4').grid(row=2, column=0)
digit_button('5').grid(row=2, column=1)
digit_button('6').grid(row=2, column=2)
digit_button('7').grid(row=3, column=0)
digit_button('8').grid(row=3, column=1)
digit_button('9').grid(row=3, column=2)
digit_button('0').grid(row=4, column=1)

math_button('/').grid(row=1, column=3)
math_button('+').grid(row=2, column=3)
math_button('*').grid(row=3, column=3)
math_button('-').grid(row=4, column=3)


equal_button('=').grid(row=4, column=0)

clear = customtkinter.CTkButton(
    master=app, text='c', command=lambda: window.delete(0, customtkinter.END),
    width=50, height=35, fg_color='black', text_color='white',
    border_width=3, border_color='white'
).grid(row=4, column=2)

app.mainloop()