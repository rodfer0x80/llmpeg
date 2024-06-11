from pathlib import Path
from dataclasses import dataclass

from pylogger import LoggerToStdout

from llmpeg.capabilities.network.browser.webdriver import DefaultChromeDriver
from llmpeg.types import URL


@dataclass
class Browser:
  cache_dir: Path

  def __post_init__(self):
    self.cache_dir = self.cache_dir / 'browser'
    Path.mkdir(self.cache_dir, exist_ok=True)

    self.logger = LoggerToStdout()

    self.driver = DefaultChromeDriver(
      cache_dir=self.cache_dir,
      driver_flags={'headless': True, 'incognito': False},
    )

  def screenshot(self, url: URL) -> bytes:
    data = self.driver.screenshot(str(url))
    self.logger.debug(f'Screenshot taken: {url}')
    self.driver.close()
    return data

  def save_screenshot(self, url: URL) -> str:
    ss_path = self.driver.save_screenshot(str(url))
    self.logger.debug(f'Screenshot taken: {url}')
    self.logger.debug(f'Screenshot saved: {ss_path}')
    self.driver.close()
    return ss_path
