import matplotlib.pyplot as plt
activity=['sleep','eat','reading','play','runing']
slices=[5,6,3,7,2]
color=['r','g','m','b','y']
plt.pie(slices, labels=activity, colors=color,startangle=90, shadow=True,explode=(0,0.2,0,0,0),autopct='%1.2f%%')

plt.legend()
plt.show()
