import logging
from dataclasses import dataclass

from llmpeg.utils import error

@dataclass
class Logger:
  def log(self, msg):
    return self.info(error(msg))

  def debug(msg):
    try:
      logging.debug(f'{error(msg)}')
    except Exception as e:
      raise (Exception(f'{error(e)}'))

  def info(self, msg):
    try:
      logging.info(f'{error(msg)}')
    except Exception as e:
      raise (Exception(f'{error(e)}'))

  def warning(self, msg):
    try:
      logging.warning(f'{error(msg)}')
    except Exception as e:
      raise (Exception(f'{error(e)}'))

  def error(self, msg: str) -> int:
    try:
      logging.error(f'{error(msg)}')
    except Exception as e:
      raise (Exception(f'{error(e)}'))

  def critical(self, msg: str) -> int:
    try:
      logging.critical(f'{error(msg)}')
    except Exception as e:
      raise (Exception(f'{error(e)}'))
