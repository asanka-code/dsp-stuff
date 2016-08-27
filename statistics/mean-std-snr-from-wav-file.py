from random import randint
from random import gauss
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# read a signal from a Wav file
fs, data = wavfile.read("owl.wav")
# fs=sample rate, data=signal
# data has a value range from -2^15 to (2^15)-1
# because the data type is int16

# extract data from channel 0 (our wav file is stereo which has two chanels)
data = data[:, 0]
# to extract data from channel 1
#data = data[:, 1]

# showing the properties of the signal
print 'data:', data
print 'mean:' ,np.mean(data)
print 'std:', np.std(data)
print 'SNR:', np.mean(data)/np.std(data)

# showing the waveform of the signal in channel 0
#plt.title("Waveform (channel 0)")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)
plt.xlim(0,140000)
plt.plot(data)
plt.show()

