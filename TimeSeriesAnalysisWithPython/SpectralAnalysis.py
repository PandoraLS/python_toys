# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 14:35
# @Author  : sen

import matplotlib.pylab as plt
import numpy as np
from numpy import fft
import pandas as pd


def fourierExtrapolation(x, n_predict):
    # 傅里叶外推法
    n = x.size
    # n_harm = 5  # number of harmonics in model
    n_harm = 3  # number of harmonics in model
    t = np.arange(0, n)
    p = np.polyfit(t, x, 1)  # find linear trend in x
    x_notrend = x - p[0] * t  # detrended x
    x_freqdom = fft.fft(x_notrend)  # detrended x in frequency domain
    f = fft.fftfreq(n)  # frequencies
    indexes = list(range(n))
    # sort indexes by frequency, lower -> higher
    indexes.sort(key=lambda i: np.absolute(f[i]))

    t = np.arange(0, n + n_predict)
    restored_sig = np.zeros(t.size)
    for i in indexes[:1 + n_harm * 2]:
        ampli = np.absolute(x_freqdom[i]) / n  # amplitude
        phase = np.angle(x_freqdom[i])  # phase
        restored_sig += ampli * np.cos(2 * np.pi * f[i] * t + phase)
    return restored_sig + p[0] * t

# x = np.array([669, 592, 664, 1005, 699, 401, 646, 472, 598, 681, 1126, 1260, 562, 491, 714, 530, 521, 687, 776, 802, 499, 536, 871, 801, 965, 768, 381, 497, 458, 699, 549, 427, 358, 219, 635, 756, 775, 969, 598, 630, 649, 722, 835, 812, 724, 966, 778, 584, 697, 737, 777, 1059, 1218, 848, 713, 884, 879, 1056, 1273, 1848, 780, 1206, 1404, 1444, 1412, 1493, 1576, 1178, 836, 1087, 1101, 1082, 775, 698, 620, 651, 731, 906, 958, 1039, 1105, 620, 576, 707, 888, 1052, 1072, 1357, 768, 986, 816, 889, 973, 983, 1351, 1266, 1053, 1879, 2085, 2419, 1880, 2045, 2212, 1491, 1378, 1524, 1231, 1577, 2459, 1848, 1506, 1589, 1386, 1111, 1180, 1075, 1595, 1309, 2092, 1846, 2321, 2036, 3587, 1637, 1416, 1432, 1110, 1135, 1233, 1439, 894, 628, 967, 1176, 1069, 1193, 1771, 1199, 888, 1155, 1254, 1403, 1502, 1692, 1187, 1110, 1382, 1808, 2039, 1810, 1819, 1408, 803, 1568, 1227, 1270, 1268, 1535, 873, 1006, 1328, 1733, 1352, 1906, 2029, 1734, 1314, 1810, 1540, 1958, 1420, 1530, 1126, 721, 771, 874, 997, 1186, 1415, 973, 1146, 1147, 1079, 3854, 3407, 2257, 1200, 734, 1051, 1030, 1370, 2422, 1531, 1062, 530, 1030, 1061, 1249, 2080, 2251, 1190, 756, 1161, 1053, 1063, 932, 1604, 1130, 744, 930, 948, 1107, 1161, 1194, 1366, 1155, 785, 602, 903, 1142, 1410, 1256, 742, 985, 1037, 1067, 1196, 1412, 1127, 779, 911, 989, 946, 888, 1349, 1124, 761, 994, 1068, 971, 1157, 1558, 1223, 782, 2790, 1835, 1444, 1098, 1399, 1255, 950, 1110, 1345, 1224, 1092, 1446, 1210, 1122, 1259, 1181, 1035, 1325, 1481, 1278, 769, 911, 876, 877, 950, 1383, 980, 705, 888, 877, 638, 1065, 1142, 1090, 1316, 1270, 1048, 1256, 1009, 1175, 1176, 870, 856, 860])
# n_predict = 100
# extrapolation = fourierExtrapolation(x, n_predict)
# plt.plot(np.arange(0, x.size), x, 'b', label = 'x', linewidth = 3)
# plt.plot(np.arange(0, extrapolation.size), extrapolation, 'r', label = 'extrapolation')
# plt.legend()
# plt.show()

# x = np.array([151, 150, 148, 147, 147, 146, 146, 146])
# n_predict = 4
# extrapolation = fourierExtrapolation(x[:4], n_predict)
# extrapolation_int = [int(_) for _ in extrapolation]
# print(extrapolation_int)
# plt.plot(np.arange(0, x.size), x, 'b', label = 'x', linewidth = 3)
# plt.plot(np.arange(0, extrapolation.size), extrapolation, 'r', label = 'extrapolation')
# plt.legend()
# plt.show()

