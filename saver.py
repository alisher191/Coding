import tkinter as tk
import pytube

root = tk.Tk()
root.geometry('465x300')
root.resizable(width=False, height=False)
root.title("Save video from Youtube")


try:
    def main():
        global link, place
        lab = tk.Label(root, text='Ссылка для скачивания: ', font='Times 20')
        lab.grid(row=4, column=0, columnspan=4)
        link = tk.Entry(root, width=50, bd=3)
        link.grid(row=5, column=0, columnspan=4)

        labe = tk.Label(root, text='Место для сохранения: ', font='Times 20')
        labe.grid(row=6, column=3)
        place = tk.Entry(root, width=50, bd=3)
        place.grid(row=7, column=3)

        def download():
            yt = pytube.YouTube(link.get())
            stream = yt.streams.get_highest_resolution()
            stream.download(place.get())

        download = tk.Button(root, text="Скачать", width=10, height=3, command=download,
                          bg='green', fg='black')
        download.grid(row=8, column=0, columnspan=5)
except:
    exlab = tk.Label(root, text='Извините произошла ошибка', font='Times 24')
    exlab.grid(row=9, column=3)

main()
root.mainloop()
