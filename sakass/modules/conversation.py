from sakass.modules.patterns import Prompts, Triggers
import ollama  # TODO: change this to use tinygrad?
from typing import Union
# TODO: have a conversation with preprompted character roleplay and play songs on request
# TODO: this should be a in front of browser and call it todo stuff instead of bypassing this and using capabilities directly


class Conversation:
  def __init__(self, model: str): 
    self.model = model  # NOTE: e.g. "gemma:2b"
    self.messages = []

  def summarize(self, prompt: str) -> str: return ollama.generate(model=self.model, prompt=f"{Prompts.summarize}\n{prompt}")['response']
  def explain(self, prompt: str) -> str: return ollama.generate(model=self.model, prompt=f"{Prompts.explain}\n{prompt}")['response']
  def respond(self, prompt: str) -> str: return ollama.generate(model=self.model, prompt=prompt)['response']
  
  def clear_chat(self) -> None: self.messages = []
  def _add_message(self, prompt) -> None: return self.messages.append({"role": "user", "content": prompt})
  def chat(self, prompt: str) -> Union[str, list[str]]:
    self._add_message(prompt)
    return ollama.chat(model=self.model, messages=self.messages)['message']['content']
