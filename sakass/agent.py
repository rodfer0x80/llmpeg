from .capabilities import Speak, Listen
from .modules import Conversation, Browser

class Agent:
  def __init__(self, conversation_model, browser_model, browser_embedding):
    self.conversation = Conversation(model=conversation_model)
    self.browser = Browser(model=browser_model, embedding=browser_embedding)
    self.speak = Speak()
    self.listen = Listen()
    
  def respond(self, text):
    print(self.conversation.respond(text))

  def summarize(self, text):
    print(self.conversation.summarize(text))

  def summarize_url(self, url):
    self.browser.summarize_url(url)
