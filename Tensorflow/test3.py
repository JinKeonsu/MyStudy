import tensorflow as tf

hello = tf.constant("Hello, tensorFlow")
sess = tf.Session()

print(sess.run(hello))
