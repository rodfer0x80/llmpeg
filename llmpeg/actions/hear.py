from dataclasses import dataclass
from pathlib import Path

import whisper  # TODO: change this to use tinygrad customised whisper example

from llmpeg.utils import CurrentDate


@dataclass
class Hear:
        model_size: str
        cache_dir: Path

        def __post_init__(self):
                # NOTE: e.g. "tiny"
                self.model = whisper.load_model(self.model_size)
                self.cache_dir = self.cache_dir / 'stt'
                Path.mkdir(self.cache_dir, exist_ok=True)

        def synthesize_to_stream(self, audio_data: bytes) -> str:
                return self.model.transcribe(audio_data)['text']

        def synthesize_to_file(self, audio_data: bytes, path: Path) -> Path:
                path = self.cache_dir / f'{CurrentDate()}.txt'
                open(path, 'w').write(self.model.transcribe(audio_data)['text'])
                return path
