from pathlib import Path
from dataclasses import dataclass
import site

from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

from llmpeg.types import Date  # TODO: fileIO should be in actions

# TODO: make this in torch


@dataclass
class Speech:
  model_size: str
  cache_dir: Path
  large_model = 'tts_models/en/jenny/jenny'
  small_model = 'tts_models/en/ljspeech/glow-tts'

  def __post_init__(self) -> None:
    self.cache_dir = self.cache_dir / 'tts'
    Path.mkdir(self.cache_dir, exist_ok=True)

    if self.model_size == 'large':
      self.model_name = self.large_model
    else:
      self.model_name = self.small_model
    self.speed = 2.5  # 1.3 for small, 2.5 for large?

    model_config_path = site.getsitepackages()[0] + '/TTS/.models.json'
    model_manager = ModelManager(model_config_path)
    model_path, config_path, model_item = model_manager.download_model(self.model_name)
    voc_path, voc_config_path, _ = model_manager.download_model(model_item['default_vocoder'])
    self.synthesizer = Synthesizer(
      tts_checkpoint=model_path,
      tts_config_path=config_path,
      vocoder_checkpoint=voc_path,
      vocoder_config=voc_config_path,
    )

  # TODO: fileIO should be in actions
  def synthesize_to_file(self, text: str) -> Path:
    path = self.cache_dir / f'{Date.now()}.wav'
    outputs = self.synthesizer.tts(text)
    self.synthesizer.save_wav(outputs, path)
    return path

  # def synthesize_to_stream(self, text: str) -> str:
  #   return self.tts.tts(text=text, speed=self.speed)
