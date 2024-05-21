import time
from pathlib import Path

import vlc
import numpy as np

from llmpeg.utils import error


class AudioOutput:
  def __init__(self, audio_output_src: str) -> None:
    self.instance = vlc.Instance(audio_output_src)  # e.g. "--aout=alsa"
    self.player = vlc.MediaPlayer(self.instance)
    self.playing = False

  def stop(self) -> None:
    self.player.stop()
    self.playing = False

  def play(self, tracks: list[str | Path | bytes | np.float32]) -> None:
    try:
      for track in tracks:
        if track:
          self.player.set_media(vlc.Media(track))
          self.player.play()
          while self.player.get_state() == vlc.State.Opening:
            time.sleep(0.1)  # wait for the player to start playing
          while self.player.get_state() not in [
            vlc.State.Ended,
            vlc.State.Error,
          ]:
            time.sleep(0.1)  # wait until playback is finished or an error occurs
    except KeyboardInterrupt:
      self.player.stop()
      self.playing = False
      print('[INFO]: Stopped playback.')
      return
    except TypeError as e:
      self.player.stop()
      self.playing = False
      print(f'[ERROR]: {error(e)}')
      return
    except Exception as e:
      self.player.stop()
      self.playing = False
      print(f'[ERROR]: {error(e)}')
      return
