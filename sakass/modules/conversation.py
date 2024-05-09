from sakass.modules.patterns import Prompts, Triggers
import ollama  # TODO: change this to use tinygrad?
from typing import Union
# TODO: have a conversation with preprompted character roleplay and play songs on request
# TODO: this should be a in front of browser and call it todo stuff instead of bypassing this and using capabilities directly


class Conversation:
  def __init__(self, model: str):
    self.model = model  # NOTE: e.g. "gemma:2b"

  def summarize(self, prompt: str) -> str:
    return ollama.generate(
        model=self.model,
        prompt=f"{Prompts.summarize}\n{prompt}"
    )

  def explain(self, prompt: str) -> str:
    return ollama.generate(
        model=self.model,
        prompt=f"{Prompts.explain}\n{prompt}"
    )

  def respond(self, prompt: str) -> str:
    return ollama.generate(
        model=self.model,
        prompt=prompt
    )

  def chat(self, messages: list[dict[str, str]], prompt: str) -> Union[str, list[str]]:
    messages.append({
        "role": "user",
        "content": prompt,
    })
    res = ollama.chat(
        model=self.model,
        messages=messages,
    )
    return res['message']['content'], messages
