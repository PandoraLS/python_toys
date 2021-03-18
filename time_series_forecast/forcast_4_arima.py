# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 16:37
# @Author  : sen

# ARIMA example
from statsmodels.tsa.arima_model import ARIMA
from random import random
# contrived dataset
data = [x + random() for x in range(1, 100)]
print(data)
# fit model
model = ARIMA(data, order=(1, 1, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data), typ='levels')
print(yhat) # [100.36637647]


data = [53, 54, 55, 56, 56, 57, 59, 60]
# fit model
model = ARIMA(data, order=(2, 1, 2))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data), typ='levels')
print(yhat) #
