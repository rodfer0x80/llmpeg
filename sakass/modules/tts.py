from TTS.api import TTS as MozillaTTS

import tempfile


class TTS:
  def __init__(self, model_size, lang) -> None:
    self.lang = lang  # NOTE: e.g. "en"
    self.large_tts_model = "tts_models/en/jenny/jenny"
    self.small_tts_model = "tts_models/en/ljspeech/glow-tts"
    model_name = self.large_tts_model if model_size == "large" else self.small_tts_model
    self.speed = 1.3 if model_size == "large" else 2.5
    self.tts = MozillaTTS(model_name=model_name)

  def text_to_audio(self, text: str) -> str:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    self.tts.tts_to_file(text=text, file_path=tmp.name, speed=self.speed)
    return tmp.name
