import requests
from bs4 import BeautifulSoup

class Browser:
  def __init__(self, model):
    self.model = model
    self.headless = True

  def extract_text_from_url(self, url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    text_elements = soup.find_all(['p', 'div', 'span', 'article', 'section', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    text = '\n'.join(element.get_text(separator='\n') for element in text_elements)
    return text