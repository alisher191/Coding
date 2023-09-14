from pathlib import Path
from moviepy import editor

video_file = Path('Kendrick Lamar - Money Trees (Feat Jay Rock).mp4')

video = editor.VideoFileClip(f'{video_file}')
video_file = video_file.name.replace(' ', '_').split('.')

audio = video.audio
audio.write_audiofile(f'{video_file[0]}.mp3')

