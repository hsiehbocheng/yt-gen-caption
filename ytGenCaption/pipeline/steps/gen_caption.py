import pysrt

from .step import Step, StepException
from faster_whisper import WhisperModel


def timestamp_to_seconds(timestamp):
    return timestamp.hours * 3600 + timestamp.minutes * 60 + timestamp.seconds + timestamp.milliseconds / 1000.0


class GenCaption(Step):
    def process(self, input_kwargs, temp_data):
        audio_filename = temp_data.audio_filepath

        if temp_data.caption_filepath:
            captions = pysrt.open(temp_data.caption_filepath)
            all_text = '\n'.join(
                "[%.2fs -> %.2fs] %s" % (
                    timestamp_to_seconds(sub.start),
                    timestamp_to_seconds(sub.end),
                    sub.text.replace('\n', ' ')
                ) for sub in captions
            )
            print(all_text)
        else:
            print("No captions found for this video.\n Use Whisper to generate captions.")
            model = WhisperModel('small')
            segments, _ = model.transcribe(
                audio_filename,
                vad_filter=True,
                temperature=0.001
            )
            caption_filepath = temp_data.audio_filepath.replace('.mp3', '.txt')
            with open(caption_filepath, 'w') as f:
                for segment in segments:
                    # Format the output string for each segment
                    output_text = f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}\n"
                    # Write to file
                    f.write(output_text)
                    # Print to console
                    print(output_text.strip())
