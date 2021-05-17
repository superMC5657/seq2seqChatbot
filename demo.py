# -*- coding: utf-8 -*-
# !@time: 2021/5/18 上午2:03
# !@author: superMC @email: 18758266469@163.com
# !@fileName: demo.py


import tensorflow as tf

a = tf.random.uniform([1, 1, 256])
b = tf.random.uniform([1, 20, 256])
print(a + b)
