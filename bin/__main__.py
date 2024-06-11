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
    self.agent = Agent(
      self.rational_model,
      self.trigger_model,
      self.speech_model_size,
      self.hear_model_size,
    )

  def run(self):
    # NOTE: [EDITABLE]

    # self.agent.chat()
    print('0')
    self.agent.summarize_search('https://news.mit.edu/2020/brain-reading-computer-code-1215')
    # self.agent.explain_search('https://news.mit.edu/2020/brain-reading-computer-code-1215')

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
