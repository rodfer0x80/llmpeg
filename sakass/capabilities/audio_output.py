import vlc
import signal

#TODO: convert txt to audio and play live during conversation
class AudioOutput:
    def __init__(self):
        self.player = vlc.MediaPlayer()
        # TODO: this should be a config option or probed
        self.instance = vlc.Instance("--aout=alsa")
        self.playing = False

    def play_audio_stream(self, audio_stream):
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
            return 0
