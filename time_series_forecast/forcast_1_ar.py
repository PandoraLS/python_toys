# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 15:50
# @Author  : sen


"""
https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/
自回归（AR）
"""
# AR example
from statsmodels.tsa.ar_model import AutoReg
from random import random
# contrived dataset
data = [x + random() for x in range(1, 100)]
print(data)
# fit model
model = AutoReg(data, lags=1)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat) # [100.31506212]


data2 = [53, 54, 55, 56, 56, 57, 59, 60]
model = AutoReg(data2, lags=1)
model_fit = model.fit()

yhat2 = model_fit.predict(len(data2), len(data2))
print(yhat2)


# tmp = [53, 54, 55, 56, 56, 57, 59, 60]
tmp = [151, 150, 148, 147, 147, 146, 146, 146]
res = []
for i in range(4):
    src_data = tmp
    model = AutoReg(src_data, lags=1)
    model_fit = model.fit()
    yhat = model_fit.predict(len(src_data), len(src_data))
    yhat_value = yhat[0]

    tmp = tmp[1:]
    tmp.append(int(yhat_value))
    res.append(int(yhat_value))
    print(tmp)

print(res)



def predict_forcast(src_list):
    # assert len(src_list) == 8, "src_list should be 8"
    res = []
    tmp = src_list
    for i in range(4):
        src_data = tmp
        model = AutoReg(src_data, lags=1)
        model_fit = model.fit()
        yhat = model_fit.predict(len(src_data), len(src_data))
        yhat_value = yhat[0]

        tmp = tmp[1:]
        tmp.append(int(yhat_value))
        res.append(int(yhat_value))
        # print(tmp)
    return res


if __name__ == '__main__':
    src_list = [65, 65, 66, 66, 66, 66, 66, 67]
    # src_list = [66, 67, 68, 69]
    print(predict_forcast(src_list))