# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 17:20
# @Author  : sen

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def count_parameters(x_arry, y_arry, sum_n,n, n_arry):

      Par_t = sum_n
      Par_y = np.mean(y_arry)

      Par_sumty = np.sum(y_arry*n_arry)
      Par_sumt2 = np.sum(n_arry**2)

      b = (Par_sumty - Par_y*Par_t)/(Par_sumt2 - Par_t/n*Par_t)
      a = Par_y - b*Par_t/n

      print("参数b的值为:", b)
      print("参数a的值为", a)
      predict(a, b, n)

      x = input('进行差分运算，输入需要对第几期进行差分:')
      x = eval(x)
      count_chafen(a,b,x)

def predict(a, b, n):
    y = a + b*(n+1.0)
    print("%d年预测的利润额为:"%(n+1993), y)

def count_chafen(a,b,x):

    y1 = (a + b*x) - (a + b*(x-1))
    y_1 =(a + b*(x-1))-(a + b*(x-2))
    y2 = y1-y_1
    y_2 = (a + b*(x-1)) - (a + b*(x-2))+(a + b*(x-2)) - (a + b*(x-3))
    y3 = y2-y_2
    print("第%d期的一阶差分为:"%x, y1)
    print("第%d期的二阶差分为:" %x, y2)
    print("第%d期的三阶差分为:" %x, y3)


t = 2.0
sum_n = 0


x_arry = np.array([1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003])
y_arry = np.array([200, 300, 350, 400, 500, 630, 700, 750, 850, 950, 1020])
n = len(y_arry)
# y = a + bt

n_arry = []
for i in range(n+1):
    n_arry.append(i)
    sum_n += i
n_arry.pop(0)
n_arry = np.array(n_arry)

## 绘图
plt.plot(x_arry, y_arry)
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
plt.xlabel("年份", fontproperties = font)
plt.ylabel("利润额", fontproperties = font)
plt.show()

count_parameters(x_arry, y_arry, sum_n, n, n_arry)
