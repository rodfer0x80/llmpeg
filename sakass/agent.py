from sakass.capabilities import AudioInput, AudioOutput
from .modules import Conversation, Browser, NLP, TTS, STT
from sakass.logger import LoggerFactory

from typing import Optional
import time


class Agent:
  def __init__(self, conversation_model: str, stt_model_size: str, tts_model_size: str):
    self.logger = LoggerFactory(log_output="stdout")()
    self.conversation = Conversation(model=conversation_model)
    self.browser = Browser()
    self.nlp = NLP()
    self.tts = TTS(model_size=tts_model_size)
    self.stt = STT(model_size=stt_model_size)
    self.audio_output = AudioOutput()
    self.audio_input = AudioInput()

  # NOTE: <-------- Browser -------->
  def summarize_search(self, url: str) -> None:
    search_content, err = self.browser.scrape(url)
    assert not err, err
    self.summarize(search_content)

  def explain_search(self, url: str) -> None:
    search_content, err = self.browser.scrape(url)
    assert not err, err
    self.explain(search_content)

  def stream_audio(self, query: str) -> None:
    audio_stream, _ = self.browser.search_audio_stream(query)
    # NOTE: convert to list for play_audio_stream
    print(audio_stream)
    audio_stream = [audio_stream] if audio_stream else None
    if audio_stream:
      self.audio_output.play_audio_stream(audio_stream)
    else:
      self.logger.error("No audio stream found.")

  # NOTE: <-------- Audio -------->
  def text_to_speech(self, text: str) -> None:
    audio_path = self.tts.synthesize(text=text)
    audio_stream = [audio_path]
    self.audio_output.play_audio_stream(audio_stream)

   # TODO: this tts part should go to modules/stt where stuff is fronted from this class into agent class
  def speech_to_text(self) -> str:
    self.logger.debug("Recording...")
    audio_stream = self.audio_input.capture_audio()
    self.logger.debug("Finished recording...")
    text = self.stt.audio_to_text(audio_stream)
    return text

  # NOTE: <-------- Conversation -------->
  def chat(self) -> None:
    prompt = ""
    messages = []
    exit_flag = True
    self.logger.info("Starting chat...")
    prompt = self.speech_to_text().strip()
    self.logger.info(f"USER: {prompt}")
    # TODO: this should be a check for a conversation end using NLP
    while not self.nlp.check_goodbye(prompt):
      if exit_flag:
        exit_flag = False
      if self.nlp.check_audio_request(prompt):
        self.logger.debug("Audio request...")
        self.stream_audio(prompt)
        time.sleep(.5)
      else:
        res, messages = self.conversation.chat(
            messages=messages, prompt=prompt)
        self.logger.info(f"AGENT: {res}")
        self.text_to_speech(text=res)
      prompt = self.speech_to_text().strip()
      self.logger.info(f"USER: {prompt}")
    if exit_flag:
      res = self.conversation.respond(prompt)['response']
      self.logger.info(f"AGENT: {res}")
      self.text_to_speech(text=res)

  def respond(self) -> None:
    text = self.speech_to_text().strip()
    self.logger.info(f"USER: {text}")
    if self.nlp.check_audio_request(text):
      self.logger.debug("Audio request...")
      self.stream_audio(text)
      return
    self.logger.debug("Responding...")
    res = self.conversation.respond(text)['response']
    self.logger.info(f"AGENT: {res}")
    self.text_to_speech(res)

  def explain(self, text="") -> None:
    if not text:
      text = self.speech_to_text().strip()
      self.logger.info(f"USER: {text}")
    else:
      self.logger.info(f"USER: __explain__ {text}")
    res = self.conversation.explain(text)['response']
    self.logger.info(f"AGENT: {res}")
    self.text_to_speech(res)

  def summarize(self, text="") -> None:
    if not text:
      text = self.speech_to_text().strip()
      self.logger.info(f"USER: {text}")
    else:
      self.logger.info(f"USER: __summarize__ {text}")
    res = self.conversation.summarize(text)['response']
    self.logger.info(f"AGENT: {res}")
    self.text_to_speech(res)
