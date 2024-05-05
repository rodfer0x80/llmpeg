#!/usr/bin/env python3

import sys
import os

from sakass.agent import Agent

class Main:
  def __init__(self):
    conversation_model = "gemma:2b"
    browser_model = "gemma:2b"
    browser_embedding = "nomic-embed-text"
    self.agent = Agent(
      conversation_model=conversation_model, 
      browser_model=browser_model, 
      browser_embedding=browser_embedding)
 
  def __call__(self):
    self.agent.search("https://en.wikipedia.org/wiki/Masculinity", "what is masculinity")
    self.agent.summarize_search("https://en.wikipedia.org/wiki/Masculinity")
    self.agent.explain_search("https://en.wikipedia.org/wiki/Masculinity")
    return 0
  

if __name__ == '__main__':
  sys.exit(Main()())
