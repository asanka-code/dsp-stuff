import matplotlib.pyplot as plt
import numpy as np
from random import gauss
from scipy.interpolate import UnivariateSpline

# generating dummy temperature data over time
sample = 100000

temp = list()
for i in range(0,sample):
    temp.append(gauss(0,1)) # gauss(mean, std)
y0 = np.array(temp)

temp = list()
for i in range(0,sample):
    temp.append(gauss(0,0.2)) # gauss(mean, std)
y1 = np.array(temp)

temp = list()
for i in range(0,sample):
    temp.append(gauss(2,0.5)) # gauss(mean, std)
y2 = np.array(temp)

# plotting the PDF
p, x = np.histogram(y0, bins=sample)
x = x[:-1] + (x[1] - x[0])/2   # convert bin edges to centers
f = UnivariateSpline(x, p, s=sample)
plt.plot(x, f(x)/sample)

# plotting the PDF
p, x = np.histogram(y1, bins=sample)
x = x[:-1] + (x[1] - x[0])/2   # convert bin edges to centers
f = UnivariateSpline(x, p, s=sample)
plt.plot(x, f(x)/sample)

# plotting the PDF
p, x = np.histogram(y2, bins=sample)
x = x[:-1] + (x[1] - x[0])/2   # convert bin edges to centers
f = UnivariateSpline(x, p, s=sample)
plt.plot(x, f(x)/sample)

#plt.title("PDF of temperature signal")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.legend(['mean=0,std=1', 'mean=0,std=0.2', 'mean=2,std=0.5'], loc='upper left')
plt.show()


