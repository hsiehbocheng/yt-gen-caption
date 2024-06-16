import os
from yt_dlp import YoutubeDL

from .step import Step, StepException
from .settings import DOWNLOAD_DIR


class YT():
    def __init__(self, filename, info_dict):
        self.filename = filename
        self.info_dict = info_dict
        self.audio_filepath = self.get_audio_filepath()
        self.caption_filepath = self.get_caption_filepath()

    def get_audio_filepath(self):
        return self.filename + '.mp3'

    def get_caption_filepath(self):
        if self.info_dict.get('requested_subtitles'):
            ext = list(self.info_dict['requested_subtitles'].keys())[0]
            return self.filename + '.' + ext + '.srt'
        else:
            return None


class DownloadAudio(Step):
    def process(self, input_kwargs, temp_data):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)

        urls = input_kwargs['urls']
        ydl_opts = {
            'format': 'bestaudio',
            'writesubtitles': True,
            'subtitlesformat': 'srt',
            'outtmpl': {
                'default': 'downloads/%(title)s.%(ext)s',
            },

            # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
            'postprocessors': [
                {  # Extract audio using ffmpeg
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                },
                {  # Convert subtitles to srt
                    'key': 'FFmpegSubtitlesConvertor',
                    'format': 'srt'
                }
            ]
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(urls[0], download=False)
                filename = ydl.prepare_filename(info_dict).replace('.webm', '').replace('.mp4', '')
                ydl.download(urls)
                temp_data = YT(filename, info_dict)
        except:
            return StepException("Failed to download audio")
        return temp_data
