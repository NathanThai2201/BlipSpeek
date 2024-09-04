import simpleaudio as sa
import os
import threading
import time

# GLOBAL VARIABLES, ONLY CHANGE THESE
global_tone = "1.wav"
global_speed = 0.05

def playsound(end = 0):
    sound_path = os.path.join(os.path.dirname(__file__), 'sounds', global_tone)
    wave_obj = sa.WaveObject.from_wave_file(sound_path)
    play_obj = wave_obj.play()
    if end == 1:
        play_obj.wait_done()

def main():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Enter a sentence:")
    print("")
    text_input = input('Input:').lower()
    os.system('cls' if os.name=='nt' else 'clear')

    words = text_input.split(' ')
    for word in words:
        print(word)
        for i in range(len(word)):
            if i == len(word)-1:
                playsound(1)
            else:
                playsound(0)
            time.sleep(global_speed)

if __name__ == "__main__":
    main()
