from scrapegraphai.graphs import SmartScraperGraph

class Prompts:
  summarize = "what is all about?"
class Browser:
  def __init__(self, model, embedding):
    self.graph_config = {
      "llm": {
          "model": f"ollama/{model}",
          "temperature": 0,
          "format": "json",
          "base_url": "http://localhost:11434", 
      },
      "embeddings": {
          "model": f"ollama/{embedding}",
          "base_url": "http://localhost:11434",  
      }
    }

  def scrape_url(self, url, prompt):
    smart_scraper_graph = SmartScraperGraph(
      prompt=prompt,
      source=url, # also accepts a string with the already downloaded HTML code
      config=self.graph_config
    )
    data = smart_scraper_graph.run()
    return data
  
  def summarize_url(self, url):
    print(self.scrape_url(url=url, prompt=Prompts.summarize))
