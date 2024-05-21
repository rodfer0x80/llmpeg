from pathlib import Path
from dataclasses import dataclass

from TTS.api import TTS as MozillaTTS

from llmpeg.utils import curr_date

@dataclass
class TTS:
  model_size: str
  cache_dir: Path
  large_model = 'tts_models/en/jenny/jenny'
  small_modell = 'tts_models/en/ljspeech/glow-tts'

  def __init__(self, model_size: str, cache_dir: Path) -> None:
    self.cache_dir = cache_dir / 'tts'
    Path.makedirs(self.cache_dir, exist_ok=True)

    self.model_name = self.large_model if model_size == 'large' else self.small_modell
    self.speed = 1.3 if model_size == 'large' else 2.5
    self.tts = MozillaTTS(model_name=self.model_name)

  def synthesize_to_file(self, text: str, path: Path = None) -> Path:
    if not path:
      path = self.cache_dir / f'{curr_date()}.wav'
    self.tts.tts_to_file(text=text, speed=self.speed, file_path=path)
    return path

  # def synthesize_to_stream(self, text: str) -> str:
  #   return self.tts.tts(text=text, speed=self.speed)
