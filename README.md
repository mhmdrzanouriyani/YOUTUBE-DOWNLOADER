# YouTube Video Downloader with yt-dlp

این پروژه یک اسکریپت ساده برای دانلود ویدیوهای یوتیوب با بهترین کیفیت ویدیو و صوت است، که با استفاده از کتابخانه‌ی **yt-dlp** نوشته شده است.

---

## ویژگی‌ها

- دریافت لینک ویدیو از کاربر
- دانلود بهترین کیفیت ویدیو و صدا به صورت جداگانه و ادغام شده
- ذخیره فایل دانلود شده در مسیر دلخواه با نام و عنوان ویدیو

---

## پیش‌نیازها

- پایتون نسخه 3.6 به بالا
- نصب کتابخانه‌ی yt-dlp

---

## نصب

برای نصب yt-dlp از دستور زیر استفاده کنید:

```bash
pip install yt-dlp
```

---

## نحوه استفاده

1. فایل `download_youtube.py` را با کد زیر ایجاد کنید:

```python
from yt_dlp import YoutubeDL

url = input("Enter Youtube link : ").strip()

ydl_opts = {
    'format' : 'bestvideo+bestaudio',
    'outtmpl' : r'E:\New folder\%(title)s.%(ext)s'
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
```

2. در ترمینال به محل فایل بروید و دستور زیر را اجرا کنید:

```bash
python download_youtube.py
```

3. لینک ویدیوی یوتیوب را وارد کنید و صبر کنید تا دانلود کامل شود.

---

## نکات مهم

- مسیر ذخیره فایل‌ها در قسمت `'outtmpl'` قابل تغییر است.  
- مطمئن شوید پوشه مقصد وجود دارد تا فایل‌ها به درستی ذخیره شوند.

---
موفق باشید

MOHAMMADREZA NOURIYANI 
https://www.instagram.com/MOHIX_CODE/
https://www.youtube.com/@Mohixcode
