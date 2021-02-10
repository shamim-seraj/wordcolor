from wordcolor import image_processor
import cv2 as cv
from sklearn.cluster import KMeans


def test_calculate_percentage():
    img = cv.imread("./28a838a314a04ea199097db1c1d931ef.jpg")
    print(img.shape)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    clt = KMeans(n_clusters=3)
    clt.fit(img.reshape(-1, 3))
    dict = image_processor.calculate_percentage(clt)
    val_list = sorted(dict.values())
    assert val_list == [26, 30, 43]