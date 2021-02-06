import numpy as np
import math


def color_diff(c1, c2):
    c1 = c1.lstrip('#')
    c2 = c2.lstrip('#')
    x = tuple(int(c1[i:i+2], 16) for i in (0, 2, 4))
    y = tuple(int(c2[i:i+2], 16) for i in (0, 2, 4))
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) **2)


def calculate_mean(original_data, estimated_data):
    diff = []
    for item in estimated_data:
        diff.append(color_diff(original_data[item], estimated_data[item]))
    return round(np.mean(diff), 2)


def calculate_standard_deviation(original_data, estimated_data):
    diff = []
    for item in estimated_data:
        diff.append(color_diff(original_data[item], estimated_data[item]))
    return round(np.std(diff), 2)


def calculate_variance(original_data, estimated_data):
    diff = []
    for item in estimated_data:
        diff.append(color_diff(original_data[item], estimated_data[item]))
    return round(np.var(diff), 2)