import time
import cv2 as cv
import numpy as np
import DuckDuckGoImages as ddg
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from collections import Counter
import os


def show_img_compar(img_1, img_2):
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off') #hide the axis
    ax[1].axis('off')
    f.tight_layout()
    plt.show()


def download_images():
    f = open(r'data.txt', 'r')
    for x in f:
        phrase = x[8:][:-1]
        ddg.download(phrase, phrase, 10)
        print("Download completed for: ", phrase)
        print("10s interval")
        time.sleep(10)
    f.close()


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


def generate_palette_percentage(k_cluster):
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)

    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        print(counter[i])
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


if __name__ == '__main__':
    img_list = os.listdir('tomato')
    clt = KMeans(n_clusters=3)
    cluster_data = []
    for x in img_list:
        img = cv.imread("tomato/" + x)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        clt.fit(img.reshape(-1, 3))
        for z in clt.cluster_centers_:
            cluster_data.append(z)
        show_img_compar(img, generate_palette_percentage(clt))

    print(len(cluster_data))
    clt.fit(cluster_data)
    print(clt.cluster_centers_)
    img = cv.imread("sky/a24acfb8866e4724957e4cdfe026c99b.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    show_img_compar(img, generate_palette_percentage(clt))
    cv.imshow('Result', generate_palette_percentage(clt))

