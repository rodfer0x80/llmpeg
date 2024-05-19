from typing import List
import time
import os

import vlc

from llmpeg.utils import error

class AudioOutput:
    def __init__(self, audio_output_src: str):
        self.instance = vlc.Instance(audio_output_src)  # e.g. "--aout=alsa"
        self.player = vlc.MediaPlayer(self.instance)
        self.playing = False
    
    def play_stream(self, audio_stream: List[str]) -> None:
      try:
        for track in audio_stream:
          if track:
            self.player.set_media(vlc.Media(track))
            self.player.play()      
            while self.player.get_state() == vlc.State.Opening: time.sleep(0.1)  # wait for the player to start playing
            while self.player.get_state() not in [vlc.State.Ended, vlc.State.Error]: time.sleep(0.1)  # wait until playback is finished or an error occurs
      except KeyboardInterrupt:
            self.player.stop()
            self.playing = False
            print("[INFO]: Stopped playback.")
            return
      except TypeError as e:
            self.player.stop()
            self.playing = False
            print(f"[ERROR]: {error(e)}")
            return
      except Exception as e:
            self.player.stop()
            self.playing = False
            print(f"[ERROR]: {error(e)}")
            return
    
    def play_from_file(self, audio_file: os.PathLike) -> None: self.play_stream([audio_file])