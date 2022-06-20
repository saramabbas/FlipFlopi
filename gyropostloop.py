import matplotlib.pyplot as plt
import math
import csv
import numpy as np




j=1
plt.figure(figsize=(12, 12), dpi=80)
while j<10:
    csv.reader('out'+str(j)+'.csv')
    t=[]
    a=[]
    sp=int('33'+str(j))
    
    with open('out'+str(j)+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            a.append(float(row[1]))
            t.append(float(row[0]))     
    plt.subplot(sp)
    plt.xlim(60,90)
    plt.scatter(t,a)
    j=j+1
plt.show()

j=1
plt.figure(figsize=(12, 12), dpi=80)
tt=[]
aa=[]
while j<10:
    csv.reader('out'+str(j)+'.csv')
    t=[]
    a=[]
    
    sp=int('33'+str(j))
    
    with open('out'+str(j)+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            a.append(float(row[1]))
            t.append(float(row[0]))
            aa.append(float(row[1]))
            tt.append(float(row[0])+120*(j-1))


    ## Approximate signal to equal intervals of time
    N=len(t)
    t = np.arange(0,t[len(t)-1],t[len(t)-1]/len(t))
    
    ## Calc FFT
    fft = np.fft.fft(a)
    freqs = np.fft.fftfreq(len(t))
    
    ## Plot FFT
    T = t[1] - t[0]  # sampling interval 
    f = np.linspace(0, 1 / T, N)
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    
    x=f[:N // 2]
    y=np.abs(fft)[:N // 2] * 1 / N
    y[0]=0
    
    print("dominant amplitude")

    
    ## Print location of dominant amplitude
    mY = np.abs((fft)[:N // 2] * 1 / N) # Find magnitude
    mY[0]=0 #Scrub the first amplitude to prevent 0 freq as dominant
    peakY = np.max(mY) # Find max peak
    print("max peak found")
    locY = np.argmax(mY) # Find its location
    frqY = f[:N // 2][locY] # Get the actual frequency value

    
    plt.subplot(sp)
    
    plt.title(("f = "+str(round(frqY,2))))
    plt.xlim(0,2)
    plt.plot(x,y)
    j=j+1
    #plt.plot(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N)
plt.show()

plt.figure(figsize=(12, 12), dpi=80)
plt.scatter(tt,aa)
plt.show()
## Approximate signal to equal intervals of time
N=len(tt)
tt = np.arange(0,tt[len(tt)-1],tt[len(tt)-1]/len(tt))

## Calc FFT
fft = np.fft.fft(aa)
freqs = np.fft.fftfreq(len(tt))

## Plot FFT
plt.figure(figsize=(12, 12), dpi=80)
T = tt[1] - tt[0]  # sampling interval 
f = np.linspace(0, 1 / T, N)
plt.ylabel("Amplitude")
plt.xlabel("Frequency [Hz]")
x=f[:N // 2]
y=np.abs(fft)[:N // 2] * 1 / N
y[0]=0
plt.plot(x,y)
plt.xlim(0,2)
plt.show()
## Print location of dominant amplitude
mY = np.abs((fft)[:N // 2] * 1 / N) # Find magnitude
mY[0]=0 #Scrub the first amplitude to prevent 0 freq as dominant
peakY = np.max(mY) # Find max peak
locY = np.argmax(mY) # Find its location
frqY = f[:N // 2][locY] # Get the actual frequency value
print ("Roll Frequency = "+str(round(frqY,3)))
print ("Roll Period = "+str(round(1/frqY,3)))

