from dataclasses import dataclass, field
import inspect
from datetime import datetime
from urllib.parse import urlparse


@dataclass
class Error:
    msg: str
    error_msg: str = field(init=False)

    def __post_init__(self):
        frame = inspect.currentframe().f_back
        path = inspect.getfile(frame)
        method = frame.f_code.co_name
        line = frame.f_lineno
        self.error_msg = f'[{path}:{method}:{line}]: {self.msg}'

    def __str__(self):
        return self.error_msg

    def __repr__(self):
        return f'Error({self.error_msg!r})'


class URL:
    text: str

    def __post_init__(self):
        if not self.is_valid_url(self.text):
            raise ValueError(f'Invalid URL: {self.text}')

    # @staticmethod
    # def is_valid_url(url: str) -> bool:
    #     # Simple regex to check the structure of the URL
    #     regex = re.compile(
    #         r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://
    #         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    #         r'localhost|'  # localhost...
    #         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    #         r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    #         r'(?::\d+)?'  # optional port
    #         r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    #     return re.match(regex, url) is not None

    @staticmethod
    def is_valid_url(url: str) -> bool:
        parsed_url = urlparse(url)
        return all([parsed_url.scheme, parsed_url.netloc])

    def __str__(self):
        return self.text

    def __repr__(self):
        return f'URL({self.text!r})'

    def __eq__(self, other):
        if not isinstance(other, URL):
            return NotImplemented
        return self.text == other.text

    def __ne__(self, other):
        if not isinstance(other, URL):
            return NotImplemented
        return self.text != other.text

    def __lt__(self, other):
        if not isinstance(other, URL):
            return NotImplemented
        return self.text < other.text

    def __le__(self, other):
        if not isinstance(other, URL):
            return NotImplemented
        return self.text <= other.text

    def __gt__(self, other):
        if not isinstance(other, URL):
            return NotImplemented
        return self.text > other.text

    def __ge__(self, other):
        if not isinstance(other, URL):
            return NotImplemented
        return self.text >= other.text


@dataclass
class Date:
    text: str = None


@dataclass(unsafe_hash=True)
class CurrentDate(Date):
    def __post_init__(self):
        if not self.text:
            self.text = datetime.datetime.now().strftime('%H-%M-%S_%d-%m-%Y')

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text
