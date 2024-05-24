from dataclasses import dataclass
from typing import Union

import ollama


@dataclass
class LLM:
  model: str  # NOTE: e.g. "gemma:2b"

  def generate(self, prompt: str) -> str:
    return ollama.generate(model=self.model, prompt=prompt)['response']

  def recall_generate(self, prompt: str, messages: list) -> Union[str, list[str]]:
    return ollama.chat(model=self.model, messages=messages)['message']['content']
