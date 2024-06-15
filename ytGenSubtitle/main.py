from yt_dlp import YoutubeDL
from faster_whisper import WhisperModel

urls = ['https://www.youtube.com/watch?v=4kzl1b5hsgg']
ydl_opts = {
    'format': 'bestaudio',
    'outtmpl': '%(title)s',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

with YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(urls[0], download=False)
    filename = ydl.prepare_filename(info_dict).replace('.webm', '.mp3').replace('.mp4', '.mp3')
    ydl.download(urls)