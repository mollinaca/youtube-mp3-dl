#!/usr/bin/env python3

import subprocess
import os
import shutil
import sys


def download(url):
    node_path = shutil.which("node") or os.path.expandvars(
        "$HOME/.local/share/mise/shims/node"
    )

    cmd = [
        sys.executable,
        "-m",
        "yt_dlp",
        "--js-runtime", f"node:{node_path}",
        "--remote-components", "ejs:github",
        "-f", "bestaudio",
        "-x",
        "--audio-format", "mp3",
        "-o", "%(id)s_.mp3",
        url,
    ]

    if os.environ.get("YTDLP_DEBUG"):
        cmd.insert(3, "--verbose")

    return subprocess.run(cmd).returncode


def main():
    # Keep the original interactive usage, while allowing callers to pass a URL.
    url = sys.argv[1] if len(sys.argv) > 1 else input("URL : ").strip()

    if not url:
        print("URL is required.", file=sys.stderr)
        return 2

    return download(url)

if __name__ == '__main__':
    raise SystemExit(main())
