"""
This module deals with image processing
"""


import time
from collections import Counter
import os
import multiprocessing
from os import getpid
import cv2 as cv
import numpy as np
import DuckDuckGoImages as ddg
from sklearn.cluster import KMeans


def download_images(img_count, file_path):
    """
    :param img_count: no of images to be downloaded per phrase
    :param file_path: file to look into
    :return: nothing
    """
    data_file = open(file_path, 'r')
    for line in data_file:
        phrase = line[8:][:-1]
        ddg.download(phrase, "images/" + phrase, img_count)
        print("Download completed for: ", phrase)
        print("10s interval")
        time.sleep(10)
    data_file.close()


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


def copy_items_in_list(percentage, centers, cluster_data):
    """
    :param percentage: percentage of the cluster centers
    :param centers: cluster centers
    :param cluster_data: a list of all cluster centers
    :return:
    """
    for key, value in percentage.items():
        for _ in range(value):
            cluster_data.append(centers[key])
    return cluster_data


def get_max_value_index(values):
    """
    :param values: list of values
    :return: index of maximum value
    """
    max_per = max(values.values())
    max_keys = [k for k, v in values.items() if v == max_per]
    return max_keys[0]


def apply_kmeans_on_single_image(img_url):
    """
    :param img_url: image to apply kmeans on
    :return: returns weighted centers
    """
    clt = KMeans(n_clusters=3)
    print(f"Applying KMeans on Image : {img_url} on the process: {getpid()}")
    cluster_data = []
    try:
        img = cv.imread(img_url)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        # downscale the image
        print('Original Dimensions : ', img.shape)
        scale_percent = 20
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized_img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        print('Resized Dimensions : ', resized_img.shape)

        clt.fit(resized_img.reshape(-1, 3))
        percentage = calculate_percentage(clt)
        for key, value in percentage.items():
            for _ in range(value):
                cluster_data.append(clt.cluster_centers_[key])
    except Exception as ex:
        print("Could not read broken image", ex)
    return cluster_data


def get_common_color_v2(phrase):
    """
    :param phrase: english phrase for which the color to be determined
    :return: the hex code color
    """
    img_list = os.listdir(phrase)
    print("No of images fetched: ", len(img_list))
    for idx in range(len(img_list)):
        img_list[idx] = f"{phrase}/{img_list[idx]}"
    pool = multiprocessing.Pool(processes=5)
    output_data = pool.map(apply_kmeans_on_single_image, img_list)
    cluster_data = []
    for cluster in output_data:
        for data in cluster:
            cluster_data.append(data)

    # clustering on top of all cluster centers from 20 images
    print("Applying KMeans on Combined Data of Size: ", len(cluster_data))
    clt = KMeans(n_clusters=3)
    clt.fit(cluster_data)
    print("Final three Colors: ", clt.cluster_centers_)
    final_percentage = calculate_percentage(clt)
    print("Percentage of Colors: ", final_percentage)

    # finding the center with max percentage
    max_center_index = get_max_value_index(final_percentage)
    final_col = '#%02x%02x%02x' % tuple([round(x) for x in clt.cluster_centers_[max_center_index]])
    print("Color with Maximum Percentage: ", final_col)
    return final_col
