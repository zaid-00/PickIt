import sounddevice as sd
import soundfile as sf


class Sound:
    def __init__(self, file_path):
        self.file_path = file_path

    def play_sound(self):
        data, fs = sf.read(self.file_path, dtype='float32')
        sd.play(data, fs)
        status = sd.wait()
