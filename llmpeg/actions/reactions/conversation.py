import ollama  # TODO: change this to use tinygrad?

# TODO: have a conversation with preprompted character roleplay and play songs on request
# TODO: this should be a in front of browser and call it todo stuff instead of bypassing this and using capabilities directly
class Conversation:     
  explain_prompt: str = "Explain the following data which was extracted from a webpage in your own words"
  summarize_prompt: str = "Summarize the following data which was extracted from a webpage"

  def __init__(self, model: str): self.model, self.messages = model, [] # NOTE: e.g. "gemma:2b"
  
  def summarize(self, prompt: str) -> str: return ollama.generate(model=self.model, prompt=f"{self.summarize_prompt}\n{prompt}")['response']
  def explain(self, prompt: str) -> str: return ollama.generate(model=self.model, prompt=f"{self.explain_prompt}\n{prompt}")['response']
  def respond(self, prompt: str) -> str: return ollama.generate(model=self.model, prompt=prompt)['response']
  
  def clear_chat(self) -> None: self.messages = []
  def _add_message(self, prompt) -> None: return self.messages.append({"role": "user", "content": prompt})
  def chat(self, prompt: str) -> str|list[str]:
    self._add_message(prompt)
    return ollama.chat(model=self.model, messages=self.messages)['message']['content']
