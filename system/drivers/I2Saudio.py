from i2saudio import TDeckAudioI2S

player = TDeckAudioI2S(0, pins={'sck': 7, 'ws': 5, 'sd': 6})

def playWav(filename, volume=0.5):
    player.reinitialize_i2s()
    player.play_wav(filename, volume=volume)