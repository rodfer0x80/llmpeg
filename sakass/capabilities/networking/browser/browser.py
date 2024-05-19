from typing import Tuple, Optional
import os

from sakass.capabilities.networking.browser.webdriver import DefaultChromeDriver
from sakass.capabilities.networking import Networking

class Browser:
  def __init__(self, cache_dir: os.PathLike): 
    self.cache_dir = cache_dir
    self.driver = DefaultChromeDriver(cache_dir=self.cache_dir,driver_flags={"headless": False,"incognito": False})
    self.networking = Networking()
  
  def scrape(self, url: str) -> Tuple[str, Optional[str]]: return self.networking.scrape(url)
  # TODO: need to hide browser while doing this but headless is only screenshoting all the page on x11
  
  def screenshot(self, url: str) -> bytes: 
    data = self.driver.screenshot(url)
    self.driver.close()
    return data
  def save_screenshot(self, url: str, path = "") -> str: 
    ss_path = self.driver.save_screenshot(url, path)
    self.driver.close()
    return ss_path
  
  def search_audio_stream(self, query: str) -> Tuple[Optional[str], Optional[str]]: self.driver.search_audio_stream(query)
