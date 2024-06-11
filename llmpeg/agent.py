import time
from dataclasses import dataclass
from pathlib import Path

from pylogger import LoggerToStdout

from llmpeg.config import Config
from llmpeg.capabilities.audio.audio import Audio
from llmpeg.capabilities.network.network import Network
from llmpeg.capabilities.clipboard import Clipboard
from llmpeg.actions.actions import Actions
from llmpeg.types import URL
from llmpeg.capabilities.filesystem import FileCacheDirectory


@dataclass
class Agent:
  rational_model: str
  trigger_model: str
  speech_model: str
  hear_model: str

  def __post_init__(self):
    self.cache_dir = FileCacheDirectory().__repr__()
    # TODO: configurable class for customising the agent
    Path.mkdir(self.cache_dir, exist_ok=True)

    self.logger = LoggerToStdout()

    # TODO: make this work and dynamically
    Config()

    self.audio = Audio(cache_dir=self.cache_dir)
    self.network = Network(cache_dir=self.cache_dir)

    self.actions = Actions(
      self.cache_dir,
      self.rational_model,
      self.trigger_model,
      self.speech_model,
      self.hear_model,
    )
    print('finished actions')

  # NOTE: <-------- Vision -------->
  def ocr_url(self, url: URL):
    ss_path: Path = self.network.browser.save_screenshot(url)
    prediction = self.actions.vision.ocr(ss_path)
    return prediction

  def dictate_url(self, url: str):
    text = ' '.join(self.ocr_url(url))
    self.text_to_speech(text)

  # TODO: explain/summ etc on data from ocr_url

  # NOTE: <-------- Browser -------->
  def summarize_search(self, url: str) -> None:
    print('1')
    search_content, _ = self.network.scrape(url)
    print('2')
    self.summarize(search_content)
    print('3')

  def explain_search(self, url: str) -> None:
    search_content, _ = self.network.scrape(url)
    self.explain(search_content)

  def chat_search(self) -> None:
    url = Clipboard().copy_from_clipboard()
    search_content, _ = self.network.scrape(url)
    self.summarize(search_content)

  def stream_soundtrack(self, query: str) -> None:
    audio_stream, err = self.network.find_audio(query)
    if err:
      self.logger.error(err)
      # self.logger.error('No audio stream found.')
      return
    self.logger.debug(audio_stream)
    audio_stream = [audio_stream] if audio_stream else None
    if audio_stream:
      self.audio.play_audio_stream(audio_stream)
    else:
      self.logger.error('No audio stream found.')

  # NOTE: <-------- Audio -------->
  # def text_to_speech(self, text: str) -> None:
  # self.audio.play_stream(self.tts.synthesize_to_stream(text=text))
  def text_to_speech(self, text: str) -> None:
    audio_file = self.actions.speech.synthesize_to_file(text)
    self.audio.play_audio_file(audio_file)

  def speech_to_text(self) -> str:
    self.logger.debug('Recording...')
    audio_stream = self.audio.capture_stream()
    self.logger.debug('Finished recording...')
    text = self.actions.hear.synthesize_to_stream(audio_stream)
    return text

  # NOTE: <-------- Conversation -------->
  def chat(self) -> None:
    prompt = ''
    exit_flag = True
    self.logger.info('Starting chat...')
    self.actions.rational.clear_chat()
    prompt = self.speech_to_text().strip()
    self.logger.info(f'USER: {prompt}')
    # TODO: this should be a check for a conversation end using NLP
    while not self.actions.trigger.check_goodbye(prompt):
      if exit_flag:
        exit_flag = False
      if self.actions.trigger.check_browse_request(prompt):
        self.logger.debug('Search request... ' + prompt)
        self.chat_search(prompt)
      elif self.actions.trigger.check_explain_request(prompt):
        self.logger.debug('Explain request... ' + prompt)
        self.explain(prompt)
      elif self.actions.trigger.check_summarize_request(prompt):
        self.logger.debug('Summarize request... ' + prompt)
        self.summarize(prompt)
      elif self.actions.trigger.check_audio_request(prompt):
        self.logger.debug('Audio request...')
        self.stream_soundtrack(prompt)
        time.sleep(0.5)
      else:  # TODO: we need a wait feature for when the user
        # TODO:  is doing something else
        res = self.actions.rational.chat(prompt=prompt)
        self.logger.info(f'AGENT: {res}')
        self.text_to_speech(text=res)
      prompt = self.speech_to_text().strip()
      self.logger.info(f'USER: {prompt}')
    if exit_flag:
      res = self.actions.rational.chat(prompt)
      self.logger.info(f'AGENT: {res}')
      self.text_to_speech(text=res)

  def respond(self) -> None:
    text = self.speech_to_text().strip()
    self.logger.info(f'USER: {text}')
    if self.actions.trigger.check_audio_request(text):
      self.logger.debug('Audio request...')
      self.stream_soundtrack(text)
      return
    self.logger.debug('Responding...')
    res = self.actions.rational.respond(text)
    self.logger.info(f'AGENT: {res}')
    self.text_to_speech(res)

  def explain(self, text='') -> None:
    if not text:
      text = self.speech_to_text().strip()
      self.logger.info(f'USER: {text}')
    else:
      self.logger.info(f'USER: __explain__ {text}')
    res = self.actions.rational.explain(text)
    self.logger.info(f'AGENT: {res}')
    self.text_to_speech(res)

  def summarize(self, text='') -> None:
    if not text:
      text = self.speech_to_text().strip()
      self.logger.info(f'USER: {text}')
    else:
      self.logger.info(f'USER: __summarize__ {text}')
    res = self.actions.rational.summarize(text)
    self.logger.info(f'AGENT: {res}')
    self.text_to_speech(res)
