from pathlib import Path
from dataclasses import dataclass
import site

import torch
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

from llmpeg.utils import curr_date

@dataclass
class TTS:
  model_size: str
  cache_dir: Path
  large_model = 'tts_models/en/jenny/jenny'
  small_model = 'tts_models/en/ljspeech/glow-tts'

  def __post_init__(self) -> None:
    self.cache_dir = self.cache_dir / 'tts'
    Path.mkdir(self.cache_dir, exist_ok=True)

    self.model_name = self.large_model if self.model_size == 'large' else self.small_model
    print(self.model_name)
    self.speed = 1.3 if self.model_size == 'large' else 2.5

    model_config_path = site.getsitepackages()[0]+"/TTS/.models.json"
    model_manager = ModelManager(model_config_path)
    model_path, config_path, model_item = model_manager.download_model(self.model_name)
    voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])
    self.synthesizer = Synthesizer(
        tts_checkpoint=model_path,
        tts_config_path=config_path,
        vocoder_checkpoint=voc_path,
        vocoder_config=voc_config_path
    )

  def synthesize_to_file(self, text: str) -> Path:
    path = self.cache_dir / f'{curr_date()}.wav'
    outputs = self.synthesizer.tts(text)
    self.synthesizer.save_wav(outputs, path)  
    return path

  # def synthesize_to_stream(self, text: str) -> str:
  #   return self.tts.tts(text=text, speed=self.speed)





