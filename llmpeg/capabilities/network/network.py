import requests
from dataclasses import dataclass
from typing import Union
from pathlib import Path

from bs4 import BeautifulSoup
import yt_dlp

from llmpeg.utils import Error
from llmpeg.capabilities.network.browser import Browser


@dataclass
class Network:
    cache_dir: Path

    def __post_init__(self) -> None:
        self.session: requests.Session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0'  # 'Chrome/78.0.3904.108'
        })
        self.browser = Browser(self.cache_dir)

    def scrape(self, url: str) -> tuple[str, Union[str, None]]:
        try:
            response = self.session.get(url)
            # NOTE: raise an exception for bad status codes
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            text_content = soup.get_text()
            text_content = ' '.join(text_content.split())
            text_content = text_content.replace('\n', ' ')
            text_content = text_content.replace('\t', ' ')
            text_content = text_content.replace('\r', ' ')
            text_content = text_content.replace('\xa0', ' ')
            text_content = text_content.replace('\u200b', ' ')
            return text_content, None
        except requests.RequestException as e:
            return '', Error(e).__repr__()

    def scrape_url(self, url: str) -> tuple[Union[str, None], Union[str, None]]:
        text_content, err = self.scrape(url)
        if err:
            raise Exception(Error(err).__repr__())
        return text_content

    def _find_audio(self, query: str) -> tuple[Union[str, None], Union[str, None]]:
        # NOTE: ffmpeg is required for this to work
        # NOTE: mp3 192kbps is the preferred format
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [
                {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }
            ],
            'quiet': True,
        }
        # NOTE: search ytdl database for the query
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                results = ydl.extract_info(f'ytsearch1:{query}', download=False)
                if 'entries' in results and len(results['entries']) > 0:
                    return results['entries'][0]['url'], None
                else:
                    return None, Error('No search results found').__repr__()

    def find_audio(self, query: str) -> tuple[Union[str, None], Union[str, None]]:
        try:
            return self._find_audio(query)
        except Exception as e:
            return None, Error(e).__repr__()
