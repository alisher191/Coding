import pytube
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("320x220")


def window():
    global linkw
    label = customtkinter.CTkLabel(app, text="Ссылка:")
    label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    linkw = customtkinter.CTkEntry(app, width=150, border_width=3)
    linkw.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)


def download():
    link = pytube.YouTube(linkw.get())
    quality = link.streams.get_highest_resolution()
    quality.download()


button = customtkinter.CTkButton(app, text="Download", command=download)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


window()
app.mainloop()

# pyinstaller --noconfirm --onefile --windowed --add-data "C:\Users\User\AppData\Local\Programs\Python\Python311\Lib\site-packages\customtkinter;customtkinter/"  "main.py"


