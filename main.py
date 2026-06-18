#!/usr/bin/env python3

import subprocess
import os

def main():
    print("URL : ", end="")
    url = input().strip()

    node_path = os.path.expandvars("$HOME/.local/share/mise/shims/node")

    cmd = [
        "yt-dlp",
        "--js-runtime", f"node:{node_path}",
        "--remote-components", "ejs:github",
        "-f", "bestaudio",
        "-x",
        "--audio-format", "mp3",
        "-o", "%(id)s_.mp3",
        url
    ]

    subprocess.run(cmd)

if __name__ == '__main__':
    main()

