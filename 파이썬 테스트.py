# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)
# 파이썬 테스트

'''
import tensorflow as tf

with tf.compat.v1.Session() as sess:
  h = tf.constant("Hello")
  w = tf.constant("World!")
  hw = h + w
  ans = sess.run(hw)
  print(ans)
'''

a=""
try:
  a="k"
  raise Exception('test exception raise')
except:
  print(a)