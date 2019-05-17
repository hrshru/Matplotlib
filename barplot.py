import matplotlib.pyplot as plt
x=[1,2,3,4,5,]
y=[34,45,56,54,32]
tick_label=['one','two','three','four','five']
plt.bar(x,y,tick_label=tick_label,width=0.7,color=['red','green','orange','blue','yellow'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('barGraph')
plt.show()
