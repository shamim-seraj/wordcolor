import image_processor as ip
import os
import stat_calculator as sc


def import_data():
    f = open(r'data.txt', 'r')
    data = []
    for x in f:
        data.append((x[:7], x[8:][:-1]))
    f.close()
    return data


if __name__ == '__main__':
    # download 20 images in a directory per phrase that are in the data.txt file
    ip.download_images(20)

    # loop through all the directories and estimate a color for each phrase
    os.listdir()
    print(ip.generate_most_common_color("sky"))
    
    # display the original and the estimated color for each phrase
    
    # calculate difference between the estimation and the original color
    print("Mean: ", sc.calculate_mean())
    print("Standard Deviation: ", sc.calculate_standard_deviation())
    print("Variance: ", sc.calculate_variance())
