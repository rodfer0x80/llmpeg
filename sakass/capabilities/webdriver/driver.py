from sakass.utils import error

class Driver:
  def __init__(self, headless):
    self.options = None
    self.service = None
    self.headless = headless
    
  def close(self): self.driver.quit() if self.driver else None
  def init(self): raise(error("Not implemented"))
  def get(self): return self.driver

  def _enable_insecure_options(self):
    self.options.add_argument('--single-process')
    self.options.add_argument("--disable-popup-blocking")
    self.options.add_argument("--no-sandbox")
    self.options.add_argument("--disable-web-security")
    self.options.add_argument("--allow-running-insecure-content")
  def _enable_system_options(self):
    self.options.add_argument("--disable-dev-shm-usage")
    if self.headless: self.options.add_argument("--headless")

