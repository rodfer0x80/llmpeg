from dataclasses import dataclass
from pathlib import Path

import whisper  # TODO: change this to use tinygrad customised whisper example

from llmpeg.utils import curr_date


@dataclass
class STT:
  model_size: str
  cache_dir: Path

  def __post_init__(self):
    self.model = whisper.load_model(self.model_size)  # NOTE: e.g. "tiny"
    self.cache_dir = self.cache_dir / 'stt'
    Path.mkdir(self.cache_dir, exist_ok=True)

  def audio_to_text(self, audio_data: bytes) -> str:
    return self.model.transcribe(audio_data)['text']

  def audio_to_text_file(self, audio_data: bytes, path: Path) -> Path:
    if not path:
      path = self.cache_dir / f'{curr_date()}.txt'
    open(path, 'w').write(self.model.transcribe(audio_data)['text'])
    return path
