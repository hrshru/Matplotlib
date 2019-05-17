import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0.0,2.0,0.01)
s=1+np.cos(2*np.pi*t)
plt.plot(t,s, '--')
plt.xlabel('time')
plt.ylabel('frequency')
plt.title('cosine wave')
plt.grid()
plt.show()
