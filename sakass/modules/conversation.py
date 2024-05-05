import ollama

class Prompts:
  summarize = "what is all about?"

class Triggers:
  start = "hey babe"
  stop = "see ya babe"

class Conversation:
  def __init__(self, model):
    self.model = model

  def summarize(self, text):
    return ollama.generate(model=self.model, prompt=f"{Prompts.summarize}\n{text}")

  def respond(self, text):
    return ollama.generate(model=self.model, prompt=text)