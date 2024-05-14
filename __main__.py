#!/usr/bin/env python3

from sakass.agent import Agent


class Main:
  def __init__(self):
    self.agent = Agent(
        conversation_model="llama3",
        stt_model_size="base"
    )

  def __call__(self):
    self.agent.explain_search("https://aljamal.substack.com/p/homoiconic-python")

    return 0


if __name__ == '__main__':
  exit(Main()())
