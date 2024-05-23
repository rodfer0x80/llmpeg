from dataclasses import dataclass

from llmpeg.utils import Error


@dataclass
class Logger:
  def log(self, msg: str):
    self.debug(msg)

  def debug(self, msg: str):
    print(f'[DEBUG]: {Error(msg)}')

  def info(self, msg: str):
    print(f'[INFO]: {Error(msg)}')

  def warning(self, msg: str):
    print(f'[WARNING]: {Error(msg)}')

  def error(self, msg: str):
    print(f'[ERROR]: {Error(msg)}')

  def critical(self, msg: str):
    print(f'[CRITICAL]: {Error(msg)}')