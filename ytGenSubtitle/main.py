import argparse
from faster_whisper import WhisperModel
from steps.download_audio import DownloadAudio


parser = argparse.ArgumentParser(
    description='Generate subtitles for a YouTube video.')
parser.add_argument("-vurl",
                    default=None,
                    type=str,
                    help="YouTube video URL",
                    nargs="?")

args = parser.parse_args()
urls = []
if args.vurl:
    urls.append(args.vurl)
else:
    url = input("Enter the YouTube video URL: ")
    urls.append(url)

input_kwargs = {
    "urls": urls
}

steps = [
    DownloadAudio()
]

for step in steps:
    try:
        step.process(input_kwargs)
    except:
        print("Error occurred in step: ", step)
