# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qJHeNV1GiwezFmpD_GZiePgvxv1wVMf-
"""

a = int(input())
l = 0
t = 0
f = 0
noneformat = 0
while l < a:
  i = 0
  ii = 0
  m = 0
  n = 0
  s = 0
  j = 0
  da = 0
  net = 0
  three1 = 0
  three2 = 0
  b = input().split()
  s = len(b)
  while j < s:
    if "True" in b[i]:
      m += 1
    elif "False" in b[i]:
      n += 1
    i += 1
    j += 1
# определяет одна ли булевая переменная в строке или нет "da" "net"
  for ii in range(1):
    if n + m == 1:
      da += 1
    else:
      net += 1
# если булевая переменная одна в стрроке выводит "True" или "False"
  for ii in range(1):
    if da == 1:
      t += m
      f += n
# если булевых переменных несколько то сравниваем 4 элемент в строке с "True" или "False"
    elif net == 1:
      if "True" in b[3]:
        three1 += 1
      elif "False" in b[3]:
        three2 += 1
        t += three1
        f += three2
      else:
        noneformat += 1
  l += 1
print(t, f, noneformat)