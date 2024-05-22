import time
from dataclasses import dataclass
from pathlib import Path
from typing import Union

import vlc
import numpy as np

from llmpeg.utils import error


@dataclass
class AudioOutput:
  audio_output_src: str  # e.g. "--aout=alsa"
  cache_dir: Path

  def __post_init__(self) -> None:
    self.instance = vlc.Instance(self.audio_output_src, '--verbose=1')
    self.player = vlc.MediaPlayer(self.instance)
    self.playing = False

  def stop(self) -> None:
    self.player.stop()
    self.playing = False

  def play(self, tracks: list[Union[str, Path, bytes, np.float32]]) -> None:
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
