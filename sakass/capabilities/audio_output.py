import vlc

import time
import os
from typing import Optional, List


class AudioOutput:
  def __init__(self, audio_output_config: Optional[str] = None):
    self.instance = vlc.Instance(audio_output_config or "--aout=alsa")
    self.player = vlc.MediaPlayer(self.instance)
    self.playing = False

  def play_audio_file(self, audio_file_path: str) -> None:
    err = "File not found."
    if audio_file_path:
      try:
        media = self.instance.media_new(audio_file_path)
        self.player.set_media(media)
        self.player.play()
        time.sleep(0.1)
        while self.player.is_playing():
          time.sleep(0.5)
      except vlc.VLCException as e:
        err = e
        return err
      finally:
        if os.path.exists(audio_file_path):
          os.remove(audio_file_path)
    return err

  def play_audio_stream(self, audio_stream: List[str]) -> None:
    try:
      for audio_url in audio_stream:
        if audio_url:
          self.player.set_media(vlc.Media(audio_url))
          self.player.play()
          while self.player.get_state() == vlc.State.Opening:  # NOTE: wait for the player to start playing
            continue
          while self.player.get_state() != vlc.State.Ended:  # NOTE: wait until playback is finished
            continue
    except KeyboardInterrupt:
      self.player.stop()
      self.playing = False
      return
