import ollama

class Prompts:
  def __init__(self):
    self.summarize = "what is all about?"

class Triggers:
  def __init__(self):
    self.start = "hey babe"
    self.stop = "see ya babe"

class Conversation:
  def __init__(self, model):
    self.triggers = Triggers()
    self.prompts = Prompts()
    self.model = model

  def summarize(self, text):
    return ollama.generate(model=self.model, prompt=f"{self.prompts.summarize}\n{text}")

  def respond(self, text):
    return ollama.generate(model=self.model, prompt=text)