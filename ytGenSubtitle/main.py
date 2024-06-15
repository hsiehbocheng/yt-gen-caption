import argparse
from faster_whisper import WhisperModel
from pipeline.steps.download_audio import DownloadAudio
from pipeline.pipeline import Pipeline


parser = argparse.ArgumentParser(
    description='Generate subtitles for a YouTube video.')
parser.add_argument("vurl",
                    type=str,
                    help="YouTube video URL")

args = parser.parse_args()


input_kwargs = {
    "urls": [args.vurl]
}


def main():
    steps = [
        DownloadAudio()
    ]
    pipeline = Pipeline(steps)
    pipeline.run(input_kwargs)


if __name__ == '__main__':
    main()
