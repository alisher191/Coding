import tkinter as tk
import pytube


win = tk.Tk()
win.minsize(460, 300)
win.resizable(False, False)
win.title('Youtube video saver')


def main():

    global link

    lab = tk.Label(win, text='Путь до видео', font='Times 20')
    lab.grid(row=4, column=0, columnspan=4)
    link = tk.Entry(win, width=50, bd=3)
    link.grid(row=5, column=0, columnspan=4)


def download():

    video = pytube.YouTube(link.get())
    quality = video.streams.get_highest_resolution()
    quality.download()


do = tk.Button(win, text='Save', command=download, width=8, height=4,
               bg='red', fg='black')
do.grid(row=8, column=0, columnspan=5)


if __name__ == '__main__':
    main()
    win.mainloop()
