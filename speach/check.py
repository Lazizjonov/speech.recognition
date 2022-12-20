import sounddevice as sd
from matplotlib import pyplot as plt
import time
from numpy import fft
import soundfile as sf
from numpy import mean
import numpy as np
import os
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

data, info = sf.read("examples/audio_2021-07-27_10-07-33.wav")
# plt.plot(data)
# plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    if( (i + 1) * 2500 < len(data) ):
        arr = mean(data[i*5000:(i*5000)+5000], axis=1)
        arr *= np.hamming(5000)
        fur1 = np.absolute(fft.rfft(arr, 512))
        pow_frames = (1.0 / 512) * ((fur1) ** 2)
        ax1.clear()
        ax1.plot(pow_frames)
        
        sd.play(data[i*5000:(i*5000)+5000])

ani = animation.FuncAnimation(fig, animate, interval=104)

plt.show()