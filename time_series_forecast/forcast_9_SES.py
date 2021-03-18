# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 16:47
# @Author  : sen

# SES example
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from random import random
# contrived dataset
data = [x + random() for x in range(1, 100)]
print(data)
# fit model
model = SimpleExpSmoothing(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat) # [99.23471016]


data = [53, 54, 55, 56, 56, 57, 59, 60]
print(data)
# fit model
model = SimpleExpSmoothing(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat) #
