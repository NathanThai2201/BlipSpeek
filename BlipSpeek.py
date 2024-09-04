import simpleaudio as sa
import os

global_ringtone = "ring1.wav"

def main():
    sound_path = os.path.join(os.path.dirname(__file__), 'sounds', global_ringtone)
    wave_obj = sa.WaveObject.from_wave_file(sound_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing

if __name__ == "__main__":
    main()
