import pysrt

from .step import Step, StepException
from faster_whisper import WhisperModel


def timestamp_to_seconds(timestamp):
    return timestamp.hours * 3600 + timestamp.minutes * 60 + timestamp.seconds + timestamp.milliseconds / 1000.0
def seconds_to_srt_time(seconds):
    """Convert seconds to SubRipTime format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds - int(seconds)) * 1000)
    return pysrt.SubRipTime(hours, minutes, seconds, milliseconds)

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
            
            caption_filepath = temp_data.audio_filepath.replace('.mp3', '.srt')
            subtitles = pysrt.SubRipFile()
            for i, segment in enumerate(segments, start=1):
                start_time = seconds_to_srt_time(segment.start)
                end_time = seconds_to_srt_time(segment.end)
                subtitle = pysrt.SubRipItem(index=i, start=start_time, end=end_time, text=segment.text)
                
                # Add subtitle to the list
                subtitles.append(subtitle)

                # Optional: print subtitle
                print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

            # Save subtitles to file
            subtitles.save(caption_filepath, encoding='utf-8')
