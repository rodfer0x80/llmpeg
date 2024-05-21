import logging
from pathlib import Path

from llmpeg.logger.logger import Logger
from llmpeg.utils import curr_date


class LoggerToLogfile(Logger):
  def __init__(self, cache_dir: Path):
    super().__init__()
    logging.basicConfig(
      level=logging.DEBUG,
      format='%(asctime)s %(levelname)s %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S',
      filename=cache_dir / f'{curr_date}.log',
    )
