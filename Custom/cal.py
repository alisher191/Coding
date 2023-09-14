import customtkinter
import tkinter as tk
from tkinter import messagebox

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
# app.resizable(False, False)
app.geometry('201x176')
app.title("Calculator")

linkw = customtkinter.CTkEntry(app, width=200, height=35, border_width=3)
linkw.grid(row=0, column=0, columnspan=4)


def calculate():
    value = linkw.get()
    if value[-1] in '/+-*':
        value = value+value[:-1]
    linkw.delete(0, customtkinter.END)
    try:
        linkw.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Error", 'Нужно вводить только цифры!')
    except ZeroDivisionError:
        messagebox.showinfo('Error', 'На ноль делить нельзя!')


def add_digit(digit):
    linkw.insert('end', digit)


def add_op(op):
    value = linkw.get()
    if value[-1] in '/+-*.':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = linkw.get()
    linkw.delete(0, customtkinter.END)
    linkw.insert(0, value+op)


def make_digit_button(digit):
    return customtkinter.CTkButton(master=app, text=digit, 
                                   command=lambda: add_digit(digit), 
                                   width=50, height=35,
                                   border_width=3, border_color='white')


def make_oper_button(op):
    return customtkinter.CTkButton(master=app, text=op, command=lambda: add_op(op), 
                                   width=50, height=35,
                                   fg_color='green',
                                   border_width=3, border_color='white')


def make_calc_button(op):
    return customtkinter.CTkButton(master=app, text=op, 
                                   command=calculate, width=50, 
                                   fg_color='red', height=35,
                                   border_width=3, border_color='white')


make_digit_button('1').grid(row=1, column=0)
make_digit_button('2').grid(row=1, column=1)
make_digit_button('3').grid(row=1, column=2)
make_digit_button('4').grid(row=2, column=0)
make_digit_button('5').grid(row=2, column=1)
make_digit_button('6').grid(row=2, column=2)
make_digit_button('7').grid(row=3, column=0)
make_digit_button('8').grid(row=3, column=1)
make_digit_button('9').grid(row=3, column=2)
make_digit_button('0').grid(row=4, column=1)


make_oper_button('/').grid(row=1, column=3)
make_oper_button('+').grid(row=2, column=3)
make_oper_button('*').grid(row=3, column=3)
make_oper_button('-').grid(row=4, column=3)


make_calc_button('=').grid(row=4, column=0)
clear = customtkinter.CTkButton(master=app, text='c', 
                                command=lambda: linkw.delete(0, customtkinter.END), 
                                width=50, height=35,
                                fg_color='black', text_color='white',
                                border_width=3, border_color='white')
clear.grid(row=4, column=2)


app.mainloop()
