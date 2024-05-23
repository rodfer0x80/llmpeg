import requests
from dataclasses import dataclass
from typing import Union

from bs4 import BeautifulSoup
import yt_dlp

from llmpeg.utils import Error


@dataclass
class Networking:
  def __post_init__(self) -> None:
    self.session: requests.Session = requests.Session()
    self.session.headers.update({'User-Agent': 'Mozilla/5.0'})  # self.session.headers.update({'User-Agent': 'Chrome/78.0.3904.108'})

  def scrape(self, url: str) -> tuple[str, Union[str, None]]:
    try:
      response = self.session.get(url)
      response.raise_for_status()  # NOTE: raise an exception for bad status codes
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
      return '', Error(e)

  def search_audio_stream(self, query: str) -> tuple[Union[str, None], Union[str, None]]:
    try:
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
        search_results = ydl.extract_info(f'ytsearch1:{query}', download=False)
        if 'entries' in search_results and len(search_results['entries']) > 0:
          return search_results['entries'][0]['url'], None
        else:
          return None, Error('No search results found')
    except Exception as e:
      return None, Error(e)