def predict_frame(src_list, plot_flag=False):
    """
    实验输入数据长度对傅里叶外推的影响
    :param src_list: 输入的是全部的数据，最后4个数是待预测的
    :param plot_flag: 是否绘图
    :return:
    """
    x = np.array(src_list[:-4])
    n_predict = 4
    extrapolation = fourierExtrapolation(x, n_predict)
    extrapolation_int = [int(_) for _ in extrapolation]
    print("predicted", extrapolation_int[:])
    print("groundtru", src_list[:])
    if plot_flag:
        plt.plot(np.arange(0, len(src_list)), src_list, 'b', label='ground', linewidth=3)
        plt.plot(np.arange(0, extrapolation.size), extrapolation, 'r', label='predict')
        plt.legend()
        plt.show()

def predict_frame_nogroundtruth(src_list, plot_flag=False):
    """
    实验输入数据长度对傅里叶外推的影响
    :param src_list: 输入的是全部的数据，最后4个数是待预测的
    :param plot_flag: 是否绘图
    :return:
    """
    x = np.array(src_list[:])
    n_predict = 4
    extrapolation = fourierExtrapolation(x, n_predict)
    extrapolation_int = [int(_) for _ in extrapolation]
    # print("predicted", extrapolation_int[:-4], extrapolation_int[-4:])
    # print("groundtru", src_list)
    if plot_flag:
        plt.plot(np.arange(0, len(src_list)), src_list, 'b', label='ground', linewidth=3)
        plt.plot(np.arange(0, extrapolation.size), extrapolation, 'r', label='predict')
        plt.legend()
        plt.show()
    return extrapolation_int[-4:]

def rolling_predict_frame(src_list, plot_flag=False):
    res = src_list[:-4]
    x = np.array(src_list[:-4])
    n_predict = 1
    for i in range(4):
        extrapolation = fourierExtrapolation(x, n_predict)
        extrapolation_int = [int(_) for _ in extrapolation]
        res.append(extrapolation_int[-1])
        x = np.array(res[i+1:])
    print("predicted", res[:])
    print("groundtru", src_list[:])
    if plot_flag:
        plt.plot(np.arange(0, len(src_list)), src_list, 'b', label='ground', linewidth=3)
        plt.plot(np.arange(0, len(res)), res, 'r', label='predict')
        plt.legend()
        plt.show()

def rolling_predict_frame_nogroundtruth(src_list, plot_flag=False):
    res = src_list
    x = np.array(src_list)
    n_predict = 1
    for i in range(4):
        extrapolation = fourierExtrapolation(x, n_predict)
        extrapolation_int = [int(_) for _ in extrapolation]
        res.append(extrapolation_int[-1])
        x = np.array(res[:])
    print("predicted", extrapolation_int[:-4], extrapolation_int[-4:])
    print("groundtru", src_list[:-4])
    if plot_flag:
        plt.plot(np.arange(0, len(src_list)), src_list, 'b', label='ground', linewidth=3)
        plt.plot(np.arange(0, len(res)), res, 'r', label='predict')
        plt.legend()
        plt.show()
    return extrapolation_int[-4:]



def predict_from_file():
    src_file_path = "C:\Education\code\pytorch_learn\TimeSeriesAnalysisWithPython-master\data\pitch_16000_voice_sort_clean.txt"
    file = open(src_file_path)
    lines = file.readlines()
    for i in range(len(lines)):
        if 20000 < i and i < 20020:
            line = lines[i].split()
            line = [int(_) for _ in line]
            # predict_frame(line)
            predict_frame_nogroundtruth(line)
            print()

def rolling_predict_from_file():
    src_file_path = "C:\Education\code\pytorch_learn\TimeSeriesAnalysisWithPython-master\data\pitch_16000_voice_sort_clean.txt"
    file = open(src_file_path)
    lines = file.readlines()
    for i in range(len(lines)):
        if 20000 < i and i < 20020:
            line = lines[i].split()
            line = [int(_) for _ in line]
            # rolling_predict_frame(line)
            rolling_predict_frame_nogroundtruth(line)

            print()

if __name__ == '__main__':
    print('---------------------------------------------')
    # src_list = [151, 150, 148, 147, 147, 146, 146, 146]
    # predict_frame(src_list)
    print('---------------------------------------------')
    predict_from_file()
    # rolling_predict_from_file()