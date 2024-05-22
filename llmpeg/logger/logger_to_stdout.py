from dataclasses import dataclass

from llmpeg.utils import error


@dataclass
class LoggerToStdout:
  def log(self, msg: str):
    self.debug(msg)

  def debug(self, msg: str):
    print(f'[DEBUG]: {error(msg)}')

  def info(self, msg: str):
    print(f'[INFO]: {error(msg)}')

  def warning(self, msg: str):
    print(f'[WARNING]: {error(msg)}')

  def error(self, msg: str):
    print(f'[ERROR]: {error(msg)}')

  def critical(self, msg: str):
    print(f'[CRITICAL]: {error(msg)}')
