from pathlib import Path

from moviepy import editor
import pytube

video = pytube.YouTube('https://youtu.be/mgu8HeWghlE')
quality = video.streams.get_highest_resolution()
quality.download()

video_file = Path(input())
video = editor.VideoFileClip(f'{video_file}')
video_file = video_file.name.replace(' ', '_').split('.')

audio = video.audio
audio.write_audiofile(f'{video_file[0]}.mp3')
