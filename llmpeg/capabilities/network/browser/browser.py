from pathlib import Path
from dataclasses import dataclass
from typing import Union

from llmpeg.capabilities.networking.browser.webdriver import DefaultChromeDriver
from llmpeg.capabilities.networking import Networking


@dataclass
class Browser:
  cache_dir: Path

  def __post_init__(self):
    self.cache_dir = self.cache_dir / 'browser'
    Path.mkdir(self.cache_dir, exist_ok=True)
    self.driver = DefaultChromeDriver(cache_dir=self.cache_dir, driver_flags={'headless': True, 'incognito': False})
    self.networking = Networking()

  def scrape(self, url: str) -> tuple[str, Union[str, None]]:
    return self.networking.scrape(url)

  # TODO: need to hide browser while doing this but headless is only screenshoting all the page on x11

  def screenshot(self, url: str) -> bytes:
    data = self.driver.screenshot(url)
    self.driver.close()
    return data

  def save_screenshot(self, url: str) -> str:
    ss_path = self.driver.save_screenshot(url)
    self.driver.close()
    return ss_path

  def scrape_url(self, url: str) -> tuple[Union[str, None], Union[str, None]]:
    text_content, err = self.networking.scrape(url)
    if err:
      raise Exception(err)
    return text_content