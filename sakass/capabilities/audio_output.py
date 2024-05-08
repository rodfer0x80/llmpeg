import vlc
from gtts import gTTS

import time
import os
import tempfile
from typing import Optional, List

class AudioOutput:
    def __init__(self, audio_output_config: Optional[str] = None):
        self.instance = vlc.Instance(audio_output_config or "--aout=alsa")
        self.player = vlc.MediaPlayer(self.instance)
        self.playing = False

    #TODO: this tts part should go to modules/tts where stuff is fronted from this class into agent class
    def generate_tts(self, text: str) -> str:
        tts_file = gTTS(text=text, lang="en", slow=False)
        print(text)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        tts_file.save(temp_file.name)
        return temp_file.name

    def play_audio_single(self, audio_file_path: str) -> None:
        if audio_file_path:
            try:
                media = self.instance.media_new(audio_file_path)
                self.player.set_media(media)
                self.player.play()
                time.sleep(0.1)
                while self.player.is_playing():
                    time.sleep(0.5)
            except vlc.VLCException as e:
                print(f"VLC error playing audio: {e}")
            finally:
                if os.path.exists(audio_file_path):
                    os.remove(audio_file_path)

    def text_to_speech(self, text: str) -> None:
        audio_file_path = self.generate_tts(text)
        self.play_audio_single(audio_file_path)

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
