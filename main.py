#!/usr/bin/env python3

from yt_dlp import YoutubeDL

def main():
    print ("URL : ", end="")
    url = input()

    ydl_video_opts = {
        'outtmpl': '%(id)s'+'_.mp3',
        'format': 'bestaudio'
    }

    with YoutubeDL(ydl_video_opts) as ydl:
        result = ydl.download(url)

    return

if __name__ == '__main__':
    main()
    exit (0)
