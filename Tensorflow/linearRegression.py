import tensorflow as tf

x_train = [1, 2, 3]
#y_train = [1, 2, 3]
y_train = [0.95, 2.0, 3.01]

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = x_train * W + b

cost = tf.reduce_mean(tf.square(hypothesis - y_train))
#cost = tf.square(hypothesis - y_train)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()

sess.run(tf.global_variables_initializer())

for step in range(3001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))




'''
2980 8.89092e-05 [ 1.02983463] [-0.07295763]
3000 8.89066e-05 [ 1.02984214] [-0.07297509]
'''