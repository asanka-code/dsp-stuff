from random import gauss
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# generating a gaussian random signal
x = list()
for i in range(0,10000):
    x.append(gauss(0,10)) # gauss(mean, std)
x = np.array(x)

# showing the CDF of a signal
X = np.sort(x)
F = np.array(range(len(x)))/float(len(x))
plt.plot(X, F)
#plt.title("CDF")
plt.xlabel("Value")
plt.ylabel("Cumulative Frequency")
plt.grid(True)
plt.show()

