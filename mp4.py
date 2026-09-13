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
        url = input().strip()

    # サイト（YouTube, ABEMA等）を問わず最高画質・音質で取得しMP4で出力する設定
    ydl_video_opts = {
        'format': 'bv*+ba/b',        # 映像・音声をそれぞれ最高画質で取得（無ければ単体ストリーム）
        'merge_output_format': 'mp4', # 結合時のフォーマットをMP4に指定
        'outtmpl': '%(title)s.%(ext)s',
    }

    with YoutubeDL(ydl_video_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    main()