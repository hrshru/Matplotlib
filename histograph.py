import matplotlib.pyplot as plt
age=[20,22,34,54,34,22,36,41,35,23,24,37,43,56,12,23,43,33]
range=(0,100)
bins=10
plt.hist(age,bins,range,color='green',histtype='bar',rwidth=0.7)
plt.xlabel('ages')
plt.ylabel('y-axis')
plt.title('histogram-plot')
plt.show()
