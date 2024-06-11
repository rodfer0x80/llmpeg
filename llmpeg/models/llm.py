from dataclasses import dataclass
from typing import Union

import ollama


@dataclass
class LLM:
  model: str  # NOTE: e.g. "llama3"

  def generate(self, prompt: str) -> str:
    return ollama.generate(model=self.model, prompt=prompt)['response']

  def batch_generate(self, prompt: str, messages: list) -> Union[str, list[str]]:
    return ollama.chat(model=self.model, prompt=prompt, messages=messages)['message']['content']
