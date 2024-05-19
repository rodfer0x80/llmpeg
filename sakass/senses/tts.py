import os

from TTS.api import TTS as MozillaTTS

from sakass.utils import curr_date

class TTS:
  LARGE_MODEL = "tts_models/en/jenny/jenny"
  SMALL_MODEL = "tts_models/en/ljspeech/glow-tts"
  def __init__(self, model_size: str, cache_dir: os.PathLike) -> None:
    self.cache_dir = cache_dir
    self.model_name = self.LARGE_MODEL if model_size == "large" else self.SMALL_MODEL
    self.speed = 1.3 if model_size == "large" else 2.5
    self.tts = MozillaTTS(model_name=self.model_name)
    
  def synthesize_to_file(self, text: str) -> os.PathLike:
    path = os.path.join(self.cache_dir, f"{curr_date()}.wav")
    self.tts.tts_to_file(text=text, speed=self.speed, file_path=path)
    return path
  
  # def synthesize_to_stream(self, text: str) -> str: return self.tts.tts(text=text, speed=self.speed)
