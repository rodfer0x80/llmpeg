#!/usr/bin/env python3

from sakass.agent import Agent


class Main:
  def __init__(self):
    self.agent = Agent(
        conversation_model="gemma:2b",
        stt_model_size="base"
    )

  def __call__(self):
    self.agent.chat()
    return 0


if __name__ == '__main__':
  exit(Main()())
