from dataclasses import dataclass

from llmpeg.logger.logger_to_stdout import LoggerToStdout
from llmpeg.logger.logger_to_logfile import LoggerToLogfile
from llmpeg.utils import error


@dataclass
class LoggerFactory:
  log_output: str
  
  def __post_init__(self):
    if self.log_output == 'stdout': return LoggerToStdout()
    elif self.log_output == 'logfile': return LoggerToLogfile()
    else:
      raise (Exception(error('Invalid <log_output>')))
