from pathlib import Path
from dataclasses import dataclass

import easyocr


@dataclass
class Vision:
  def __post_init__(self):
    self.ocr_reader = easyocr.Reader(['ch_tra', 'en'])

  def ocr_stream(self, stream: bytes) -> list[str]:
    return self.ocr_reader.readtext(stream, detail=0)

  def ocr_img(self, path: Path) -> list[str]:
    return [word[-2] for word in self.ocr_reader.readtext(path, detail=0)]

  # TODO: https://github.com/Efficient-Large-Model/VILA?tab=readme-ov-file
