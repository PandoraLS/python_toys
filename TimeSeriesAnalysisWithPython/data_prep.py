# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 16:06
# @Author  : sen

def pitch_src_list_class():
    """
    这个函数写的有问题，不要使用
    :return:
    """
    src_file_path = r"C:\Education\code\pytorch_learn\TimeSeriesAnalysisWithPython-master\data\pitch_16000_voice_sort.txt"
    tar_file_path = "C:\Education\code\pytorch_learn\TimeSeriesAnalysisWithPython-master\data\pitch_class"
    count = {}
    with open(src_file_path) as file:
        lines = file.readlines()
        lines.sort(key=lambda x: len(x))
    for line in lines:
        line = line.split()
        count[len(line)] = count.get(len(line), 0) + 1
        with open(tar_file_path + '\len_' + str(len(line)) + '.txt', 'w') as tmp:
            tmp.write('\t\t'.join(line))
            tmp.write('\n')

def pitch_clean():
    """
    清洗数据，提出前2帧差异较大的数据，提升数据集的质量
    Returns:
    """
    pitchL3to1_file = "C:\Education\code\pytorch_learn\TimeSeriesAnalysisWithPython-master\data\pitch_16000_voice_sort.txt"
    target_file = "C:\Education\code\pytorch_learn\TimeSeriesAnalysisWithPython-master\data\pitch_16000_voice_sort_clean.txt"
    tar_file = open(target_file, "w", encoding="utf8")
    count_dict = {}
    with open(pitchL3to1_file) as src_file:
        for line in src_file:
            elems = line.strip().split("\t\t")
            all_data = [int(_) for _ in elems]
            # all_data = [int(elems[i]) for i in range(8)] + [int(elems[i]) for i in range(9,13)]
            max_all_data = max(all_data)
            min_all_data = min(all_data)

            if max_all_data - min_all_data <= 24:
                tar_file.write(line)
                print(line,end='')


if __name__ == '__main__':
    pitch_src_list_class()
    # pitch_clean()

