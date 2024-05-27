import numpy as np
import pyaudio
from dataclasses import dataclass
from pathlib import Path
from functools import partial

from llmpeg.utils import CurrentDate, WaveFile


@dataclass
class AudioInput:
    cache_dir: Path

    def __post_init__(self):
        self.audio = pyaudio.PyAudio()

    def capture_stream(self, duration: int = 5, sr: int = 16000) -> np.float32:
        CHUNK = 1024
        FORMAT = pyaudio.paInt16  # int16
        CHANNELS = 1
        frames = []

        stream = self.audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=sr,
            input=True,
            frames_per_buffer=CHUNK,
        )

        num_frames = int(sr / CHUNK * duration)
        read_chunk = partial(stream.read, CHUNK)
        frames = [np.frombuffer(read_chunk(), dtype=np.int16) for _ in range(num_frames)]

        stream.stop_stream()
        stream.close()

        audio_stream = np.concatenate(frames).astype(np.float32)
        return audio_stream  # float32

    def __del__(self):
        self.audio.terminate()

    def capture_to_file(self, duration: int = 5, sr: int = 16000) -> Path:
        audio_stream = self.capture_stream(duration, sr)
        audio_file = self.cache_dir / f'{CurrentDate().date}.wav'
        WaveFile.write(audio_stream, audio_file, sr)
        return audio_file
