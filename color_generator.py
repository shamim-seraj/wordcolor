import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.cluster import KMeans

cluster_centers = []


def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        #cv.imshow('image', img)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        dim = (500, 300)
        # resize image
        img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        generate_palette(img)
        if img is not None:
            images.append(img)
        print(len(images))
    return images
#folder="directory/folder path"


def palette_perc(k_cluster):
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
    centers = k_cluster.cluster_centers_
    print(centers)
    cluster_centers.append(centers)
    step = 0

    for idx, centers in enumerate(k_cluster.cluster_centers_):
        palette[:, step:int(step + perc[idx] * width + 1), :] = centers
        step += int(perc[idx] * width + 1)

    return palette


def show_img_compar(img_1, img_2 ):
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off') #hide the axis
    ax[1].axis('off')
    f.tight_layout()
    plt.show()


def generate_palette(img):
    clt = KMeans(n_clusters=3)
    clt = clt.fit(img.reshape(-1, 3))
    show_img_compar(img, palette_perc(clt))

#generate most common color


def color_generate():
    center_array = np.asarray(cluster_centers)
    print(center_array)
    #kmeans = KMeans(n_clusters=3)
    #kmeans.fit(center_array)
    #print(kmeans.cluster_centers_)


