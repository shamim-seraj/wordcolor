"""
This module deals with image processing
"""

import os
from collections import Counter
import cv2 as cv
import numpy as np
from sklearn.cluster import KMeans


def calculate_percentage(clt):
    """
    :param clt: KMeans cluster object
    :return: percentage of the cluster centers
    """
    n_pixels = len(clt.labels_)
    counter = Counter(clt.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = int(np.round(counter[i] / n_pixels, 2)*100)
    return perc


def get_perc_list(clt):
    """
    :param clt: KMeans cluster object
    :return: percentage of the cluster centers
    """
    n_pixels = len(clt.labels_)
    counter = Counter(clt.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = int(np.round(counter[i] / n_pixels, 2)*100)

    percentage = []
    for key, value in perc.items():
        percentage.append(value)
    return percentage


def get_max_value_index(values):
    """
    :param values: list of values
    :return: index of maximum value
    """
    max_per = max(values.values())
    max_keys = [k for k, v in values.items() if v == max_per]
    return max_keys[0]


def get_common_color_v3(phrase):
    """
    :param phrase: english phrase for which the color to be determined
    :return: the hex code color
    """
    img_list = os.listdir(phrase)
    print("No of images fetched: ", len(img_list))
    if len(img_list) == 0:
        return "No Color Found"
    clt = KMeans(n_clusters=3)
    cluster_data = []
    perc_list = []
    for img_url in img_list:
        url = phrase + "/" + img_url
        print("Applying KMeans on Image : " + url)
        try:
            img = cv.imread(url)
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

            # downscale the image
            scale_percent = 20
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized_img = cv.resize(img, dim, interpolation=cv.INTER_AREA)

            clt.fit(resized_img.reshape(-1, 3))
            perc = get_perc_list(clt)
            perc_list.append(perc)
            cluster_data.append(clt.cluster_centers_)
        except Exception as ex:
            print("Could not read broken image", ex)

    flat_cluster_data = []
    for sublist in cluster_data:
        for item in sublist:
            flat_cluster_data.append(item)
    flat_perc_list = []
    for sublist in perc_list:
        for item in sublist:
            flat_perc_list.append(item)

    if len(flat_cluster_data) == 0:
        return "No Color Found"

    # clustering on top of all cluster centers from 20 images
    print("Applying weighted KMeans on Combined Data of Size: ", len(flat_cluster_data))
    clt.fit(flat_cluster_data, sample_weight=flat_perc_list)
    final_percentage = calculate_percentage(clt)

    # finding the center with max percentage
    max_center_index = get_max_value_index(final_percentage)
    final_col = '#%02x%02x%02x' % tuple([round(x) for x in clt.cluster_centers_[max_center_index]])
    print("Color with Maximum Percentage: ", final_col)
    return final_col
