import whisper  # TODO: change this to use tinygrad customised whisper example


class STT:
  def __init__(self, model_size: str):
    self.model = whisper.load_model(model_size)  # NOTE: e.g. "tiny"

  def audio_to_text(self, audio_data: bytes) -> str:
    return self.model.transcribe(audio_data)["text"]

if __name__ == '__main__':
  from pocketsphinx import AudioFile
  from sakass.capabilities.audio_input import AudioInput
  audio_input = AudioInput()
  audio_data = audio_input.capture_audio()
  audio_file = audio_input.save_audio_to_file(audio_data)
  for phrase in AudioFile(audio_file): print(phrase)