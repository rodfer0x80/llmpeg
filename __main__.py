#!/usr/bin/env python3

import os

from sakass.agent import Agent

class Main:
  def __init__(self):
    os.environ["DEBUG"] = "1"
    self.agent = Agent(
        conversation_model="gemma:2b",
        nlp_model="punkt",
        tts_model_size="small",
        stt_model_size="tiny"
    )

  def __call__(self):
    url = "https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/waits/test_waits.py"
    #self.agent.explain_search("https://aljamal.substack.com/p/homoiconic-python")
    self.agent.dictate_url(url)
    return 0


if __name__ == '__main__':
  exit(Main()())
