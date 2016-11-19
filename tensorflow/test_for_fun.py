# coding:utf-8
import tensorflow as tf

hello = tf.constant("hi new world")
sess = tf.Session()
print(sess.run(hello))
a = tf.constant(19)
b = tf.constant(7)
print(sess.run(a/b))
