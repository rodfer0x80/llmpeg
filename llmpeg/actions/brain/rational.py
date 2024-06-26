from dataclasses import dataclass
from typing import Union

from llmpeg.models.llm import LLM


# TODO: have a conversation with preprompted character roleplay
# TODO: and play songs on request
# TODO: this should be a in front of browser and call it todo stuff
# TODO: instead of bypassing this and using capabilities directly


# TODO: build ollama models for this 1 small 1 large
@dataclass
class BrainRational:
  model: str  # NOTE: e.g. "gemma:2b"
  explain_prompt: str = 'Explain the following data which was extracted' + ' ' + 'from a webpage in your own words'
  summarize_prompt: str = 'Summarize the following data which was extracted' + ' ' + 'from a webpage'

  # TODO: sqlite3 for storing chat history
  def __post_init__(self) -> None:
    self.chat_messages = []
    self.llm = LLM(self.model)

  def summarize(self, prompt: str) -> str:
    return self.llm.generate(f'{self.summarize_prompt}\n{prompt}')

  def explain(self, prompt: str) -> str:
    return self.llm.generate(f'{self.explain_prompt}\n{prompt}')

  def respond(self, prompt: str) -> str:
    return self.llm.generate(prompt)

  def clear_chat(self) -> None:
    self.chat_messages = []

  def _add_message(self, prompt) -> None:
    return self.chat_messages.append({
      'role': 'user',
      'content': prompt,
    })

  def chat(self, prompt: str) -> Union[str, list[str]]:
    self._add_message(prompt)
    message = self.chat_messages[-1]['content']
    return self.llm.batch_generate(message, self.chat_messages)
