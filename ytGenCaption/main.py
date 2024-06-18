import argparse
import os

from pipeline.pipeline import Pipeline
from pipeline.steps.download_audio import DownloadAudio
from pipeline.steps.gen_caption import GenCaption

os.makedirs('downloads', exist_ok=True)

parser = argparse.ArgumentParser(
    description='Generate subtitles for a YouTube video.')
parser.add_argument("-vurl",
                    type=str,
                    help="YouTube video URL")

args = parser.parse_args()


input_kwargs = {
    "urls": [args.vurl]
}


def main():
    steps = [
        DownloadAudio(),
        GenCaption(),
    ]
    pipeline = Pipeline(steps)
    pipeline.run(input_kwargs=input_kwargs)


if __name__ == '__main__':
    main()
