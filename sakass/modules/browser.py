import requests
from bs4 import BeautifulSoup

class Browser:
  def __init__(self):
      return None
  
  def scrape(self, url):
      err = None
      try:
          response = requests.get(url)
          response.raise_for_status()  # Raise an exception for bad status codes
          soup = BeautifulSoup(response.content, 'html.parser')
          text_content = soup.get_text()
          return text_content, err
      except requests.RequestException as e:
          err = f"Error:{e}"
          return "", err
