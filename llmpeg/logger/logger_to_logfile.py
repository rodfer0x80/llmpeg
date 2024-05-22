import logging
from pathlib import Path
from dataclasses import dataclass

from llmpeg.logger.logger import Logger
from llmpeg.utils import curr_date


@dataclass
class LoggerToLogfile(Logger):
  cache_dir: Path

  def __post_init__(self):
    super().__init__()
    logging.basicConfig(
      level=logging.DEBUG,
      format='%(asctime)s %(levelname)s %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S',
      filename=self.cache_dir / f'{curr_date}.log',
    )
