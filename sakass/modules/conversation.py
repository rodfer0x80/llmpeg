from sakass.modules.patterns import Prompts, Triggers
import ollama  # TODO: change this to use tinygrad?
from typing import Union
import asyncio
from ollama import AsyncClient
# TODO: have a conversation with preprompted character roleplay and play songs on request
# TODO: this should be a in front of browser and call it todo stuff instead of bypassing this and using capabilities directly


class Conversation:
  def __init__(self, model: str):
    self.model = model
    self.client = ollama.Client(host='http://localhost:11434')

  def summarize(self, text: str) -> str:
    return ollama.generate(
        model=self.model,
        prompt=f"{Prompts.summarize}\n{text}"
    )

  def explain(self, text: str) -> str:
    return ollama.generate(
        model=self.model,
        prompt=f"{Prompts.explain}\n{text}"
    )

  def respond(self, text: str) -> str:
    return ollama.generate(
        model=self.model,
        prompt=text
    )

  def chat(self, messages: list[dict[str, str]], text: str) -> Union[str, list[str]]:
    messages.append(
        {
            "role": "user",
            "content": text
        }
    )
    res = ollama.chat(
        model=self.model,
        messages=messages,
    )
    return res['message']['content'], messages
