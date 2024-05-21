from pathlib import Path

import easyocr

from llmpeg.capabilities.networking.browser import Browser


class Vision:
  def __init__(self, browser: Browser):
    self.browser = browser
    self.ocr_reader = easyocr.Reader(['ch_tra', 'en'])

  def ocr_stream(self, stream: bytes) -> list[str]:
    return self.ocr_reader.readtext(stream, detail=0)

  def ocr_img(self, path: Path) -> list[str]:
    return [word[-2] for word in self.ocr_reader.readtext(path, detail=0)]

  # TODO: https://github.com/Efficient-Large-Model/VILA?tab=readme-ov-file
