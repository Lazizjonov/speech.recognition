import sounddevice as sd
from matplotlib import pyplot as plt
import time
from numpy import fft

rec = sd.rec(3 * 44100, channels=1, samplerate=44100, dtype='float64')
sd.wait()

plt.plot(rec[:500])
plt.show()

furier = fft.fft(rec)
plt.plot(furier)
plt.show()

sd.play(rec, 44100)
time.sleep(3)
sd.stop()