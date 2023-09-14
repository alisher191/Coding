import pytube


video = pytube.YouTube('https://www.youtube.com/watch?v=smqhSl0u_sI&list=RDsmqhSl0u_sI&start_radio=1')
a = video.streams.get_highest_resolution()
name = a.title
a.download()

