#!/usr/bin/env python3

from sakass.agent import Agent


class Main:
  def __init__(self):
    self.agent = Agent(
        conversation_model="llama3",
        tts_model_size="large",
        stt_model_size="base"
    )

  def __call__(self):
    self.agent.explain_search("https://aljamal.substack.com/p/homoiconic-python")
    #self.agent.chat()
    return 0


if __name__ == '__main__':
  exit(Main()())
