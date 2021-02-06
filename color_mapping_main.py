import image_processor as ip
import os
import stat_calculator as sc


if __name__ == '__main__':
    # download 20 images in a directory per phrase that are in the data.txt file
    ip.download_images(20)

    # loop through all the directories and estimate a color for each phrase
    dir_list = os.listdir("images")
    print(dir_list)
    estimated_color_list = []
    for directory in dir_list:
        estimated_color_list.append(ip.generate_most_common_color("images/" + directory) + " " + directory)

    # dump estimated color in a text file
    f = open("data_estimated.txt", "a")
    for item in estimated_color_list:
        f.write("%s\n" % item)
    f.close()

    # display the original and the estimated color for each phrase


    # calculate difference between the estimation and the original color
    #print("Mean: ", sc.calculate_mean())
    #print("Standard Deviation: ", sc.calculate_standard_deviation())
    #print("Variance: ", sc.calculate_variance())
