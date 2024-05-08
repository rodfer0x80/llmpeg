from gtts import gTTS

import tempfile

class TTS:
  def __init__(self) -> None:
    pass

  def text_to_audio(self, text: str) -> str:
    tts_file = gTTS(text=text, lang="en", slow=False)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts_file.save(temp_file.name)
    return temp_file.name