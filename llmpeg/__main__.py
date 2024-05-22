from dataclasses import dataclass

from jsonargparse import CLI

from llmpeg.agent import Agent

@dataclass
class Main:
  conversation_model: str
  nlp_model: str
  tts_model_size: str
  stt_model_size: str
  
  def __post_init__(self):
    self.agent = Agent(
      conversation_model=self.conversation_model,
      nlp_model=self.nlp_model,
      tts_model_size=self.tts_model_size,
      stt_model_size=self.stt_model_size,
    )

  def run(self):
    # NOTE: [EDITABLE]
    
    self.url = 'https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/waits/test_waits.py'
    self.agent.dictate_url(self.url)

    # ----------------

def main():
  try:
    CLI(Main())
    return 0
  except KeyboardInterrupt:
    return 0
  except ValueError:
    return 0


if __name__ == '__main__':
  exit(main())
