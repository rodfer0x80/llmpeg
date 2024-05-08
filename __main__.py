#!/usr/bin/env python3

from sakass.agent import Agent


class Main:
  def __init__(self):
    conversation_model = "gemma:2b"
    self.agent = Agent(conversation_model=conversation_model)

  def __call__(self):
    self.agent.chat()
    # self.agent.respond()
    # self.agent.stream_audio("play Californication by Red Hot Chili Peppers")
    # self.agent.stream_audio("play On My Way by Sabrina Carpenter")
    # self.agent.explain_search("https://joe-antognini.github.io/machine-learning/steins-paradox")

    return 0


if __name__ == '__main__':
  exit(Main()())
