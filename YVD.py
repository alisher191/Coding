import tkinter as tk
import pytube
from tkinter import messagebox
from pathlib import Path
from moviepy import editor

win = tk.Tk()
win.minsize(460, 300)
win.resizable(False, False)
win.title('Youtube video saver')

try:
    def main():
        global link, link2
        lab = tk.Label(win, text='Путь до видео', font='Times 20')
        lab.grid(row=4, column=0, columnspan=4)
        link = tk.Entry(win, width=50, bd=3)
        link.grid(row=5, column=0, columnspan=4)

        # lab2 = tk.Label(win, text='Путь для сохранения аудио:', font='Times 20')
        # lab2.grid(row=6, column=0, columnspan=4)
        # link2 = tk.Entry(win, width=50, bd=3)
        # link2.grid(row=7, column=0, columnspan=4)

    def download():
        # video_file = Path(link.get())

        # video = editor.VideoFileClip(f'{video_file}')
        # video_file = video_file.name.replace(' ', '_').split('.')

        # audio = video.audio
        # audio.write_audiofile(f'/Users/macbook/Desktop/Converted_Audio/{video_file[0]}.mp3')
        video = pytube.YouTube(link.get())
        quality = video.streams.get_highest_resolution()
        quality.download()
       
    do = tk.Button(win, text='Save', command=download, width=8, height=4,
                    bg='red', fg='black')
    do.grid(row=8, column=0, columnspan=5)


except:
    messagebox.showinfo('Error', 'Проверьте корректность введённых данных!')

main()
win.mainloop()