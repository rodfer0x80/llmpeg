import time
import os

import os

from sakass.logger import LoggerFactory
from sakass.config import Config
from sakass.capabilities.audio.audio import Audio
from sakass.capabilities.networking.browser import Browser
from sakass.senses import Conversation, Browser, NLP, TTS, STT, Vision

class Agent:
  def __init__(self, conversation_model: str, nlp_model: str, tts_model_size: str, stt_model_size: str):
    # TODO: configurable class for customising the agent
    self.cache_dir = os.path.expanduser("~/.cache/sakass")
    os.makedirs(self.cache_dir, exist_ok=True)
    self.logger = LoggerFactory(log_output="stdout")()

    # TODO: make this work and dynamically
    Config()()

    self.audio = Audio(cache_dir=self.cache_dir, audio_output_src="--aout=alsa")
    self.browser = Browser(cache_dir=self.cache_dir)

    self.conversation = Conversation(model=conversation_model)
    self.nlp = NLP(model_name=nlp_model)
    self.stt = STT(model_size=stt_model_size, cache_dir=self.cache_dir)
    self.tts = TTS(model_size=tts_model_size, cache_dir=self.cache_dir)
    self.vision = Vision(browser=self.browser)


  def ocr_url(self, url: str): return self.vision.ocr_stream(self.browser.screenshot(url))
  def dictate_url(self, url: str): self.text_to_speech(" ".join(self.ocr_url(url)))
  # TODO: explain/summ etc on data from ocr_url



  # TODO: all of this shit below is legacy and has to be cleaned up

  # NOTE: <-------- Browser -------->
  def summarize_search(self, url: str) -> None:
    search_content, err = self.browser.scrape(url)
    assert not err, err
    self.summarize(search_content)

  def explain_search(self, url: str) -> None:
    search_content, err = self.browser.scrape(url)
    assert not err, err
    self.explain(search_content)

  def stream_soundtrack(self, query: str) -> None:
    audio_stream, _ = self.browser.search_audio_stream(query)
    # NOTE: convert to list for play_audio_stream
    self.logger.debug(audio_stream)
    audio_stream = [audio_stream] if audio_stream else None
    if audio_stream: self.audio.play_stream(audio_stream)
    else: self.logger.error("No audio stream found.")

  # NOTE: <-------- Audio -------->
  # def text_to_speech(self, text: str) -> None: self.audio.play_stream(self.tts.synthesize_to_stream(text=text))
  def text_to_speech(self, text: str) -> None: self.audio.play_from_file(self.tts.synthesize_to_file(text=text))

  def speech_to_text(self) -> str:
    self.logger.debug("Recording...")
    audio_stream = self.audio.capture_stream()
    self.logger.debug("Finished recording...")
    text = self.stt.audio_to_text(audio_stream)
    return text

  # NOTE: <-------- Conversation -------->
  def chat(self) -> None:
    prompt = ""
    exit_flag = True
    self.logger.info("Starting chat...")
    self.conversation.clear_chat()
    prompt = self.speech_to_text().strip()
    self.logger.info(f"USER: {prompt}")
    # TODO: this should be a check for a conversation end using NLP
    while not self.nlp.check_goodbye(prompt):
      if exit_flag: exit_flag = False
      if self.nlp.check_audio_request(prompt):
        self.logger.debug("Audio request...")
        self.stream_soundtrack(prompt)
        time.sleep(.5)
      else:
        res = self.conversation.chat(prompt=prompt)
        self.logger.info(f"AGENT: {res}")
        self.text_to_speech(text=res)
      prompt = self.speech_to_text().strip()
      self.logger.info(f"USER: {prompt}")
    if exit_flag:
      res = self.conversation.respond(prompt)
      self.logger.info(f"AGENT: {res}")
      self.text_to_speech(text=res)

  def respond(self) -> None:
    text = self.speech_to_text().strip()
    self.logger.info(f"USER: {text}")
    if self.nlp.check_audio_request(text):
      self.logger.debug("Audio request...")
      self.stream_soundtrack(text)
      return
    self.logger.debug("Responding...")
    res = self.conversation.respond(text)
    self.logger.info(f"AGENT: {res}")
    self.text_to_speech(res)

  def explain(self, text="") -> None:
    if not text:
      text = self.speech_to_text().strip()
      self.logger.info(f"USER: {text}")
    else:
      self.logger.info(f"USER: __explain__ {text}")
    res = self.conversation.explain(text)
    self.logger.info(f"AGENT: {res}")
    self.text_to_speech(res)

  def summarize(self, text="") -> None:
    if not text:
      text = self.speech_to_text().strip()
      self.logger.info(f"USER: {text}")
    else:
      self.logger.info(f"USER: __summarize__ {text}")
    res = self.conversation.summarize(text)
    self.logger.info(f"AGENT: {res}")
    self.text_to_speech(res)
