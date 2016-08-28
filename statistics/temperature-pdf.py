import matplotlib.pyplot as plt
import numpy as np
from random import gauss
from scipy.interpolate import UnivariateSpline

# generating dummy temperature data over time
sample = 3600
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

# plotting the PDF
p, x = np.histogram(y, bins=sample)
x = x[:-1] + (x[1] - x[0])/2   # convert bin edges to centers
f = UnivariateSpline(x, p, s=sample)
plt.plot(x, f(x)/sample)
#plt.title("PDF of temperature signal")
plt.xlabel("Temperature (C)")
plt.ylabel("Probability")
plt.grid(True)
plt.show()


