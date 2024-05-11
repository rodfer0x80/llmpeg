import os
from typing import List

import vlc
# import pygame

class AudioOutput:
  def __init__(self, audio_output_src="--aout=alsa"):
    self.instance = vlc.Instance(audio_output_src)  # NOTE: e.g. "--aout=alsa"
    self.player = vlc.MediaPlayer(self.instance)
    self.playing = False
    # pygame.mixer.init()

  # def play_audio_file(self, audio_file_path: str, delete=False) -> None:
  #   pygame.mixer.music.load(audio_file_path)
  #   pygame.mixer.music.play()
  #   clock = pygame.time.Clock()
  #   while pygame.mixer.music.get_busy(): clock.tick(30)  
  #   if delete: os.remove(audio_file_path)

  def play_audio_stream(self, audio_stream: List[str]) -> None:
    try:
      for audio_url in audio_stream:
        if audio_url:
          self.player.set_media(vlc.Media(audio_url))
          self.player.play()
          while self.player.get_state() == vlc.State.Opening: continue # NOTE: wait for the player to start playing
          while self.player.get_state() != vlc.State.Ended: continue  # NOTE: wait until playback is finished  
    except KeyboardInterrupt:
      self.player.stop()
      self.playing = False
      return
