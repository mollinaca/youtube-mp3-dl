#!/usr/bin/env python3
import sys
from yt_dlp import YoutubeDL

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = None

    if url is None:
        print("URL : ", end="")
        url = input()

    ydl_video_opts = {
        'format': 'bestvideo+bestaudio/best',  # 柔軟な指定
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',  # 動画タイトルに変更
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # 出力を mp4 に
        }],
    }

    with YoutubeDL(ydl_video_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    main()
