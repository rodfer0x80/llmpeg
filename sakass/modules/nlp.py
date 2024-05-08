class NLP:
  def __init__(self):
    pass

  #TODO: find sentiment to play song or not
  def check_audio_request(self, text: str) -> bool:
    return "play" in text
