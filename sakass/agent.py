from sakass.capabilities import AudioInput, AudioOutput
from sakass.modules import Conversation, Browser, NLP
from typing import Optional


class Agent:
  def __init__(self, conversation_model: str):
    self.conversation = Conversation(model=conversation_model)
    self.browser = Browser()
    self.nlp = NLP()
    self.audio_output = AudioOutput()
    self.audio_input = AudioInput()

  #NOTE: <-------- Browser -------->
  def summarize_search(self, url: str) -> None:
    search_content, err = self.browser.scrape(url)
    if err:
      print(err)
    else:
      self.summarize(search_content)

  def explain_search(self, url: str) -> None:
    search_content, err = self.browser.scrape(url)
    if err:
      print(err)
    else:
      self.explain(search_content)

  def stream_audio(self, query: str) -> None:
    # TODO: add NLP checks for query to check if playing a song or answering with LLM
    audio_stream, _ = self.browser.search_audio_stream(query)
    if audio_stream:
      self.audio_output.play_audio_stream(audio_stream)
    else:
      print("No audio stream found.")

  #NOTE: <-------- Conversation -------->
  def respond(self) -> None:
    text = self.audio_input.speech_to_text()
    print("user: "+text)
    if text:
      if self.nlp.check_audio_request(text):
        self.stream_audio(text)
      else:
        res = self.conversation.respond(text)['response']
        print("machine: "+res)
        self.audio_output.text_to_speech(res)

  def say(self, text: str) -> None:
    self.audio_output.text_to_speech(text)

  def explain(self, text: str) -> None:
    if not text:
      return
    print(self.conversation.explain(text)['response'])

  def summarize(self, text: str) -> None:
    if not text:
      return
    print(self.conversation.summarize(text)['response'])
