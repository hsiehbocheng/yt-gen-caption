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
parser.add_argument("-model_size_or_path",
                    type=str,
                    default="small",
                    choices=[
                    "tiny", "tiny.en", "base", "base.en",
                    "small", "small.en", "distil-small.en", "medium", "medium.en", "distil-medium.en",
                    "large-v1", "large-v2", "large-v3", "large", "distil-large-v2", "distil-large-v3"],
                    help="""Size of the model to use (tiny, tiny.en, base, base.en,
                        small, small.en, distil-small.en, medium, medium.en, distil-medium.en, large-v1,
                        large-v2, large-v3, large, distil-large-v2 or distil-large-v3), a path to a
                        converted model directory, or a CTranslate2-converted Whisper model ID from the HF Hub.
                        When a size or a model ID is configured, the converted model is downloaded
                        from the Hugging Face Hub.""")
parser.add_argument("-temperatures",
                    default=0.001,
                    type=float,
                    help="Specify the temperature setting for the Whisper model. This float value adjusts the model's randomness during inference.")
parser.add_argument("-initial_prompt",
                    type=str,  # This will accept string input. For Iterable[int], further validation is needed in your script.
                    default='',
                    help="Optional initial prompt for the model. Can be a string or an iterable of integers. Defaults to None if not provided.")

args = parser.parse_args()


input_kwargs = {
    "urls": [args.vurl],
    "model_size_or_path": args.model_size_or_path,
    "temperatures": [args.temperatures],
    "initial_prompt": args.initial_prompt,
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
