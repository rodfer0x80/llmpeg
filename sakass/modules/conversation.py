from sakass.modules.patterns import Prompts, Triggers
import ollama  # TODO: change this to use tinygrad?
from typing import Union

# TODO: have a conversation with preprompted character roleplay and play songs on request
# TODO: this should be a in front of browser and call it todo stuff instead of bypassing this and using capabilities directly

class Conversation:
  def __init__(self, model: str):
    self.model = model

  def summarize(self, text: str) -> str:
    return ollama.generate(model=self.model, prompt=f"{Prompts.summarize}\n{text}")

  def explain(self, text: str) -> str:
    return ollama.generate(model=self.model, prompt=f"{Prompts.explain}\n{text}")

  def respond(self, text: str) -> str:
    return ollama.generate(model=self.model, prompt=text)

  def chat(self, text: str) -> Union[int, str]:
    return 0  # TODO: use ollama.chat() feature to chat with the model
