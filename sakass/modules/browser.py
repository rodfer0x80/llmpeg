from typing import Tuple, Optional

from selenium import webdriver

from sakass.capabilities.networking import Networking
from sakass.modules.vision import Vision
class Browser:
  def __init__(self, driver: webdriver.Chrome, vision: Vision):
    self.driver = driver
    self.networking = Networking()
    self.vision = vision
  def close(self): self.driver.quit()

  def scrape(self, url: str) -> Tuple[str, Optional[str]]: return self.networking.scrape(url)

  def screenshot(self, url: str) -> bytes: return self.driver.screenshot(url)
  def save_screenshot(self, url: str, path = "") -> str: return self.driver.save_screenshot(url, path)
  def scrapeshot(self, url: str) -> bytes: return self.vision(self.driver.save_screenshot(url))
  
  def search_audio_stream(self, query: str) -> Tuple[Optional[str], Optional[str]]: self.driver.search_audio_stream(query)
