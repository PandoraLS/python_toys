# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 16:48
# @Author  : sen

# HWES example
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from random import random
# contrived dataset
data = [x + random() for x in range(1, 100)]
# fit model
model = ExponentialSmoothing(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat) # [99.86238233]


data = [53, 54, 55, 56, 56, 57, 59, 60]
print(data)

# fit model
model = ExponentialSmoothing(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat) #