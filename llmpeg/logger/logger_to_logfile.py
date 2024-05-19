import logging
import pathlib
import os

from llmpeg.logger.logger import Logger
from llmpeg.utils import curr_date

class LoggerToLogfile(Logger):
  def __init__(self, cache_dir: str):
    super().__init__()
    self.cache_dir = cache_dir
    self.logfile = pathlib.Path(os.path.join(self.cache_dir, f"{curr_date}.log"))
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=self.logfile
    )
