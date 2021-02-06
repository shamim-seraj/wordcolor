import time
import cv2 as cv
import numpy as np
import DuckDuckGoImages as ddg
from sklearn.cluster import KMeans
from collections import Counter
import os


def download_images(img_count):
    f = open(r'data.txt', 'r')
    for x in f:
        phrase = x[8:][:-1]
        ddg.download(phrase, "images/" + phrase, img_count)
        print("Download completed for: ", phrase)
        print("10s interval")
        time.sleep(10)
    f.close()


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
        for center in clt.cluster_centers_:
            cluster_data.append(center)
        # show_img_compar(img, generate_palette_percentage(clt))
    # clustering on top of all cluster centers from 20 images
    print("Size of cluster_data: ", len(cluster_data))
    clt.fit(cluster_data)
    n_pixels = len(clt.labels_)
    counter = Counter(clt.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i] / n_pixels, 2)
    perc = dict(sorted(perc.items()))
    print("Final Cluster Centers: ")
    print(clt.cluster_centers_)
    print("Percentage of Centers: ")
    print(perc)

    # finding the max counter value for clusters
    max_per = max(perc.values())
    max_key = [k for k, v in perc.items() if v == max_per]
    # print the cluster center with max counter value
    print("Keys: ")
    print(max_key)
    return '#%02x%02x%02x' % tuple([round(x) for x in clt.cluster_centers_[max_key[0]]])


