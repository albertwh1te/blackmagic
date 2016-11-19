# encoding:utf-8
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# The downloaded data is split into three parts, 55,000 data points of training data (mnist.train), 10,000 points of test data (mnist.test), and 5,000 points of validation data (mnist.validation). This split is very important: it's essential in machine learning that we have separate data which we don't learn from so that we can make sure that what we've learned actually generalizes!
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# We describe these interacting operations by manipulating symbolic variables. Let's create one:

# x isn't a specific value. It's a placeholder, a value that we'll input when we ask TensorFlow to run a computation. We want to be able to input any number of MNIST images, each flattened into a 784-dimensional vector. We represent this as a 2-D tensor of floating-point numbers, with a shape [None, 784]. (Here None means that a dimension can be of any length.)

x = tf.placeholder(tf.float32, [None, 784])

 #A Variable is a modifiable tensor that lives in TensorFlow's graph of interacting operations. It can be used and even modified by the computation. For machine learning applications, one generally has the model parameters be Variables.

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# We can now implement our model. It only takes one line!

y = tf.nn.softmax(tf.matmul(x, W) + b)

# One very common, very nice cost function is "cross-entropy." Surprisingly, cross-entropy arises from thinking about information compressing codes in information theory but it winds up being an important idea in lots of areas, from gambling to machine learning. It's defined:

# Hy′(y)=−∑iyi′log⁡(yi)
# Where y is our predicted probability distribution, and y′ is the true distribution (the one-hot vector we'll input). In some rough sense, the cross-entropy is measuring how inefficient our predictions are for describing the truth. Going into more detail about cross-entropy is beyond the scope of this tutorial, but it's well worth understanding.

# To implement cross-entropy we need to first add a new placeholder to input the correct answers:

y_ = tf.placeholder(tf.float32, [None, 10])

# Then we can implement the cross-entropy, −∑y′log⁡(y):

cross_entropy = -tf.reduce_sum(y_*tf.log(y))

# Now that we know what we want our model to do, it's very easy to have TensorFlow train it to do so. Because TensorFlow knows the entire graph of your computations, it can automatically use the backpropagation algorithm to efficiently determine how your variables affect the cost you ask it minimize. Then it can apply your choice of optimization algorithm to modify the variables and reduce the cost.
# In this case, we ask TensorFlow to minimize cross_entropy using the gradient descent algorithm with a learning rate of 0.01. Gradient descent is a simple procedure, where TensorFlow simply shifts each variable a little bit in the direction that reduces the cost. But TensorFlow also provides many other optimization algorithms: using one is as simple as tweaking one line.

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# Now we have our model set up to train. One last thing before we launch it, we have to add an operation to initialize the variables we created:

init = tf.initialize_all_variables()

# We can now launch the model in a Session, and run the operation that initializes the variables:

sess = tf.Session()
sess.run(init)

# Let's train -- we'll run the training step 1000 times!
# Each step of the loop, we get a "batch" of one hundred random data points from our training set. We run train_step feeding in the batches data to replace the placeholders.

for i in range(100):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# Well, first let's figure out where we predicted the correct label. tf.argmax is an extremely useful function which gives you the index of the highest entry in a tensor along some axis. For example, tf.argmax(y,1) is the label our model thinks is most likely for each input, while tf.argmax(y_,1) is the correct label. We can use tf.equal to check if our prediction matches the truth.

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

