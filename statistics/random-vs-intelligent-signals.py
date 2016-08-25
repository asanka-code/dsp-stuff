from random import randint
from random import gauss
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# generating a random signal
def getGaussianRandomSignal():
    x = list()
    for i in range(0,10000):
        x.append(gauss(0,10)) # gauss(mean, std)
    return np.array(x)

# generating a random signal
def getUniformRandomSignal():
    x = list()
    for i in range(0,10000):
        x.append(randint(0,100))
    return np.array(x)

# read a signal from a Wav file
def getIntelligentSignal():
    fs, x= wavfile.read("owl.wav")
    return x

# showing the properties of a signal
def showProperties(x):
    print 'x:', x
    print 'mean:' ,np.mean(x)
    print 'std:', np.std(x)
    print 'SNR:', np.mean(x)/np.std(x)

# showing the histogram of a signal
def showHistogram(x):
    plt.hist(x, normed=True)
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

# showing the CDF of a signal
def showCDF(x):
    X = np.sort(x)
    F = np.array(range(len(x)))/float(len(x))
    plt.plot(X, F)
    plt.title("CDF")
    plt.xlabel("Value")
    plt.ylabel("Cumulative Frequency")
    plt.grid(True)
    plt.show()

uniformSignal = getUniformRandomSignal()
gaussSignal = getGaussianRandomSignal()
intelSignal = getIntelligentSignal()

#showProperties(uniformSignal)
#showProperties(gaussSignal)
#showProperties(intelSignal)

showHistogram(uniformSignal)
showHistogram(gaussSignal)
showHistogram(intelSignal)

#showCDF(uniformSignal)
#showCDF(gaussSignal)
#showCDF(intelSignal)




