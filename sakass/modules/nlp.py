import nltk

from sakass.modules.patterns import Triggers


class NLP:
  def __init__(self, wordlist: str):
    nltk.download(wordlist) #NOTE: e.g. "punkt"

  def check_greeting(self, prompt: str) -> bool:
    return any(keyword in nltk.tokenize.word_tokenize(prompt.lower()) for keyword in Triggers.greeting)

  def check_goodbye(self, text: str) -> bool:
    return any(keyword in nltk.tokenize.word_tokenize(text.lower()) for keyword in Triggers.goodbye)

  # TODO: find sentiment to play song or not
  def check_audio_request(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    if Triggers.audio_start in tokens and any(keyword in tokens for keyword in Triggers.audio_check):
      return True
    return False
