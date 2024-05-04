#!/usr/bin/env python3

import sys

from sakass.agent import Agent

class Main:
  def __init__(self):
    self.agent = Agent(conversation_model="gemma:2b", browser_model="gemma:2b")
 
  def __call__(self):
    self.test_complete()
    self.test_summarize()
    return 0
  
  def test_complete(self):
    self._input = "hi babe"
    self.agent.respond(self._input)

  def test_summarize(self):
    url = "https://medium.com/@michaelnau.dev/web-scraping-for-llms-a66818950b26"
    self.agent.summarize_url(url)

if __name__ == '__main__':
  sys.exit(Main()())
