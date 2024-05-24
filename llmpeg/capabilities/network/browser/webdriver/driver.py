from dataclasses import dataclass

from llmpeg.utils import Error


@dataclass
class Driver:
  def _init_driver(self) -> None:
    raise Exception(Error('Not implemented'))

  def close(self) -> None:
    self.driver.close() if self.driver else None  # NOTE: webdrive breaks without this condition

  def quit(self) -> None:
    self.driver.quit() if self.driver else None  # NOTE: webdrive breaks without this condition

  def _enable_insecure_options(self) -> None:
    self.options.add_argument('--single-process')
    self.options.add_argument('--disable-popup-blocking')
    self.options.add_argument('--no-sandbox')
    self.options.add_argument('--disable-web-security')
    self.options.add_argument('--allow-running-insecure-content')

  def _enable_system_options(self) -> None:
    self.options.add_argument('--disable-dev-shm-usage')
    if self.headless:
      self.options.add_argument('--headless')
