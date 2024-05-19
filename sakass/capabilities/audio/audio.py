from sakass.capabilities.audio.audio_input import AudioInput
from sakass.capabilities.audio.audio_output import AudioOutput

class Audio:
  def __init__(self, cache_dir: str, audio_output_src: str): self.audio_input, self.audio_output = AudioInput(cache_dir=cache_dir), AudioOutput(audio_output_src=audio_output_src)

  def capture_stream(self, duration=5): return self.audio_input.capture_stream(duration)
  def capture_to_file(self, audio_stream, path=""): return self.audio_input.capture_to_file(audio_stream, path)
  
  def play_stream(self, audio_stream): return self.audio_output.play_stream(audio_stream)
  def play_from_file(self, audio_file): return self.audio_output.play_from_file(audio_file)