from dataclasses import dataclass, field
import inspect
from datetime import datetime
from urllib.parse import urlparse


@dataclass
class Error:
  msg: str
  error_msg: str = field(init=False)

  def __post_init__(self):
    frame = inspect.currentframe().f_back
    path = inspect.getfile(frame)
    method = frame.f_code.co_name
    line = frame.f_lineno
    self.error_msg = f'[{path}:{method}:{line}]: {self.msg}'

  def __str__(self):
    return self.error_msg

  def __repr__(self):
    return f'Error({self.error_msg!r})'


class URL:
  text: str

  def __post_init__(self):
    if not self.is_valid_url(self.text):
      raise ValueError(f'Invalid URL: {self.text}')

  @staticmethod
  def is_valid_url(url: str) -> bool:
    parsed_url = urlparse(url)
    return all([parsed_url.scheme, parsed_url.netloc])

  def __str__(self):
    return self.text

  def __repr__(self):
    return f'URL({self.text!r})'


@dataclass
class Date:
  text: str = None

  def now(self):
    self.text = datetime.datetime.now().strftime('%H-%M-%S_%d-%m-%Y')
    return self.text

  def __str__(self):
    return self.text

  def __repr__(self):
    return f'Date({self.text!r})'

@dataclass
class ImgVec:
    data: list[int]
