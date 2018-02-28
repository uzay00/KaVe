import numpy as np
import matplotlib.pyplot as plt

k = 0.075
M = 100
dt = 0.01
zaman = np.arange(0, 1.1, dt)

I = [1];
for t in range(len(zaman)):
    dI = k * (M - I[t]) * I[t] * dt    
    yeniI = I[t] + dI
    I.append(yeniI)

plt.figure(figsize=(12,8))
plt.plot(I,'g-',markersize=10)
plt.grid(True) 
plt.ylabel('Hastalık Yayılım Modeli'); 
plt.xlabel('t')
plt.legend([r'$\frac{dI}{dt} = k (M- I) I$'], shadow=True, fancybox=True)