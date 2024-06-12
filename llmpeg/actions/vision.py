from pathlib import Path
from dataclasses import dataclass
from PIL import Image
import requests
from typing import Union


from llmpeg.models.vlm import VLM
from llmpeg.types import URL  # TODO: fileIO should be in actions


@dataclass
class Vision:
  model_name: str
  cache_dir: Path
  ocr_query: str = 'Perform OCR on this image and return the text: '

  def __post_init__(self) -> None:
    self.cache_dir = self.cache_dir / 'vision'
    Path.mkdir(self.cache_dir, exist_ok=True)
    self.vlm = VLM(cache_dir=self.cache_dir, model_name=self.model_name)

  # TODO: fileIO should be in actions
  def preprocess_image(self, image: Union[URL, Image.Image, Path]) -> Image.Image:
    if isinstance(image, URL):
      url = str(image)
      _image = requests.get(url, stream=True).raw
      image = Image.open(_image)
    elif isinstance(image, Path):
      image = Image.open(image)
    return image.convert('RGB')

  def ocr(self, image: Union[URL, Image.Image, Path]) -> list[str]:
    return self.vlm.generate(self.ocr_query, self.preprocess_image(image))

  def query(self, query: str, image: Union[Path, URL, Image.Image]) -> list[str]:
    return self.vlm.generate(query, self.preprocess_image(image))
