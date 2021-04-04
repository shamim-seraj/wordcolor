"""
This module is to test all the functions of the module "image_processor.py"
"""
import cv2 as cv
from sklearn.cluster import KMeans
from wordcolor import image_processor as ip


def test_calculate_percentage():
    """
    :return: nothing
    """
    img = cv.imread("test_image.jpg")
    print(img.shape)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    clt = KMeans(n_clusters=3)
    clt.fit(img.reshape(-1, 3))
    perc_dict = ip.calculate_percentage(clt)
    val_list = sorted(perc_dict.values())
    assert val_list == [26, 30, 43]


def test_get_max_value_index():
    """
    :return: nothing
    """
    assert ip.get_max_value_index({0: 10, 1: 20, 2: 10}) == 1
    assert ip.get_max_value_index({0: 20, 1: 20, 2: 10}) == 0
    assert ip.get_max_value_index({0: 10, 1: 20, 2: 20}) == 1
