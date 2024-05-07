from sakass.modules.patterns import Prompts
from sakass.modules.patterns import Triggers

import ollama

#TODO: have a conversation with preprompted character roleplay and play songs on request
#TODO: this should be a in front of browser and call it todo stuff instead of bypassing this and using capabilities directly
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