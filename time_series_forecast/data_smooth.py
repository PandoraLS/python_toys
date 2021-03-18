# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 17:05
# @Author  : sen
"""

pandas的多项式预测：
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter

# x = np.linspace(0,2*np.pi,100)
# y = np.sin(x) + np.random.random(100) * 0.2
# yhat = savgol_filter(y, 51, 3) # window size 51, polynomial order 3
# plt.plot(x,y)
# plt.plot(x,yhat, color='red')
# plt.show()

# x1 = np.array([63, 65, 67, 69, ])
#


# x = [57,58, 60, 61, 63, 65, 67, 69, np.nan, np.nan, np.nan,  np.nan, np.nan, np.nan, 79, 80, 80, 81]
# x = [57,58, 60, 61,
#      63, 65, 67, 69,
#      np.nan, np.nan, np.nan, np.nan,
#      np.nan, np.nan]

# x = [63, 65, 67, 69, 82, 82, 82, 81]
# x = [97, 101, 104, 108, 122, 124, 124, 126]
# x = [107, 107, 107, 106, 108, 109, 110, 111]
x = [107, 107, 107, 106, 108, 109, 110, 111]
# x2 = x[:4] + [np.nan, np.nan, np.nan, np.nan]*4 + x[4:]
x2 = x[:4] + [np.nan, np.nan, np.nan, np.nan]*0 + x[4:]
print(x2)
# x2 = [95, 95, 95, 95,
#     np.nan, np.nan, np.nan, np.nan,
#       99, 100, 101, 102]
s = pd.Series(x2)
# tmp = s.interpolate(method='polynomial', limit_direction='both', order=2)
# tmp = [int(_) for _ in tmp]
# print(tmp)
#
#
# tmp = s.interpolate(method='spline', limit_direction='both', order=3)
# tmp = [int(_) for _ in tmp]
# print(tmp)


tmp = s.interpolate(method='slinear')
tmp2 = [int(_) for _ in tmp]
print(tmp2[4:8])
print(tmp2)

"""
可用的方法
linear
nearest
slinear
quadratic
cubic
barycentric
krogh
piecewise_polynomial
akima
pchip
from_derivatives
polynomial order=2
polynomial order=3
polynomial order=4
spline order=2
spline order=3
spline order=4
"""


