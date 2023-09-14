import tkinter as tk
import pytube
from pathlib import Path
from moviepy import editor

"""
Install Certificates.command
Update Shell Profile.command
"""


win = tk.Tk()
win.title('Video Saver')


def main():
    global link, place
    lab = tk.Label(win, text='Путь до видео:',
                   font='Times 20')
    lab.grid(row=0, column=0)
    link = tk.Entry(win, width=35)
    link.grid(row=2, column=0)

    # lab2 = tk.Label(win, text='Путь для сохранения:',
    #                font='Times 20')
    # lab2.grid(row=5, column=0)
    # place = tk.Entry(win, width=35)
    # place.grid(row=7, column=0)


def converter():
    # video = pytube.YouTube(link.get())
    # quality = video.streams.get_highest_resolution()
    # quality.download('/Users/macbook/Desktop/Converted_Audio')
    video_file = Path(link.get())

    video = editor.VideoFileClip(f'{video_file}')
    video_file = video_file.name.replace(' ', '_').split('.')

    audio = video.audio
    audio.write_audiofile(f'/Users/macbook/Desktop/Converted_Audio/{video_file[0]}.mp3')


do = tk.Button(win, text='Конвертировать', command=converter)
do.grid(row=8, column=0)

main()
win.mainloop()

