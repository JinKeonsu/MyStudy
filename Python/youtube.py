'''
pytube를 이용한 다운로드 실습
'''

import pytube
import os
import subprocess

yt = pytube.YouTube("https://www.youtube.com/watch?v=N2rTpglCkaE")
videos = yt.streams.all()

for i in range(len(videos)):
    print(i, ': ', videos[i])

cNum = int(input("다운 받을 화질은(0~21 입력)?"))
savePath = "/Users/jinkeonsu/Downloads"

videos[cNum].download(savePath)

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call([
'ffmpeg', '-i', os.path.join(savePath, oriFileName), os.path.join(savePath, newFileName)
])
