import ollama

from sakass.modules.prompts import Prompts

class Triggers:
  start = "hey babe"
  stop = "see ya babe"

class Conversation:
  def __init__(self, model):
    self.model = model

  def summarize(self, text):
    return ollama.generate(model=self.model, prompt=f"{Prompts.summarize}\n{text}")
  
  def explain(self, text):
    return ollama.generate(model=self.model, prompt=f"{Prompts.explain}\n{text}")

  def respond(self, text):
    return ollama.generate(model=self.model, prompt=text)
  
  def chat(self, text):
    return 0 # ollama.chat()