# https://www.youtube.com/watch?v=2UiX4dUUjWc



from pytube import YouTube
import os
from pydub import AudioSegment
path = os.path.dirname(__file__)

'''
yt = YouTube( str(input("Enter the URL of the video you want to download: \n>> ")))
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print(base)
print(new_file)
# result of success
print(yt.title + " has been successfully downloaded.")
print(new_file)
print(type(new_file))

song = AudioSegment.from_file(new_file)


StartMin=0
StartSec=0

EndMin=0
EndSec=30

StartTime=StartMin*60*1000+StartSec*1000
EndTime=EndMin*60*1000+EndSec*1000

extract= song[:10000]
extract.export("ClippedFile.mp3",format="mp3")

'''

def clip (new_file):
    song = AudioSegment.from_file(new_file)
    StartMin=0
    StartSec=0

    EndMin=0
    EndSec=30

    StartTime=StartMin*60*1000+StartSec*1000
    EndTime=EndMin*60*1000+EndSec*1000

    extract= song[:120000]
    extract.export("ClippedFile.mp3",format="mp3")
    return "ClippedFile.mp3"

# clip(r'/home/sidharthroy/Documents/my_project/FINAL/Stop This Train.mp3')

