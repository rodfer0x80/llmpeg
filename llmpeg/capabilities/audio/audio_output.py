import time
import threading
import queue
from typing import Union
from pathlib import Path
from io import BytesIO

import numpy as np
import pyaudio

from llmpeg.utils import WaveFile, Error


class AudioOutput:
    cache_dir: Path

    def __post_init__(self) -> None:
        self.playing = False
        self.thread = None
        self.stop_event = threading.Event()
        self.queue = queue.Queue()
        self.pa = pyaudio.PyAudio()

    def _play_audio(self, track: Union[str, Path, bytes, np.float32]) -> None:
        # 16-bit signed integer format
        stream = self.pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            output=True,
        )

        if isinstance(track, (str, Path)):
            _, data = WaveFile.read(track)
        elif isinstance(track, bytes):
            _, data = WaveFile.read(BytesIO(track))
        elif isinstance(track, np.ndarray):
            _ = 44100  # Assuming sample rate of 44100 Hz
            data = (track * np.iinfo(np.int16).max).astype(np.int16)
        else:
            err = Error('Unsupported audio format').__repr__()
            raise ValueError(err)

        self.playing = True
        stream.write(data.tobytes())
        stream.stop_stream()
        stream.close()
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
                    raise Exception(Error(e).__repr__())
            else:
                time.sleep(0.1)
