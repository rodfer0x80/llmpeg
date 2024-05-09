#!/usr/bin/env python3

from sakass.agent import Agent


class Main:
  def __init__(self):
    self.agent = Agent(
      conversation_model="gemma:2b",
      nlp_wordlist="punkt",
      audio_output_src="--aout=alsa", 
      tts_lang="en", 
      tts_model_size="small",
      stt_model_size="tiny"
    )

  def __call__(self):
    self.agent.chat()

    return 0


if __name__ == '__main__':
  exit(Main()())
