from sakass.capabilities import AudioInput, AudioOutput
from sakass.modules import Conversation, Browser, NLP, TTS, STT
from sakass.logger import LoggerToStdout

from typing import Optional

class Agent:
  def __init__(self, conversation_model: str):
    self.logger = LoggerToStdout()
    self.conversation = Conversation(model=conversation_model)
    self.browser = Browser()
    self.nlp = NLP()
    self.tts = TTS()
    self.stt = STT()
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
    audio_stream = [audio_stream] if audio_stream else None # NOTE: convert to list for play_audio_stream
    if audio_stream:
      self.audio_output.play_audio_stream(audio_stream)
    else:
      self.logger.error("No audio stream found.")

  #NOTE: <-------- Audio -------->
  def text_to_speech(self, text: str) -> None:
    audio_file_path = self.tts.text_to_audio(text)
    err = self.audio_output.play_audio_single(audio_file_path)
    # if err: self.logger.error(err)

   # TODO: this tts part should go to modules/stt where stuff is fronted from this class into agent class
  def speech_to_text(self) -> str:
    self.logger.debug("Recording...")
    audio_stream = self.audio_input.capture_audio()
    self.logger.debug("Finished recording...")
    audio_text = self.stt.audio_to_text(audio_stream)
    return audio_text

  # NOTE: <-------- Conversation -------->
  def respond(self) -> None:
    text = self.speech_to_text().strip()
    self.logger.info("[USER]: "+text)
    if self.nlp.check_audio_request(text):
      self.logger.debug("Audio request...")
      self.stream_audio(text)
      return 
    self.logger.debug("Responding...")
    res = self.conversation.respond(text)['response']
    self.logger.info("[AGENT]: "+res)
    self.text_to_speech(res)

  def explain(self, text: str) -> None:
    text = self.speech_to_text().strip()
    self.logger.info("[USER]: "+text)
    res = self.conversation.explain(text)['response']
    self.logger.info("[AGENT]: "+res)
    self.text_to_speech(res)

  def summarize(self, text: str) -> None:
    text = self.speech_to_text().strip()
    self.logger.info("[USER]: "+text)
    res = self.conversation.summarize(text)['response']
    self.logger.info("[AGENT]: "+res)
    self.text_to_speech(res)
