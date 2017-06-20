import tensorflow as tf

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = X * W + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))
#cost = tf.square(hypothesis - y_train)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, w_val, b_val, _ = sess.run([cost, W, b, train], feed_dict={ X:[1, 2, 3], Y:[0.95, 2.0, 3.01]} )
    if step % 20 == 0:
        print(step, cost_val, w_val, b_val)


print('---')
print(sess.run(hypothesis, feed_dict={X:[4]}))
print(sess.run(hypothesis, feed_dict={X:[5.6]}))
print(sess.run(hypothesis, feed_dict={X:[7.2, 8.3]}))
'''
2980 8.89092e-05 [ 1.02983463] [-0.07295763]
3000 8.89066e-05 [ 1.02984214] [-0.07297509]
'''