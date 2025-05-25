from yt_dlp import YoutubeDL

url = input("Enter Youtube link : ").strip()

ydl_opts = {
    'format' : 'bestvideo+bestaudio' , 
    'outtmpl' : r'E:\New folder\%(title)s.%(ext)s'
}

with YoutubeDL(ydl_opts) as ydl :
    ydl.download([url])

    