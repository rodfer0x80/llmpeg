import os
from pathlib import Path
from dataclasses import dataclass

import nltk

from llmpeg.actions.brain.triggerlist import TriggerList


@dataclass
class BrainTrigger:
  model_name: str
  cache_dir: Path

  # TODO: LLM for NLP
  def __post_init__(self):
    self.cache_dir = self.cache_dir / 'triggers'
    Path.mkdir(self.cache_dir, exist_ok=True)
    os.environ['NLTK_DATA'] = str(self.cache_dir / 'nltk_data')
    nltk.download(self.model_name)  # NOTE: e.g. "punkt"

  def check_greeting(self, prompt: str) -> bool:
    return any(keyword in nltk.tokenize.word_tokenize(prompt.lower()) for keyword in TriggerList.greeting)

  def check_goodbye(self, text: str) -> bool:
    return any(keyword in nltk.tokenize.word_tokenize(text.lower()) for keyword in TriggerList.goodbye) or all(
      keyword in nltk.tokenize.word_tokenize(text.lower()) for keyword in TriggerList.goodbye_default_phrase
    )

  def check_browse_request(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    return True if TriggerList.browse_start in tokens and any(keyword in tokens for keyword in TriggerList.browse_check) else False

  def check_explain_request(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    return True if TriggerList.explain_start in tokens and any(keyword in tokens for keyword in TriggerList.explain_check) else False

  # TODO: find sentiment to play song or not
  def check_audio_request(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    return True if TriggerList.audio_start in tokens and any(keyword in tokens for keyword in TriggerList.audio_check) else False
