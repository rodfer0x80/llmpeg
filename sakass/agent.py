from sakass.capabilities import Speak, Listen
from sakass.modules import Conversation, Browser

class Agent:
  def __init__(self, conversation_model, browser_model, browser_embedding):
    self.conversation = Conversation(model=conversation_model)
    self.browser = Browser(model=browser_model, embedding=browser_embedding)
    self.speak = Speak()
    self.listen = Listen()
    
  # Browser
  def search(self, url, prompt):
    print(self.browser.search(url, prompt))

  def summarize_search(self, url):
    print(self.browser.summarize(url))

  def explain_search(self, url):
    print(self.browser.explain(url))

  # Conversation
  def respond(self, text):
    print(self.conversation.respond(text))

  def explain(self, text):
    print(self.conversation.explain(text))

  def summarize(self, text):
    print(self.conversation.summarize(text))