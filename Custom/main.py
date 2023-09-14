import tkinter
import customtkinter
import pytube

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("300x220")


def window():
    global link
    lab = customtkinter.CTkLabel(app, text='Ссылка:')
    lab.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    lab2 = customtkinter.CTkLabel(app, text='Video downloader')
    lab2.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    link = customtkinter.CTkEntry(app, width=150, border_width=3)
    link.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


def download():
    video = pytube.YouTube(link.get())
    quality = video.streams.get_highest_resolution()
    quality.download()


button = customtkinter.CTkButton(master=app, text="Download", command=download)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

window()
app.mainloop()

# pyinstaller -D main.py
# pyinstaller -F --noconsole -n downloader main.py
