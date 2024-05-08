import nltk


class NLP:
  def __init__(self):
    self.audio_start = ["play"]
    self.audio_check = ["from", "by", "song", "music"]
    nltk.download('punkt')
    pass

  # TODO: find sentiment to play song or not
  def check_audio_request(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    if self.audio_start[0] in tokens and any(keyword in tokens for keyword in self.audio_check):
      return True
    return False
