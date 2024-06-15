from dataclasses import dataclass
from pathlib import Path
import wave
import struct

from PIL import Image

from llmpeg.types import ImgVec

@dataclass
class CacheDir:
  cache_dir: Path = None

  def __post_init__(self):
    if not self.cache_dir:
      self.cache_dir = Path(f'~/.cache/{str(Path(__file__).cwd().name).split("/")[-1]}').expanduser()
    Path.mkdir(self.cache_dir, exist_ok=True)

  def __str__(self) -> Path:
    return self.cache_dir

  def __repr__(self) -> Path:
    return self.cache_dir

@dataclass
class Wav:
    wav_file_path: str | Path

    def __post_init__(self):
        self.wav_file_path = Path(self.wav_file_path) if isinstance(self.wav_file_path, str) else self.wav_file_path
        if not self.wav_file_path.is_file():
            raise ValueError(f"Invalid file path: {self.wav_file_path}")
        try:
            self.wav_file = wave.open(str(self.wav_file_path), 'r')
        except wave.Error as e:
            raise ValueError(f"Error opening WAV file: {e}")
        self.sample_width = self.wav_file.getsampwidth()
        self.num_channels = self.wav_file.getnchannels()
        self.sample_rate = self.wav_file.getframerate()
        self.num_frames = self.wav_file.getnframes()
        self.format_string = f'<{"h" * self.num_channels * self.num_frames}'

    def read(self) -> list[int]:
        try:
            wav_bytes = self.wav_file.readframes(self.num_frames)
            unpacked_data = struct.unpack(self.format_string, wav_bytes)
            return list(unpacked_data)
        except struct.error as e:
            raise ValueError(f"Error reading WAV data: {e}")
        finally:
            self.wav_file.close()

    def write(self, output_file_path: str | Path, wav_bytes: list[int]):
        output_file_path = Path(output_file_path)
        packed_data = struct.pack(self.format_string, *wav_bytes)
        try:
            with wave.open(str(output_file_path), 'w') as output_wav:
                output_wav.setparams((self.num_channels, self.sample_width, self.sample_rate, self.num_frames, 'NONE', 'not compressed'))
                output_wav.writeframes(packed_data)
        except (wave.Error, struct.error) as e:
            raise ValueError(f"Error writing WAV data: {e}")
      
@dataclass
class Img:
    image_file_path: str | Path

    def __post_init__(self):
        self.image_file_path = Path(self.image_file_path) if isinstance(self.image_file_path, str) else self.image_file_path
        if not self.image_file_path.is_file():
            raise ValueError(f"Invalid file path: {self.image_file_path}")

    def read(self) -> ImgVec:
        try:
            image = Image.open(self.image_file_path)
            return list(image.getdata())
        except (OSError, Image.DecompressionBombError) as e:
            raise ValueError(f"Error reading image data: {e}")

    def write(self, output_file_path: str | Path, image_data: ImgVec):
        output_file_path = Path(output_file_path)
        try:
            image = Image.open(self.image_file_path)
            image.putdata(image_data)
            image.save(output_file_path)
        except (OSError, Image.DecompressionBombError) as e:
            raise ValueError(f"Error writing image data: {e}")