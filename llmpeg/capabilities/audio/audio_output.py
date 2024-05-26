import time
from io import BytesIO
import threading
from queue import Queue
from typing import Union
from pathlib import Path
import sounddevice as sd
import numpy as np

from llmpeg.utils import WaveFile, Error


class AudioOutput:
        def __init__(self, audio_output_src: str, cache_dir: Path) -> None:
                self.audio_output_src = audio_output_src
                self.cache_dir = cache_dir
                self.playing = False
                self.thread = None
                self.stop_event = threading.Event()
                self.queue = Queue()

        def _play_audio(self, track: Union[str, Path, bytes, np.float32]) -> None:
                if isinstance(track, (str, Path)):
                        fs, data = WaveFile.read(track)
                elif isinstance(track, bytes):
                        fs, data = WaveFile.read(BytesIO(track))
                elif isinstance(track, np.ndarray):
                        fs = 44100  # Assuming sample rate of 44100 Hz
                        data = (track * np.iinfo(np.int16).max).astype(np.int16)
                else:
                        raise ValueError(Error('Unsupported audio format').__repr__())
                self.playing = True
                sd.play(data, fs, blocking=True)
                self.playing = False

        def stop(self) -> None:
                self.stop_event.set()
                self.queue.queue.clear()

        def play(self, tracks: list[Union[str, Path, bytes, np.float32]]) -> None:
                self.stop()
                self.stop_event.clear()
                self.playing = True
                for track in tracks:
                        if track:
                                self.queue.put(track)
                self.thread = threading.Thread(target=self._play_from_queue)
                self.thread.start()

        def _play_from_queue(self) -> None:
                while not self.stop_event.is_set():
                        if not self.queue.empty():
                                track = self.queue.get()
                                try:
                                        self._play_audio(track)
                                except Exception as e:
                                        print(f'[ERROR]: {Error(e).__repr__()}')
                        else:
                                time.sleep(0.1)
