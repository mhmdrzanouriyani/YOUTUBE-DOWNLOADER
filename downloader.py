#!/usr/bin/env python3
"""
YouTube Video Downloader
Author: Mohammadreza Nouriyani (@mohix_code)
GitHub: https://github.com/mhmdrzanouriyani
"""

import os
from yt_dlp import YoutubeDL


def get_download_path() -> str:
    """Return a safe default download folder in the user's home directory."""
    path = os.path.join(os.path.expanduser("~"), "Downloads", "YouTube")
    os.makedirs(path, exist_ok=True)
    return path


def download_video(url: str, output_path: str) -> None:
    """Download a YouTube video in best quality to the given path."""
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "quiet": False,
        "noplaylist": True,
    }

    print(f"\n📥 Downloading to: {output_path}\n")
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\n✅ Download complete!")


def main():
    print("=" * 50)
    print("  🎬 YouTube Downloader - by Mohix Code")
    print("=" * 50)

    url = input("\nEnter YouTube URL: ").strip()
    if not url:
        print("❌ No URL provided. Exiting.")
        return

    output_path = get_download_path()
    download_video(url, output_path)


if __name__ == "__main__":
    main()
