"""
This module calculates statistical measures
"""

import math
import numpy as np


def color_diff(color1, color2):
    """
    :param color1: color1 in hex code
    :param color2: color2 in hex code
    :return: distance in floating point value between c1 and c2
    """
    color1 = color1.lstrip('#')
    color2 = color2.lstrip('#')
    rgb1 = tuple(int(color1[i:i+2], 16) for i in (0, 2, 4))
    rgb2 = tuple(int(color2[i:i+2], 16) for i in (0, 2, 4))
    return math.sqrt((rgb1[0] - rgb2[0])**2 + (rgb1[1] - rgb2[1]) ** 2 + (rgb1[2] - rgb2[2]) **2)


def calculate_mean(original_data, estimated_data):
    """
    :param original_data: dictionary of given phrase with hex code color
    :param estimated_data: dictionary of estimated phrase with hex code color
    :return: mean of the differences
    """
    diff = []
    for item in estimated_data:
        diff.append(color_diff(original_data[item], estimated_data[item]))
    return round(np.mean(diff), 2)


def calculate_standard_deviation(original_data, estimated_data):
    """
    :param original_data: dictionary of given phrase with hex code color
    :param estimated_data: dictionary of estimated phrase with hex code color
    :return: standard deviation of the differences
    """
    diff = []
    for item in estimated_data:
        diff.append(color_diff(original_data[item], estimated_data[item]))
    return round(np.std(diff), 2)


def calculate_variance(original_data, estimated_data):
    """
    :param original_data: dictionary of given phrase with hex code color
    :param estimated_data: dictionary of estimated phrase with hex code color
    :return: variance of the differences
    """
    diff = []
    for item in estimated_data:
        diff.append(color_diff(original_data[item], estimated_data[item]))
    return round(np.var(diff), 2)
