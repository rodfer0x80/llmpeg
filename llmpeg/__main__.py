from jsonargparse import CLI

from llmpeg.agent import Agent


class Main:
  def __init__(self):
    self.conversation_model = 'gemma:2b'
    self.nlp_model = 'punkt'
    self.tts_model_size = 'small'
    self.stt_model_size = 'tiny'

    # NOTE: [EDITABLE]
    self.url = 'https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/waits/test_waits.py'

    # ----------------

  def run(self):
    self.agent = Agent(
      conversation_model=self.conversation_model,
      nlp_model=self.nlp_model,
      tts_model_size=self.tts_model_size,
      stt_model_size=self.stt_model_size,
    )

    # NOTE: [EDITABLE]
    self.agent.dictate_url(self.url)

    # ----------------

  def __call__(self):
    self.run()
    return 0


def main():
  try:
    CLI(Main()())
    return 0
  except KeyboardInterrupt:
    return 0
  except ValueError:
    return 0


if __name__ == '__main__':
  exit(main())
