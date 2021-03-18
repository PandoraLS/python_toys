# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 16:42
# @Author  : sen

# VAR example
from statsmodels.tsa.vector_ar.var_model import VAR
from random import random
# contrived dataset with dependency
data = list()
for i in range(100):
    v1 = i + random()
    v2 = v1 + random()
    row = [v1, v2]
    data.append(row)
# fit model
model = VAR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.forecast(model_fit.y, steps=1)
print(yhat) # [[100.57274958 100.97782089]]


data = list()
for i in range(92, 100):
    # v1 = i + random()
    # v2 = v1 + random()
    # v3 = v2 + random()
    # v4 = v3 + random()

    v1 = i
    v2 = v1 + 1
    v3 = v2 + 1
    v4 = v3 + 1

    row = [v1, v2, v3, v4]
    data.append(row)
print(data)
# fit model
model = VAR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.forecast(model_fit.y, steps=1)
print(yhat) # [[100. 101. 102. 103.]]

tmp = [53, 54, 55, 56, 56, 57, 59, 60]
data = list()
for i in range(8-3):
    v1 = tmp[i]
    v2 = tmp[i+1]
    v3 = tmp[i+2]
    v4 = tmp[i+3]
    row = [v1, v2, v3, v4]
    data.append(row)
print(data)
model = VAR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.forecast(model_fit.y, steps=1)
print(yhat) #[[56.99723375 58.99861687 59.99861687 58.42461964]]




