from pathlib import Path
from dataclasses import dataclass

import sounddevice as sd
import numpy as np
import soundfile as sf


@dataclass
class AudioInput:
  cache_dir: Path

  def capture_stream(self, duration: int = 5, sr: int = 16000) -> np.float32:
    audio_data_int = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype='int16')
    sd.wait()  # NOTE: must wait until recording is finished
    audio_stream = audio_data_int.flatten().astype(np.float32)
    np.iinfo(np.int16).max
    return audio_stream

  def write_audio_stream_to_file(self, audio_stream: bytes, path: Path, sr: int = 16000):
    sf.write(path, audio_stream, samplerate=sr)
