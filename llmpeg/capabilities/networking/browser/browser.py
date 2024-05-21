from pathlib import Path
import os

from llmpeg.capabilities.networking.browser.webdriver import DefaultChromeDriver
from llmpeg.capabilities.networking import Networking

class Browser:
  def __init__(self, cache_dir: Path): 
    self.cache_dir = cache_dir / "browser"
    os.mkdir(self.cache_dir, exist_ok=True)
    
    self.driver = DefaultChromeDriver(cache_dir=self.cache_dir,driver_flags={"headless": True,"incognito": True})
    self.networking = Networking()
  
  def scrape(self, url: str) -> tuple[str, str|None]: return self.networking.scrape(url)
  # TODO: need to hide browser while doing this but headless is only screenshoting all the page on x11
  
  def screenshot(self, url: str) -> bytes: 
    data = self.driver.screenshot(url)
    self.driver.close()
    return data
  
  def save_screenshot(self, url: str, path = "") -> str: 
    ss_path = self.driver.save_screenshot(url, path)
    self.driver.close()
    return ss_path
  
  def search_audio_stream(self, query: str) -> tuple[str|None, str|None]: self.driver.search_audio_stream(query)
