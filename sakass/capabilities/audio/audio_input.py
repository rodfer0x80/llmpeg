import sounddevice as sd
import numpy as np
import soundfile as sf

import tempfile
import os

class AudioInput:
  def __init__(self, cache_dir: str):
    self.cache_dir = cache_dir

  def capture_audio(self, duration=5, sr=16000):
    audio_data_int = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype='int16')
    sd.wait()  # NOTE: must wait until recording is finished
    audio_stream = audio_data_int.flatten().astype(np.float32)
    np.iinfo(np.int16).max
    return audio_stream

  def save_audio_to_file(self, audio_stream, sr=16000, path=""):
    if not path: path = os.path.join(self.cache_dir, tempfile.NamedTemporaryFile(delete=False, suffix='.wav').name)
    sf.write(path, audio_stream, samplerate=sr)
    return path
