import time
import cv2 as cv
import numpy as np
import DuckDuckGoImages as ddg
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
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


def show_img_compar(img_1, img_2):
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off') #hide the axis
    ax[1].axis('off')
    f.tight_layout()
    plt.show()


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


def generate_cluster_centers(img):
    clt = KMeans(n_clusters=3)
    clt.fit(img.reshape(-1, 3))
    print(clt.labels_)
    print(clt.cluster_centers_)


def generate_palette(clusters):
    width=300
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width/clusters.cluster_centers_.shape[0]
    for idx, centers in enumerate(clusters.cluster_centers_):
        palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
    return palette


def get_palette_percentage(clt):
    n_pixels = len(clt.labels_)
    counter = Counter(clt.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i] / n_pixels, 2)
    perc = dict(sorted(perc.items()))
    return perc


def generate_palette_percentage(k_cluster):
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)

    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i] / n_pixels, 2)
    perc = dict(sorted(perc.items()))

    # for logging purposes
    print(perc)
    print(k_cluster.cluster_centers_)

    step = 0

    for idx, centers in enumerate(k_cluster.cluster_centers_):
        palette[:, step:int(step + perc[idx] * width + 1), :] = centers
        step += int(perc[idx] * width + 1)

    return palette


def generate_freq_map(img):
    dim = (500, 300)
    img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    unique, counts = np.unique(img.reshape(-1, 3), axis=0, return_counts=True)
    return unique, counts


