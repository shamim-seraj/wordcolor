import math
import numpy as np
import DuckDuckGoImages as ddg


def color_diff(c1, c2):
    c1 = c1.lstrip('#')
    c2 = c2.lstrip('#')
    x = tuple(int(c1[i:i+2], 16) for i in (0, 2, 4))
    y = tuple(int(c2[i:i+2], 16) for i in (0, 2, 4))
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) **2)


def import_data():
    f = open(r'data.txt', 'r')
    data = []
    for x in f:
        data.append((x[:7], x[8:][:-1]))
    f.close()
    return data


def convert_color(c):
    return '#FFFFFF'


def calculate_mean(data):
    diff = []
    for x in data:
        diff.append(color_diff(convert_color(x[1]), x[0]))
    return np.mean(diff)


def calculate_standard_deviation(data):
    diff = []
    for x in data:
        diff.append(color_diff(convert_color(x[1]), x[0]))
    return np.std(diff)


def calculate_variance(data):
    diff = []
    for x in data:
        diff.append(color_diff(convert_color(x[1]), x[0]))
    return np.var(diff)


if __name__ == '__main__':
    data = import_data()
    print('Mean: ' + str(round(calculate_mean(data), 2)))
    print('Standard Deviation: ' + str(round(calculate_standard_deviation(data), 2)))
    print('Variance: ' + str(round(calculate_variance(data), 2)))
