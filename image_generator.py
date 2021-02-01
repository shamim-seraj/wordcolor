import time
import cv2 as cv
import numpy as np
import DuckDuckGoImages as ddg


def download_images():
    f = open(r'data.txt', 'r')
    for x in f:
        phrase = x[8:][:-1]
        ddg.download(phrase, phrase, 10)
        print("Download completed for: ", phrase)
        print("10s interval")
        time.sleep(10)
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
    #ddg.download('tomatoes', 'tomatoes', 5)
    #img1 = cv.imread("tomatoes/725fd0a12bc94f0f88f6a689312183ba.jpg")
    #img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)

    #img2 = cv.imread("tomatoes/e18585644d2e4fe68e4be692cdfb1f2a.jpg")
    #img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

    #unique_color_img1 = generate_freq_map(img1)
    #unique_color_img2 = generate_freq_map(img2)

    #col_img1 = []
    #for x in unique_color_img1:
    #    col_img1.append((x[0], x[1], x[2]))
    #col_img2 = []
    #for x in unique_color_img2:
    #    col_img2.append((x[0], x[1], x[2]))
    download_images()
