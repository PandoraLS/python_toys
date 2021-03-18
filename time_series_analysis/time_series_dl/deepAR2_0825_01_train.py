# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 10:18 上午
# @Author  : sen

"""
参考来源：https://www.jianshu.com/p/4cb550302963
pip install gluonts
用于训练并保存模型

TODO:
1. pitch语音并不是连贯的，有没有必要把截断点通过某种差值平滑连起来
2. 能否只使用已有的数据集， DeepAR输入的必然是

"""
from gluonts.model import deepar
from gluonts.dataset import common
from gluonts.dataset.util import to_pandas
from gluonts.model.predictor import Predictor
from gluonts.trainer import Trainer
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
csv_path = '/Users/seenli/Documents/workspace/code/pytorch_learn2/time_series_DL/Twitter_volume_AMZN.csv'
df = pd.read_csv(csv_path,header=0,sep=',')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index(['timestamp'],inplace=True)

# print(df.value[:"2015-04-22 20:47:53"]) # 最后的时间戳是包含[2015-04-22 20:47:53]
# print(df.value[:"2015-04-23 20:47:53"]) # 如果所给时间戳超出了数据的范围的时候就会输出有的数据
# print("开始时间戳", df.index[0]) # start是开始的时间戳，target对应的是对应时间戳的序列信息
data = common.ListDataset([{'start': df.index[0], 'target': df.value[:"2015-04-22 21:00:00"]}], freq='H')#这个数据格式是固定的
# 这里df.index是时间戳，df.value是时间戳对应的值

estimator = deepar.DeepAREstimator(
    freq='H',
    prediction_length=24,
    trainer=Trainer(epochs=50)
)

predictor = estimator.train(training_data=data)

predictor.serialize(Path("/Users/seenli/Documents/workspace/code/pytorch_learn2/time_series_DL/model_save"))
for train_entry, predict_result in zip(data, predictor.predict(data)):
    to_pandas(train_entry)[-60:].plot(linewidth=2)
    predict_result.plot(color='g', prediction_intervals=[50.0, 90.0])
plt.grid(which='both')
plt.show()
##输出预测结果
prediction = next(predictor.predict(data))
print(prediction.mean)
prediction.plot(output_file='graph.png')