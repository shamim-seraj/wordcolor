import time
import cv2 as cv
import numpy as np
import DuckDuckGoImages as ddg
import color_generator as cg


def download_images():
    f = open(r'data.txt', 'r')
    for x in f:
        phrase = x[8:][:-1]
        #download image for each phrase
        #ddg.download(phrase, phrase, 10)
        ddg.download('red tomatoes', 'tomatoes', 3)
        print("Download completed for: ", phrase)
        print("10s interval")
        time.sleep(10)
        break
    f.close()


def generate_freq_map(img):
    dim = (500, 300)
    img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    unique, counts = np.unique(img.reshape(-1, 3), axis=0, return_counts=True)
    # max_index_col = np.argmax(counts, axis=0)
    # print(unique[max_index_col])
    # print(max(counts))
    return unique, counts


if __name__ == '__main__':
    download_images()
    print(cg.cluster_centers)
    print(type(cg.cluster_centers))
    cg.color_generate()
