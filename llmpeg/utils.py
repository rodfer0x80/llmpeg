# NOTE: this file has to be depency free so only core python modules allowed
import inspect
import datetime
import tkinter as tk
from pathlib import Path
from dataclasses import dataclass
from collections import namedtuple

@dataclass
class Error:
  msg: str
  error_msg: str = None

  def __post_init__(self):
    path = inspect.getfile(inspect.currentframe().f_back)
    method = inspect.currentframe().f_back.f_code.co_name
    line = inspect.currentframe().f_back.f_lineno
    self.error_msg = f'[{path}:{method}:{line}]: {self.msg}'

  def __str__(self):
    return self.error_msg

  def __repr__(self):
    return self.error_msg

@dataclass
class CurrentDate:
  date: str = None

  def __post_init__(self):
    self.date = datetime.datetime.now().strftime('%H-%M-%S_%d-%m-%Y')

  def __str__(self):
    return self.date

  def __repr__(self):
    return self.date

@dataclass
class ScreenSize:
  screen_size: tuple = None

  def __post_init__(self):
    width = tk.Tk().winfo_screenwidth()
    height = tk.Tk().winfo_screenheight()
    self.screen_size = namedtuple('ScreenSize', ['width', 'height'])(width, height)

  def __str__(self):
    return self.screen_size

  def __repr__(self):
    return self.screen_size
  
@dataclass
class FileCacheDirectory:
  cache_dir: Path = None

  def __post_init__(self):
    self.cache_dir = Path(f'~/.cache/{str(Path(__file__).cwd().name).split("/")[-1]}').expanduser()
    Path.mkdir(self.cache_dir, exist_ok=True)

  def __str__(self) -> Path:
    return self.cache_dir

  def __repr__(self) -> Path:
    return self.cache_dir
