
import numpy as np

xx = np.array([[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.8, 0.1, 0.1]])
print(xx)

y1 = np.argmax(xx, axis=1)
print(y1)

y2 = np.argmax(xx, axis=0)
print(y2)

# import matplotlib.pylab as plt
#
# def sigmoid(x):
#     return 1 / (1+np.exp(-x))
#
# def relu(x):
#     return np.maximum(0, x)
#
# x = np.arange(-5.0, 5.0, 0.1)
# y = sigmoid(x)
#
# plt.plot(x,y)
# plt.ylim(-0.5, 1.5)
# plt.show()

# print(y)