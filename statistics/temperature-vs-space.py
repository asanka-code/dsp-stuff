import matplotlib.pyplot as plt
import numpy as np
from random import gauss

# generating dummy temperature data over space
sample = 10
x = np.arange(sample)

temp = list()
for i in range(0,sample):
    temp.append(gauss(27,0.2)) # gauss(mean, std)
y = np.array(temp)

# plotting the signal waveform
#plt.title('Waveform of temparature signal')
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (C)')
plt.ylim(25, 29)
plt.grid(True)
plt.plot(x, y)
plt.show()

