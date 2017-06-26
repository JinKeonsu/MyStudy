# load_mnist
# import sys, os
# sys.path.append(os.pardir)
# from dataset.mnist import load_mnist
#
# (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
#
# print(x_train.shape)
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)

# 3.6.2
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
import numpy as np
import pickle

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)       # array of exp a
    sum_a = np.sum(exp_a)   # sum of array of exp a
    sm = exp_a / sum_a      # softmax array
    return sm

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

# real execution code from here
x, t = get_data()
network = init_network()
batch_size = 100

accuracy_count = 0
# for i in range(len(x)):
for i in range(0, len(x), batch_size):
    # y = predict(network, x[i])
    # p = np.argmax(y)
    #
    # if p == t[i]:
    #     accuracy_count += 1

    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_count += np.sum(p == t[i:i+batch_size])


print("Accuracy:" + str(float(accuracy_count) / len(x)))

print ('-----------------------------------------------')

xx = np.array([[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.8, 0.1, 0.1], [0.2, 0.9, 0.1]])
print(xx)

y1 = np.argmax(xx, axis=1)
print(y1)

y2 = np.argmax(xx, axis=0)
print(y2)