import numpy as np
import sounddevice as sd
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AudioInput:
  cache_dir: Path

  def capture_stream(self, duration: int, sr: int = 44100, channels: int = 1) -> np.ndarray:
    """
    Capture an audio stream.

    :param duration: Duration of the recording in seconds.
    :param sr: Sample rate (default is 44100 Hz). (wav standard is 44100 Hz, 16-bit, stereo)
    :param channels: Number of audio channels (1 for mono, 2 for stereo, etc.). (mono is cleaner for processing)
    :return: Recorded audio data as a numpy array.
    """
    audio_stream = sd.rec(int(duration * sr), samplerate=sr, channels=channels, dtype='float32')
    sd.wait()
    # If multiple channels, reshape to a 2D array (time, channels)
    if channels > 1:
      audio_stream = audio_stream.reshape(-1, channels)
    return audio_stream

  def __del__(self):
    pass  # sounddevice handles cleanup automatically
