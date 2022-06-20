import matplotlib.pyplot as plt
import math
import csv
import numpy as np

## Read and plot datafile
csv.reader('out.csv')
t=[]
a=[]
with open('out.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        a.append(float(row[1]))
        t.append(float(row[0]))     
plt.figure(figsize=(12, 12), dpi=80)
plt.scatter(t,a)

plt.show()


            

## Approximate signal to equal intervals of time
N=len(t)
t = np.arange(0,t[len(t)-1],t[len(t)-1]/len(t))

## Calc FFT
fft = np.fft.fft(a)
freqs = np.fft.fftfreq(len(t))

## Plot FFT
T = t[1] - t[0]  # sampling interval 
f = np.linspace(0, 1 / T, N)
plt.figure(figsize=(12, 12), dpi=80)
plt.ylabel("Amplitude")
plt.xlabel("Frequency [Hz]")
plt.xlim(0,2)
x=f[:N // 2]
y=np.abs(fft)[:N // 2] * 1 / N
y[0]=0
plt.plot(x,y)
#plt.plot(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N)
plt.show()

## Print location of dominant amplitude
mY = np.abs((fft)[:N // 2] * 1 / N) # Find magnitude
mY[0]=0 #Scrub the first amplitude to prevent 0 freq as dominant
peakY = np.max(mY) # Find max peak
locY = np.argmax(mY) # Find its location
frqY = f[:N // 2][locY] # Get the actual frequency value
print ("Roll Frequency = "+str(round(frqY,3)))
print ("Roll Period = "+str(round(1/frqY,3)))



