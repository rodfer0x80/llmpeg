#!/usr/bin/env python3

import sys

from sakass.agent import Agent

class Main:
  def __init__(self):
    conversation_model = "gemma:2b"
    self.agent = Agent(conversation_model=conversation_model)
 
  def __call__(self):
    self.agent.explain_search("https://en.wikipedia.org/wiki/Masculinity")
    return 0
  

if __name__ == '__main__':
  sys.exit(Main()())
