from pocketsphinx import AudioFile  # TODO: change this to use tinygrad customised whisper example

class STT:
  def __init__(self, model_size: str):
    pass

  def audio_to_text(self, audio_file: str) -> str:
    for phrase in AudioFile(audio_file): print(phrase)
    return ""
    # text = ""
    # for phrase in AudioFile(audio_data):
    #   text += phrase
    # return text

