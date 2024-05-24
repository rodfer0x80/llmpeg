from dataclasses import dataclass

from jsonargparse import CLI

from llmpeg.agent import Agent


@dataclass()
class Main:
  rational_model: str
  trigger_model: str
  speech_model_size: str
  hear_model_size: str

  def __post_init__(self):
    self.agent = Agent(self.rational_model, self.trigger_model, self.speech_model_size, self.hear_model_size)

  def run(self):
    # NOTE: [EDITABLE]

    self.agent.dictate_url('https://example.com/')
    self.agent.summarize_search('https://example.com/')
    # ----------------


def main():
  try:
    CLI(Main)
    return 0
  except KeyboardInterrupt:
    return 0
  except ValueError:
    return 0


if __name__ == '__main__':
  exit(main())
