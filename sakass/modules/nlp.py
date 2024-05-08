import nltk

class NLP:
  def __init__(self):
    self.audio_start = ["play"]
    self.audio_check = ["from", "by", "song", "music"]
    nltk.download('punkt')
    pass

  def check_greeting(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    return any(keyword in tokens for keyword in ["hi", "hello", "hey"])
  
  def check_goodbye(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    return any(keyword in tokens for keyword in ["bye", "goodbye"])

  # TODO: find sentiment to play song or not
  def check_audio_request(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    if self.audio_start[0] in tokens and any(keyword in tokens for keyword in self.audio_check):
      return True
    return False
