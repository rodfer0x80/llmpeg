import time
import threading
import queue
from dataclasses import dataclass
from typing import Union
from pathlib import Path

import numpy as np
import sounddevice as sd

from llmpeg.types import Error


@dataclass
class AudioOutput:
  cache_dir: Path

  def __post_init__(self) -> None:
    self.playing = False
    self.thread = None
    self.stop_event = threading.Event()
    self.queue = queue.Queue()

  def _play_audio(self, audio: Union[bytes, np.float32]) -> None:
    self.playing = True

    if isinstance(audio, bytes):
      # Assuming the byte data is int16 format (wav), convert to numpy array
      audio = np.frombuffer(audio, dtype=np.int16)
    # Ensure the audio is in float32 format for sounddevice
    if audio.dtype != np.float32:
      audio = audio.astype(np.float32)
    # Default sample rate of 44.1kHz is good enough for most audio recordings
    sd.play(audio, samplerate=44100, blocking=True)
    self.playing = False

  def stop(self) -> None:
    self.stop_event.set()
    with self.queue.mutex:
      self.queue.queue.clear()

  def play(self, tracks: list[Union[bytes, np.float32]]) -> None:
    self.stop()
    self.stop_event.clear()
    self.playing = True
    for track in tracks:
      if track:
        self.queue.put(track)
    self.thread = threading.Thread(target=self._play_from_queue)
    self.thread.start()

  def _play(self) -> None:
    if not self.queue.empty():
      track = self.queue.get()
      try:
        self._play_audio(track)
      except Exception as e:
        raise Exception(Error(e).__repr__())
    else:
      # Sleep for a short duration to avoid busy waiting
      time.sleep(0.1)

  def _play_from_queue(self) -> None:
    while not self.stop_event.is_set():
      self._play()
