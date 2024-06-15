from dataclasses import dataclass

#TODO: stop using fucking ollama and load models from hf wth torch
@dataclass
class LLM:
  model: str  # NOTE: e.g. "llama3"

  def generate(self, prompt: str) -> str:
    return ""

  def batch_generate(self, prompt: str, messages: list) -> str | list[str]:
    return ""
