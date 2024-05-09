from gtts import gTTS

import tempfile


class TTS:
  def __init__(self, lang) -> None:
    self.lang = lang # NOTE: e.g. "en"

  def text_to_audio(self, text: str) -> str:
    tts_file = gTTS(text=text, lang=self.lang, slow=False)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts_file.save(temp_file.name)
    return temp_file.name
