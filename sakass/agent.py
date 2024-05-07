from sakass.capabilities import Speak, Listen
from sakass.modules import Conversation, Browser

class Agent:
  def __init__(self, conversation_model):
    self.conversation = Conversation(model=conversation_model)
    self.browser = Browser()
    self.speak = Speak()
    self.listen = Listen()
    
  # Browser
  def summarize_search(self, url):
    search_content, err = self.browser.scrape(url)
    if err: print(err)
    else: self.summarize(search_content)

  def explain_search(self, url):
    search_content, err = self.browser.scrape(url)
    if err: print(err)
    else: self.explain(search_content)

  # Conversation
  def respond(self, text):
    if not text: return ""
    print(self.conversation.respond(text)['response'])

  def explain(self, text):
    if not text: return ""
    print(self.conversation.explain(text)['response'])

  def summarize(self, text):
    if not text: return ""
    print(self.conversation.summarize(text)['response'])