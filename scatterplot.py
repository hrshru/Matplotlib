import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,7,5,6,8,9,3,5,7]
plt.scatter(x,y,label='stars',color='green',marker='*',s=30)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Scattwerplot")
plt.legend()
plt.show()
