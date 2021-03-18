# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 16:34
# @Author  : sen

# ARMA example
from statsmodels.tsa.arima_model import ARMA
from random import random
# contrived dataset
data = [random() for x in range(1, 100)]
print(data)
# fit model
model = ARMA(data, order=(2, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat) # [0.49230843]


# data = [53, 54, 55, 56, 56, 57, 59, 60]
# model = ARMA(data, order=(2, 1))
# model_fit = model.fit(disp=False)
# # make prediction
# yhat = model_fit.predict(len(data), len(data))
# print(yhat) # 报错


