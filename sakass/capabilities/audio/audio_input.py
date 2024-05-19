import os

import sounddevice as sd
import numpy as np
import soundfile as sf

from sakass.utils import curr_date

class AudioInput:
  def __init__(self, cache_dir: str): self.cache_dir = cache_dir

  def capture_stream(self, duration: int = 5, sr: int = 16000) -> bytes: # np.ndarray
    audio_data_int = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype='int16')
    sd.wait()  # NOTE: must wait until recording is finished
    audio_stream = audio_data_int.flatten().astype(np.float32)
    np.iinfo(np.int16).max
    return audio_stream
  
  def capture_to_file(self, audio_stream: bytes, sr: int = 16000) -> os.PathLike:
    path = os.path.join(self.cache_dir, f"{curr_date()}.wav")
    sf.write(path, audio_stream, samplerate=sr)
    return path
