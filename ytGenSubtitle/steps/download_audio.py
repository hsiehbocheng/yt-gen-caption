from steps.step import Step, StepException
from yt_dlp import YoutubeDL


class DownloadAudio(Step):
    def process(self, input_kwargs):
        self.download_audio(input_kwargs['urls'])

    def download_audio(self, urls):
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
                filename = ydl.prepare_filename(info_dict).replace(
                    '.webm', '.mp3').replace('.mp4', '.mp3')
                ydl.download(urls)
        except:
            return StepException("Failed to download audio")
