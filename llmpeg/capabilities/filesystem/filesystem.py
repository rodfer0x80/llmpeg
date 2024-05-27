from dataclasses import dataclass
from pathlib import Path
import wave

import numpy as np


@dataclass
class FileCacheDirectory:
    cache_dir: Path = None

    def __post_init__(self):
        if not self.cache_dir:
            self.cache_dir = Path(f'~/.cache/{str(
                Path(__file__).cwd().name).split("/")[-1]}').expanduser()
        Path.mkdir(self.cache_dir, exist_ok=True)

    def __str__(self) -> Path:
        return self.cache_dir

    def __repr__(self) -> Path:
        return self.cache_dir


@dataclass
class WaveFile:
    def read(file: Path) -> tuple:
        with wave.open(file, 'rb') as wf:
            fs = wf.getframerate()
            data = wf.readframes(wf.getnframes())
        return fs, np.frombuffer(data, dtype=np.int16)  # 16-bit int

    def write(audio_stream: np.ndarray, path: Path, sr: int = 16000):
        with wave.open(str(path), 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit int
            wf.setframerate(sr)
            wf.writeframes(audio_stream.tobytes())
