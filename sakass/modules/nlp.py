import nltk

from sakass.modules.patterns import Triggers

class NLP:
  def __init__(self):
    nltk.download('punkt')

  def check_greeting(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    return any(keyword in tokens for keyword in Triggers.greeting)

  def check_goodbye(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    return any(keyword in tokens for keyword in Triggers.goodbye)

  # TODO: find sentiment to play song or not
  def check_audio_request(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    if Triggers.audio_start in tokens and any(keyword in tokens for keyword in Triggers.audio_check):
      return True
    return False
