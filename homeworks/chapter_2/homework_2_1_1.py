# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AsFqhaF3urgZkkw-8qlW_ZMrWW9OX8yO
"""

#2.1.1
def greetings(a):
  g = "Доброго времени суток, "+ a[0] +' "Человек" ' + a[1] + "!"
  return g
greetings(input().split())