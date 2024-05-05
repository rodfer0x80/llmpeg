#!/usr/bin/env python3

import sys
import os

from sakass.agent import Agent

class Main:
  def __init__(self):
    conversation_model = os.getenv("CONVERSATION_MODEL", "gemma:2b")
    browser_model = os.getenv("BROWSER_MODEL", "gemma:2b")
    browser_embedding = os.getenv("BROWSER_EMBEDDING", "nomic-embed-text")
    self.agent = Agent(
      conversation_model=conversation_model, 
      browser_model=browser_model, 
      browser_embedding=browser_embedding)
 
  def __call__(self):
    self.test_respond()
    self.test_summarize_url()
    return 0
  
  def test_respond(self):
    self._input = "hi babe"
    self.agent.respond(self._input)

  def test_summarize_url(self):
    url = "https://medium.com/@michaelnau.dev/web-scraping-for-llms-a66818950b26"
    self.agent.summarize_url(url)

if __name__ == '__main__':
  sys.exit(Main()())
