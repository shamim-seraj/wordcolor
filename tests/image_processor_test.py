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


def test_copy_items_in_list():
    assert image_processor.copy_items_in_list([3, 4, 2], [10, 20, 30], [10, 20, 30]) == [10, 20, 30, 10, 10, 10, 20, 20, 20, 20, 30, 30]
    assert image_processor.copy_items_in_list([1, 2, 3], [5, 10, 15], []) == [5, 10, 10, 15, 15, 15]
    assert image_processor.copy_items_in_list([1, 1, 1], [10, 20, 30], []) == [10, 20, 30]


def test_get_max_value_index():
    assert image_processor.get_max_value_index({0: 10, 1: 20, 2: 10}) == 1
    assert image_processor.get_max_value_index({0: 20, 1: 20, 2: 10}) == 0
    assert image_processor.get_max_value_index({0: 10, 1: 20, 2: 20}) == 1
