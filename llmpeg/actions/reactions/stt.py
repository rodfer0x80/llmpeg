import os
import tempfile

import whisper  # TODO: change this to use tinygrad customised whisper example

class STT:
  def __init__(self, model_size: str, cache_dir: os):
    self.model = whisper.load_model(model_size)  # NOTE: e.g. "tiny"
    self.cache_dir = cache_dir

  def audio_to_text(self, audio_data: bytes) -> str: return self.model.transcribe(audio_data)["text"]
  
  def audio_to_text_file(self, audio_data: bytes, path: str) -> str:
    if not path: path = os.path.join(self.cache_dir, tempfile.NamedTemporaryFile(delete=False, suffix='.txt').name)
    text = self.model.transcribe(audio_data)["text"]
    with open(path, "w") as f: f.write(text)
    return path
