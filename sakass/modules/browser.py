import requests
from typing import Tuple, Optional

from bs4 import BeautifulSoup
import yt_dlp


class Browser:
  def __init__(self) -> None:
    self.session = requests.Session()
    self.session.headers.update({'User-Agent': 'Mozilla/5.0'})

  def scrape(self, url: str) -> Tuple[str, Optional[str]]:
    try:
      response = self.session.get(url)
      response.raise_for_status()  # NOTE: raise an exception for bad status codes
      soup = BeautifulSoup(response.content, 'html.parser')
      text_content = soup.get_text()
      return text_content, None
    except requests.RequestException as e:
      return "", f"Error: {e}"

  def search_audio_stream(self, query: str) -> Tuple[Optional[str], Optional[str]]:
    try:
      # NOTE: ffmpeg is required for this to work
      # NOTE: mp3 192kbps is the preferred format
      ydl_opts = {
          'format': 'bestaudio/best',
          'postprocessors': [{
              'key': 'FFmpegExtractAudio',
              'preferredcodec': 'mp3',
              'preferredquality': '192',
          }],
          'quiet': True,
      }
      # NOTE: search ytdl database for the query
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch1:{query}", download=False)
        if 'entries' in search_results and len(search_results['entries']) > 0:
          audio_url = search_results['entries'][0]['url']
          return audio_url, None
        else:
          return None, "No search results found"
    except Exception as e:
      return None, f"An error occurred: {e}"
