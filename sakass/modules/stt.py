import whisper  # TODO: change this to use tinygrad customised whisper example


class STT:
  def __init__(self, model_size: str):
    self.model = whisper.load_model(model_size) # NOTE: e.g. "tiny"

  def audio_to_text(self, audio_data: bytes) -> str:
    return self.model.transcribe(audio_data)["text"]
