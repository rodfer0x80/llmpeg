from pathlib import Path
from dataclasses import dataclass

from loguru import logger

from llmpeg.utils import CurrentDate, Error


@dataclass
class LoggerToLogfile:
  cache_dir: Path

  def __post_init__(self):
    self.cache_dir = self.cache_dir / 'logs'
    Path.mkdir(self.cache_dir, exist_ok=True)
    logfile = self.cache_dir / f'{CurrentDate}.log'
    logger.add(logfile, rotation='1 day', retention='7 days', level='DEBUG')

  def log(self, msg):
    return self.info(Error(msg))

  def debug(msg):
    try:
      logger.debug(msg)
    except Exception as e:
      raise (Exception(f'{Error(e)}'))

  def info(self, msg):
    try:
      logger.info(msg)
    except Exception as e:
      raise (Exception(f'{Error(e)}'))

  def warning(self, msg):
    try:
      logger.warning(msg)
    except Exception as e:
      raise (Exception(f'{Error(e)}'))

  def error(self, msg: str) -> int:
    try:
      logger.error(msg)
    except Exception as e:
      raise (Exception(f'{Error(e)}'))

  def critical(self, msg: str) -> int:
    try:
      logger.critical(msg)
    except Exception as e:
      raise (Exception(f'{Error(e)}'))
