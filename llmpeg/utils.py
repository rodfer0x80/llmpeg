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
  width: int = None
  height: int = None

  def __post_init__(self):
    self.width = tk.Tk().winfo_screenwidth()
    self.height = tk.Tk().winfo_screenheight()

  def __str__(self) -> tuple:
    return self.width, self.height

  def __repr__(self) -> tuple:
    return self.width, self.height
  
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
