# TODO: this is all the internal logic for agent
from dataclasses import dataclass
from pathlib import Path

from llmpeg.actions.brain.rational import BrainRational
from llmpeg.actions.brain.trigger import BrainTrigger
from llmpeg.actions.hear import Hear
from llmpeg.actions.speech import Speech
from llmpeg.actions.vision import Vision

from pylogger import LoggerToStdout


@dataclass
class Actions:
  cache_dir: Path
  rational_model: str  # ollama/llama3
  trigger_model: str  # nltk => ollama/gemma:2b
  speech_model_size: str  # tts_models/en/jenny/jenny
  hear_model_size: str  # openai-whisper/base

  def __post_init__(self) -> None:
    self.logger = LoggerToStdout()
    self.rational = BrainRational(self.rational_model)
    self.logger.info('Rational model loaded')
    self.trigger = BrainTrigger(self.trigger_model, self.cache_dir)
    self.logger.info('Trigger model loaded')
    self.hear = Hear(self.speech_model_size, self.cache_dir)
    self.logger.info('Hear model loaded')
    self.speech = Speech(self.hear_model_size, self.cache_dir)
    self.logger.info('Speech model loaded')
    self.vision = Vision(self.cache_dir)
    self.logger.info('Vision model loaded')
