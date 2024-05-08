import sounddevice as sd
import numpy as np
import whisper  #TODO: change this to use tinygrad customised whisper example


class AudioInput:
  def __init__(self):
    model_size = "tiny"
    self.model = whisper.load_model(model_size)

  def capture_audio(self, duration=5, sr=16000):
    print("Recording...")
    audio_data_int = sd.rec(
        int(duration * sr), samplerate=sr, channels=1, dtype='int16')
    sd.wait()  #NOTE: must wait until recording is finished
    print("Finished recording...")
    audio_stream = audio_data_int.flatten().astype(np.float32) / \
        np.iinfo(np.int16).max
    return audio_stream

  #TODO: this tts part should go to modules/stt where stuff is fronted from this class into agent class
  def speech_to_text(self) -> str:
    audio_stream = self.capture_audio()
    audio_text = self.model.transcribe(audio_stream)["text"]
    return audio_text
