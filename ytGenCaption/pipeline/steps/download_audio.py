from .step import Step, StepException
from yt_dlp import YoutubeDL


class DownloadAudio(Step):
    def process(self, input_kwargs, temp_data):
        urls = input_kwargs['urls']
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': '%(title)s',
            # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
            'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }]
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(urls[0], download=False)
                audio_filename = ydl.prepare_filename(info_dict).replace(
                    '.webm', '.mp3').replace('.mp4', '.mp3')
                ydl.download(urls)
                temp_data['audio_filename'] = audio_filename
        except:
            return StepException("Failed to download audio")
        return temp_data
