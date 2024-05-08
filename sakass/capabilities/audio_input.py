import sounddevice as sd
import numpy as np


class AudioInput:
  def __init__(self):
    pass

  def capture_audio(self, duration=5, sr=16000):
    audio_data_int = sd.rec(
        int(duration * sr), samplerate=sr, channels=1, dtype='int16')
    sd.wait()  # NOTE: must wait until recording is finished
    audio_stream = audio_data_int.flatten().astype(np.float32) / \
        np.iinfo(np.int16).max
    return audio_stream
