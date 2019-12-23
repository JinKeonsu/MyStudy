from pytube import YouTube
# from moviepy.editor import *

# download a file from youtube
# youtube_link = 'https://www.youtube.com/watch?v=yourtubevideos'
# w = YouTube(youtube_link).streams.first()
# w.download(output_path="/your/target/directory")

# download a file with only audio, to save space
# if the final goal is to convert to mp3
youtube_link = 'https://www.youtube.com/watch?v=zdj4MiNM4EU'
y = YouTube(youtube_link)
t = y.streams.filter(only_audio=True).all()
t[0].download(output_path="/Users/jks/Project/_MyProjects/Python/download")
