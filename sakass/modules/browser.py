from scrapegraphai.graphs import SmartScraperGraph

from sakass.modules.prompts import Prompts
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

  def scrape(self, url, prompt):
    smart_scraper_graph = SmartScraperGraph(
      prompt=prompt,
      source=url, # also accepts a string with the already downloaded HTML code
      config=self.graph_config
    )
    llm_processed_data = smart_scraper_graph.run()
    return llm_processed_data
  
  def search(self, url, prompt):
    return self.scrape(url=url, prompt=prompt)
  
  def summarize(self, url, prompt=Prompts.summarize):
    print(self.scrape(url=url, prompt=prompt))

  def explain(self, url, prompt=Prompts.explain):
    print(self.scrape(url=url, prompt=Prompts.explain))
