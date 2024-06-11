from pathlib import Path
from dataclasses import dataclass
from typing import Union
from io import BytesIO

import numpy as np

from llmpeg.capabilities.audio.audio_input import AudioInput
from llmpeg.capabilities.audio.audio_output import AudioOutput
from llmpeg.capabilities.filesystem import WaveFile
from llmpeg.types import Date, URL, Error


@dataclass
class Audio:
  cache_dir: Path

  def __post_init__(self):
    self.cache_dir = self.cache_dir / 'audio'
    self.audio_input = AudioInput(cache_dir=self.cache_dir)
    self.audio_output = AudioOutput(cache_dir=self.cache_dir)

  def capture_stream(self, duration: int):
    return self.audio_input.capture_stream(duration)

  def capture_to_file(self, duration: int = 5) -> Path:
    audio_stream = self.capture_stream(duration)
    # Convert to wav format
    audio_stream = np.frombuffer(audio_stream, dtype=np.int16)
    audio_file = self.cache_dir / f'{Date.now()}.wav'
    WaveFile.write(audio_stream, audio_file, sr=44100)
    return audio_file

  def play_audio_stream(self, audio_stream: Union[bytes, np.float32]) -> None:
    self.audio_output.play([self.process_track(audio_stream)])

  def play_remote_audio_stream_url(self, url: str) -> None:
    self.audio_output.play([self.process_track(URL(url))])

  def play_audio_file(self, audio_file: Path) -> None:
    self.audio_output.play([self.process_track(audio_file)])

  def play(self, tracks: list[Union[str, Path, bytes, np.float32]]) -> None:
    self.audio_output.play([self.process_track(track) for track in tracks])

  def stop(self):
    self.audio_output.stop()

  def process_track(self, track: Union[URL, Path, bytes, np.float32]) -> bytes:
    if isinstance(track, (str, Path)):
      _, data = WaveFile.read(track)
    elif isinstance(track, bytes):
      _, data = WaveFile.read(BytesIO(track))
    elif isinstance(track, np.ndarray):
      _ = 44100  # Assuming sample rate of 44100 Hz
      data = (track * np.iinfo(np.int16).max).astype(np.int16)
    elif isinstance(track, np.float32):
      _ = 44100
    else:
      err = Error('Unsupported audio format').__repr__()
      raise ValueError(err)
    return data.tobytes()
