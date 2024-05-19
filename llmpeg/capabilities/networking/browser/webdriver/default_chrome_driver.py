import os
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as WebDriverTimeoutException
from selenium.webdriver.support import expected_conditions as EC

from llmpeg.capabilities.networking.browser.webdriver import Driver
from llmpeg.utils import curr_date, get_screen_size

class DefaultChromeDriver(Driver):
  # NOTE: default screen size
  # TODO: this should be dynamic
  WIDTH, HEIGHT = get_screen_size()
  def __init__(self, cache_dir, driver_flags):
    self.cache_dir = cache_dir
    self.headless = driver_flags["headless"]
    self.incognito = driver_flags["incognito"]
    super().__init__(headless=self.headless)
    self.browser_data_dir = os.path.join(self.cache_dir, "data")
    self.driver = self.init()
  def init(self):
    self.options = webdriver.ChromeOptions()
    self._enable_system_options()
    self._enable_stealth_options()
    self._enable_automation_options()
    driver = webdriver.Chrome(options=self.options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    return driver
  def close(self): super().close()
  def quit(self): super().quit()

  def _enable_automation_options(self):
    self.options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    self.options.add_argument("--no-sandbox") # NOTE: dont touch this breaks user perms
    self.options.add_argument("--disable-dev-shm-usage")
    self.options.add_argument('--disable-blink-features=AutomationControlled')
    self.options.add_experimental_option('useAutomationExtension', False)
    self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
    self.options.add_argument("--disable-notifications")
    # self.options.add_argument("--disable-logging")
    # self.options.add_argument("--silent")
    self.options.add_argument("--verbose")
    self.options.add_argument("disable-infobars")
    self.options.add_argument("--disable-crash-reporter")
    self.options.add_argument('--ignore-ssl-errors=yes')
    self.options.add_argument('--ignore-certificate-errors')
    # cookies and browser data dir
    self.options.add_argument(f"user-data-dir={self.browser_data_dir}")
    # self.option.add_experimental_option("detach", True) #prevent window from closing
  def _enable_stealth_options(self, country_id="en-GB", incognito=False):
    # TODO: fix this with a better UA
    # self.options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
    #                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    self.options.add_argument(f"--{country_id}")
    self.options.add_argument(f"--window-size={self.WIDTH},{self.HEIGHT}")
    if incognito: self.options.add_argument("--incognito")
    self.options.add_argument("--disable-gpu")
    # self.options.add_argument('--start-maximized')
    # self.options.add_argument('--start-fullscreen')
    # self.options.add_argument("--disable-extensions")  

  def screenshot(self, url: str) -> bytes: 
    with open(self.save_screenshot(url=url, path=""), "rb") as h: return h.read()
  def save_screenshot(self, url: str, path: os.PathLike) -> os.PathLike:
    if not path: path = os.path.join(self.cache_dir, f"{curr_date()}.png")
    # Ref: https://stackoverflow.com/a/52572919/
    original_size = self.driver.get_window_size()
    required_width = self.driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = self.driver.execute_script('return document.body.parentNode.scrollHeight')
    self.driver.set_window_size(required_width, required_height)
    self.driver.get(url)
    # NOTE: hack to wait for webpage to load, sometimes breaks
    try: WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    except WebDriverTimeoutException: pass
    WebDriverWait(self.driver, 5).until(lambda d: self.driver.execute_script('return document.readyState') == 'complete')
    #self.driver.save_screenshot(path)  # has scrollbar?
    self.driver.find_element(By.TAG_NAME, 'body').screenshot(path)  # avoids scrollbar?
    self.driver.set_window_size(original_size['width'], original_size['height'])
    return path
