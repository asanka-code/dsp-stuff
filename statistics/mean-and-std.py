import matplotlib.pyplot as plt
import numpy as np
from random import gauss


# generating a gaussian signal
Fs = 44100
f = 480
sample = 8000
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)

# plotting the signal waveform
plt.hist(y, normed=True)
plt.title("Histogram of sine wave")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

for i in range(sample):
    y[i] = y[i]*gauss(0,1)

# displaying information
print 'mean:' ,np.mean(y)
print 'std:', np.std(y)
print 'SNR:', np.mean(y)/np.std(y)

# plotting the signal waveform
plt.title('Waveform of gaussian signal')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-5, 5)
plt.grid(True)
plt.plot(x, y)
plt.show()

# plotting the histogram
plt.hist(y, normed=True)
plt.title("Histogram of gaussian signal")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


