<h1 align="center">🎬 YouTube Video Downloader</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/yt--dlp-powered-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/mhmdrzanouriyani/YOUTUBE-DOWNLOADER?style=for-the-badge" />
</p>

<p align="center">
  A clean, cross-platform YouTube video downloader built with Python and yt-dlp.<br>
  Downloads videos in the best available quality and saves them to your Downloads folder automatically.
</p>

---

## ✨ Features

- ✅ Downloads best quality video + audio merged
- ✅ Works on **Windows, Linux, macOS**
- ✅ No hardcoded paths — saves to `~/Downloads/YouTube/` automatically
- ✅ Clean CLI interface
- ✅ Lightweight — just one dependency

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/mhmdrzanouriyani/YOUTUBE-DOWNLOADER.git
cd YOUTUBE-DOWNLOADER
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run it
```bash
python downloader.py
```

### 4. Paste your YouTube URL when prompted
```
==================================================
  🎬 YouTube Downloader - by Mohix Code
==================================================

Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ

📥 Downloading to: /home/user/Downloads/YouTube
✅ Download complete!
```

---

## 📁 Project Structure

```
YOUTUBE-DOWNLOADER/
├── downloader.py       # Main script
├── requirements.txt    # Dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

---

## ⚙️ Requirements

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

---

## 🛠️ Customization

Want to change the download path? Edit this line in `downloader.py`:

```python
path = os.path.join(os.path.expanduser("~"), "Downloads", "YouTube")
```

---

## 📌 Roadmap

- [ ] Add MP3/audio-only download option
- [ ] Add playlist support
- [ ] Add progress bar
- [ ] Build a simple web UI with Flask

---

## 👨‍💻 Author

**Mohammadreza Nouriyani**

[![YouTube](https://img.shields.io/badge/YouTube-Mohix_Code-red?style=flat&logo=youtube)](https://www.youtube.com/@Mohixcode)
[![Instagram](https://img.shields.io/badge/Instagram-mohix_code-purple?style=flat&logo=instagram)](https://www.instagram.com/mohix_code)
[![GitHub](https://img.shields.io/badge/GitHub-mhmdrzanouriyani-black?style=flat&logo=github)](https://github.com/mhmdrzanouriyani)

---

⭐ If this helped you, please give it a star! It keeps me motivated.
