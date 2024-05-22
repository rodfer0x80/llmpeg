# NOTE: this file has to be depency free so only core python modules allowed
import inspect
import datetime
import tkinter as tk
from pathlib import Path


def error(msg: str) -> str:
  path = inspect.getfile(inspect.currentframe().f_back)
  method = inspect.currentframe().f_back.f_code.co_name
  line = inspect.currentframe().f_back.f_lineno
  return f'[{path}:{method}:{line}]: {msg}'


def curr_date() -> str:
  return datetime.datetime.now().strftime('%H-%M-%S_%d-%m-%Y')


def screen_size() -> tuple[int, int]:
  return tk.Tk().winfo_screenwidth(), tk.Tk().winfo_screenheight()


def filenamed_cache_dir() -> Path:
  return Path(f'~/.cache/{str(Path(__file__).cwd().name).split("/")[-1]}').expanduser()
