
import easyocr

class Vision:
  def __init__(self): self.reader = easyocr.Reader(['english_g2','en'])
  def ocr(self, path: str) -> str: return self.reader.readtext(path)