# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 13:59
# @Author  : sen
"""
实现功能：
1 对于单帧丢失，先用缓存区的voice部分滚动预测，如果后面有帧则对前一帧进行更新
2 对于连续voice丢帧情况，先滚动预测，直到后一帧为voice不丢失帧，就对前一帧进行修正
3. 对于从0000开始丢包的帧
    3.1 丢帧部分后面没有连续的2帧voice不丢失帧，就用仅有的那一帧向前复制，如果前面超出缓存区了，就不管了
    3.2 丢帧部分后面有连续的2帧voice丢失帧，就滚动向前预测，如果再往前超出缓存区了，就也不管了
"""

import collections
from pprint import pprint
from SpectralAnalysis import predict_frame_nogroundtruth, fourierExtrapolation

def solve(src_lines, flags):
    window_q, flag_q = collections.deque(src_lines[:6]), collections.deque(flags[:6])
    for i in range(6, len(src_lines)):
        window_q.popleft()
        flag_q.popleft()
        window_q.append(src_lines[i])
        flag_q.append(flags[i])
        # print(window_q, flag_q)
        if flag_q[-1] == 1: # 新进的这一帧丢失的情况
            if window_q[-1] == [288, 288, 288, 288]:
                window_q[-1] = [288, 288, 288, 288]
                src_lines[i] = [288, 288, 288, 288]
            elif window_q[-3] == [288, 288, 288, 288] and flag_q[-2] == 0: # 此时针对的是队列-2帧是voice帧，且前面都是288，-1帧为丢失帧，则用仅有的那一帧向前复制，不过作用不大
                pass
                # j = 0
                # while j < 4:
                #     if src_lines[i - 2 - j] == [288, 288, 288, 288]:
                #         window_q[-(3 + j)] = window_q[-2]
                #         src_lines[i - 2 - j] = window_q[-2]
                #     j += 1
            else:
                train_X = sum([window_q[i] for i in range(5)], []) # 将用于预测的5帧系数准备好并展开
                train_X_2 = [] # 剔除掉预测数据中的288和0
                for train_X_item in train_X:
                    if train_X_item == 288 or train_X_item == 0:
                        continue
                    else:
                        train_X_2.append(train_X_item)

                # train_X = window_q[4:6] # 第4帧和第5帧预测第六帧
                predicted = predict1(train_X_2) # 得到单向预测的结果
                window_q[-1] = predicted
                src_lines[i] = predicted

        elif flag_q[-1] == 0:
            if flag_q[-2] == 0 and window_q[-3] == [288, 288, 288, 288] and window_q[-1] != [0, 0, 0, 0]:
                # 此时的情况是长度为6的队列最后两帧是voice帧，队列前面部分全是288,因为从后往前推不太现实，所以不采用这种方法
                pass
                # window_q.reverse()
                # for j in range(2,6):
                #     train_X = [window_q[j] for j in (j-2, j-1)]
                #     train_X = sum(train_X, [])
                #     predicted = predict1(train_X)
                #     window_q[j] = predicted
                # window_q.reverse()
                # j = 0
                # while j < 6:
                #     if src_lines[i - j] == [288, 288, 288, 288]:
                #         src_lines[i - j] = window_q[-(j+1)]
                #     j += 1

            elif flag_q[-2] == 1 and window_q[-2] != [288, 288, 288, 288] and window_q[-1] != [0, 0, 0, 0]:
                # 利用后一帧voice帧对前一帧进行修正，且前一帧不是288的情况
                # 当前帧非丢失帧voice，前一帧丢失且前一帧不是288，当前帧不是unvoice
                context_X = sum([window_q[i] for i in (3, 5)], [])
                predicted_context  = predict2(context_X)
                window_q[-2] = predicted_context
                src_lines[i - 1] = predicted_context

            elif flag_q[-2] == 1 and window_q[-2] == [288, 288, 288, 288] and window_q[-3] == [0, 0, 0, 0]:
                # 当前帧非丢失voice，前一帧288，再前一帧000，用当前帧对前一帧288进行修正，不过应该没啥作用
                pass
                # context_X = sum([window_q[i] for i in (3, 5)], [])
                # predicted_context = predict2(context_X)
                # window_q[-2] = predicted_context
                # src_lines[i - 1] = predicted_context


def predict1(X):
    # 单向预测模型(能利用前2帧对后文预测)
    # return [-1, -1, -1, -1]
    output = predict_frame_nogroundtruth(X)
    return output

def predict2(X):
    # 前后帧预测模型(能利用前一帧和后一帧对中间帧预测)
    return [-2, -2, -2, -2]

def data_prep():
    for i in range(20):
        # print([i+1, i+1, i+1, i+1], end=", \n")
        print([i, i, i, i], end=", \n")

if __name__ == "__main__":
    print()
    src_lines = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4],

        [5, 5, 5, 5],
        [6, 6, 6, 6],
        [7, 7, 7, 7],
        [8, 8, 8, 8],
        [9, 9, 9, 9],

        [10, 10, 10, 10],
        [11, 11, 11, 11],
        [12, 12, 12, 12],
        [13, 13, 13, 13],
        [0, 0, 0, 0],

        [288, 288, 288, 288],
        [288, 288, 288, 288],
        [288, 288, 288, 288],
        [288, 288, 288, 288],
        [288, 288, 288, 288],

        [14, 14, 14, 14],
        [15, 15, 15, 15],
        [16, 16, 16, 16],
        [17, 17, 17, 17],
        [18, 18, 18, 18],

        [19, 19, 19, 19],
        [20, 20, 20, 20],
        [21, 21, 21, 21],
        [22, 22, 22, 22],
        [0, 0, 0, 0],

        [288, 288, 288, 288],
        [66, 66, 66, 66],
        [288, 288, 288, 288],
        [288, 288, 288, 288],
        [288, 288, 288, 288],

        [24, 24, 24, 24],
        [25, 25, 25, 25],
        [26, 26, 26, 26],
        [27, 27, 27, 27],
        [28, 28, 28, 28]


    ]
    flags = [
        0,0,0,0,0,
        0,1,1,1,0,
        1,0,0,0,0,
        1,1,1,1,1,

        0,1,0,1,0,
        0,1,1,0,0,
        1,0,1,1,1,
        0,0,0,1,0,

    ]
    solve(src_lines, flags)


    print('----------------')
    pprint(src_lines)
    # data_prep()

