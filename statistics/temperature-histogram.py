import matplotlib.pyplot as plt
import numpy as np
from random import gauss

# generating dummy temperature data over time
sample = 60
x = np.arange(sample)

temp = list()
for i in range(0,sample):
    temp.append(gauss(27,0.5)) # gauss(mean, std)
y = np.array(temp)

# plotting the signal waveform
#plt.title('Waveform of temparature signal')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (C)')
plt.ylim(25, 29)
plt.grid(True)
plt.plot(x, y)
plt.show()

# plotting the histogram
plt.hist(y, normed=True)
#plt.title("Histogram of temperature signal")
plt.xlabel("Temperature (C)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


