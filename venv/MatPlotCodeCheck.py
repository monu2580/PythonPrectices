from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

x3 = [1,12,5]
y3 = [6,5,10]

plt.plot(x,y,'g',label='one', linewidth=5)

plt.plot(x2,y2,'c',label='two', linewidth=5)

plt.plot(x3,y3,'c',label='three', linewidth=5)

plt.title('MyGraph')

plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True,color='k')
plt.show()