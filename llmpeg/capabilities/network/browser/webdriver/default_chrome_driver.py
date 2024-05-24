from pathlib import Path
from dataclasses import dataclass
from os import getenv
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as WebDriverTimeoutException
from selenium.webdriver.support import expected_conditions as EC

from llmpeg.capabilities.networking.browser.webdriver import Driver
from llmpeg.utils import CurrentDate, ScreenSize


@dataclass
class DefaultChromeDriver(Driver):
  # NOTE: default screen size
  # TODO: this should be dynamic but breaks in docker, need to check where it's running
  cache_dir: Path
  driver_flags: dict[bool, bool]
  window_width, window_height = ScreenSize().__repr__() if getenv('$DISPLAY', '') else 1920, 1080

  def __post_init__(self):
    self.browser_data_dir = self.cache_dir / 'data'
    Path.mkdir(self.browser_data_dir, exist_ok=True)
    self.cache_dir = self.cache_dir / 'webdriver'
    Path.mkdir(self.cache_dir, exist_ok=True)
    self.headless = self.driver_flags['headless']
    self.incognito = self.driver_flags['incognito']
    self.driver = self._init_driver()

  def _init_driver(self):
    self.options = webdriver.ChromeOptions()
    # super()._enable_insecure_options()
    super()._enable_system_options()
    self._enable_system_options()
    self._enable_stealth_options()
    self._enable_automation_options()
    driver = webdriver.Chrome(options=self.options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    return driver

  def close(self):
    super().close()

  def quit(self):
    super().quit()

  def _enable_automation_options(self):
    self.options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    self.options.add_argument('--no-sandbox')  # NOTE: dont touch this breaks user perms
    self.options.add_argument('--disable-dev-shm-usage')
    self.options.add_argument('--disable-blink-features=AutomationControlled')
    self.options.add_experimental_option('useAutomationExtension', False)
    self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
    self.options.add_argument('--disable-notifications')
    # self.options.add_argument("--disable-logging")
    # self.options.add_argument("--silent")
    self.options.add_argument('--verbose')
    self.options.add_argument('disable-infobars')
    self.options.add_argument('--disable-crash-reporter')
    self.options.add_argument('--ignore-ssl-errors=yes')
    self.options.add_argument('--ignore-certificate-errors')
    # cookies and browser data dir
    self.options.add_argument(f'user-data-dir={self.browser_data_dir}')
    # self.option.add_experimental_option("detach", True) #prevent window from closing

  def _enable_stealth_options(self, country_id='en-GB', incognito=False):
    # TODO: fix this with a better UA
    # self.options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
    #                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    self.options.add_argument(f'--{country_id}')
    self.options.add_argument(f'--window-size={self.window_width},{self.window_height}')
    if incognito:
      self.options.add_argument('--incognito')
    self.options.add_argument('--disable-gpu')
    # self.options.add_argument('--start-maximized')
    # self.options.add_argument('--start-fullscreen')
    # self.options.add_argument("--disable-extensions")

  def screenshot(self, url: str) -> bytes:
    img_path = self.save_screenshot(url)
    with open(img_path, 'rb') as h:
      img_bytes = h.read()
    return img_bytes

  def save_screenshot(self, url: str) -> Path:
    path = self.cache_dir / f'{CurrentDate()}.png'
    # Ref: https://stackoverflow.com/a/52572919/
    original_size = self.driver.get_window_size()
    required_width = self.driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = self.driver.execute_script('return document.body.parentNode.scrollHeight')
    self.driver.set_window_size(required_width, required_height)
    self.driver.get(url)
    # NOTE: hack to wait for webpage to load, sometimes breaks
    try:
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    except WebDriverTimeoutException:
      pass
    WebDriverWait(self.driver, 5).until(lambda d: self.driver.execute_script('return document.readyState') == 'complete')
    # self.driver.save_screenshot(path)  # has scrollbar?
    self.driver.find_element(By.TAG_NAME, 'body').screenshot(str(path))  # avoids scrollbar?
    sleep(1)
    self.driver.set_window_size(original_size['width'], original_size['height'])
    return path
