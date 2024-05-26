from pathlib import Path
from dataclasses import dataclass

from llmpeg.capabilities.network.browser.webdriver import DefaultChromeDriver


@dataclass
class Browser:
        cache_dir: Path

        def __post_init__(self):
                self.cache_dir = self.cache_dir / 'browser'
                Path.mkdir(self.cache_dir, exist_ok=True)

                self.driver = DefaultChromeDriver(
                        cache_dir=self.cache_dir, driver_flags={'headless': True, 'incognito': False}
                )

        # TODO: need to hide browser while doing this but headless is only screenshoting all the page on x11
        def screenshot(self, url: str) -> bytes:
                data = self.driver.screenshot(url)
                self.driver.close()  # NOTE: close the browser after taking the screenshot
                return data

        def save_screenshot(self, url: str) -> str:
                ss_path = self.driver.save_screenshot(url)
                self.driver.close()  # NOTE: close the browser after taking the screenshot
                return ss_path
