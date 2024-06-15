from .step import Step, StepException
from faster_whisper import WhisperModel


class GenCaption(Step):
    def process(self, input_kwargs, temp_data):
        audio_filename = temp_data['audio_filename']

        model = WhisperModel('small')
        segments, _ = model.transcribe(
            audio_filename + '.mp3',
            vad_filter=True,
            temperature=0.001
        )

        for segment in segments:
            print("[%.2fs -> %.2fs] %s" %
                  (segment.start, segment.end, segment.text))
