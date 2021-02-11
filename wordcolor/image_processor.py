import time
import cv2 as cv
import numpy as np
import DuckDuckGoImages as ddg
from sklearn.cluster import KMeans
from collections import Counter
import os


def download_images(img_count):
    f = open(r'../data.txt', 'r')
    for x in f:
        phrase = x[8:][:-1]
        ddg.download(phrase, "images/" + phrase, img_count)
        print("Download completed for: ", phrase)
        print("10s interval")
        time.sleep(10)
    f.close()


def calculate_percentage(clt):
    n_pixels = len(clt.labels_)
    counter = Counter(clt.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = int(np.round(counter[i] / n_pixels, 2)*100)
    return perc


def copy_items_in_list(percentage, centers, cluster_data):
    for i in range(len(percentage)):
        for j in range(percentage[i]):
            cluster_data.append(centers[i])
    return cluster_data


def get_max_value_index(values):
    max_per = max(values.values())
    max_keys = [k for k, v in values.items() if v == max_per]
    return max_keys[0]


def generate_most_common_color(phrase):
    img_list = os.listdir(phrase)
    print("No of images fetched: ", len(img_list))
    clt = KMeans(n_clusters=3)
    cluster_data = []
    for img_url in img_list:
        url = phrase + "/" + img_url
        print("Image URL: " + url)
        img = cv.imread(url)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        clt.fit(img.reshape(-1, 3))
        percentage = calculate_percentage(clt)
        cluster_data = copy_items_in_list(percentage, clt.cluster_centers_, cluster_data)

    # clustering on top of all cluster centers from 20 images
    print("Size of cluster_data: ", len(cluster_data))
    clt.fit(cluster_data)
    print("Final Cluster Centers: ", clt.cluster_centers_)
    final_percentage = calculate_percentage(clt)
    print("Percentage of Centers: ", final_percentage)

    # finding the center with max percentage
    max_center_index = get_max_value_index(final_percentage)
    print("Maximum Percentage Center Index: ", max_center_index)
    return '#%02x%02x%02x' % tuple([round(x) for x in clt.cluster_centers_[max_center_index]])
