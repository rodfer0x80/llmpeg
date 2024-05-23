from pathlib import Path
from dataclasses import dataclass
from typing import Union

import numpy as np

from llmpeg.capabilities.audio.audio_input import AudioInput
from llmpeg.capabilities.audio.audio_output import AudioOutput
from llmpeg.utils import CurrentDate


@dataclass
class Audio:
  cache_dir: Path
  audio_output_src: str

  def __post_init__(self):
    self.cache_dir = self.cache_dir / 'audio'
    self.audio_input = AudioInput(cache_dir=self.cache_dir)
    self.audio_output = AudioOutput(audio_output_src=self.audio_output_src, cache_dir=self.cache_dir)

  def capture_stream(self, duration: int = 5):
    return self.audio_input.capture_stream(duration)

  def capture_to_file(self, path: Path = None):
    if not path:
      path = self.cache_dir / f'{CurrentDate()}.wav'
    return self.audio_input.write_audio_stream_to_file(self.capture_stream(), path)

  def play_audio_stream(self, audio_stream: Union[bytes, np.float32]) -> None:
    self.audio_output.play([audio_stream])

  def play_remote_audio_stream_url(self, url: str) -> None:
    self.audio_output.play([url])

  def play_audio_file(self, audio_file: Path) -> None:
    self.audio_output.play([audio_file])

  def play(self, tracks) -> None:
    self.audio_output.play(tracks)

  def stop(self):
    self.audio_output.stop()
