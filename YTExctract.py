# importing packages
#https://www.youtube.com/watch?v=_FrOQC-zEog
# https://www.youtube.com/watch?v=2UiX4dUUjWc stop this train
from pytube import YouTube
import os
path = os.path.dirname(__file__)
import streamlit as st
'''
# url input from user
yt = YouTube(
	str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination =  '.'
# add to above destination if doesnt work str(input(">> ")) or
# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")

'''


def YTDL(abc):
    yt=YouTube(str(abc))
    video = yt.streams.filter(only_audio=True).first()
    destination =  '.'
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    st.write(yt.title + " has been successfully downloaded.")
    st.write(new_file)
    return new_file


