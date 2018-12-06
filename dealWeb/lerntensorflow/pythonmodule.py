import tensorflow as tf

# 创建变量 W 和 b 节点，并设置初始值
W = tf.Variable([.1], dtype=tf.float32)
b = tf.Variable([-.1], dtype=tf.float32)
# 创建 x 节点，用来输入实验中的输入数据
x = tf.placeholder(tf.float32)
# 创建线性模型
linear_model = W*x + b

# 创建 y 节点，用来输入实验中得到的输出数据，用于损失模型计算
y = tf.placeholder(tf.float32)
# 创建损失模型
loss = tf.reduce_sum(tf.square(linear_model - y))

fw=tf.assign(W,[2.])
fb=tf.assign(b,[1.])

x_train=[1, 2, 3, 6, 8]
y_train=[4.8, 8.5, 10.4, 21.0, 25.3]
optimizer=tf.train.GradientDescentOptimizer(0.001)
train=optimizer.minimize(loss)
# 创建 Session 用来计算模型
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(10000):
        sess.run(train,{x: x_train,y:y_train })
    print('W:%s b:%s loss:%s ' %(sess.run(W),sess.run(b),sess.run(loss,{x: x_train,y:y_train })))
