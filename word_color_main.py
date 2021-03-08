"""
This is the driver module
"""


import os
import wordcolor.stat_calculator as sc
import wordcolor.image_processor as ip

# download 20 images in a directory per phrase that are in the data.txt file
ip.download_images(5, "data.txt")

# loop through all the directories and estimate a color for each phrase
dir_list = os.listdir("images")
print("\n\n\nTotal phrases found: ", len(dir_list))
estimated_color_list = []
for directory in dir_list:
    print("\n\nPhrase: ", directory)
    print("=======================")
    color1 = ip.get_common_color("images/" + directory)
    color = ip.get_common_color_v3("images/" + directory)
    estimated_color_list.append(color + " " + directory)

# dump estimated color in a text file
f = open("data_estimated.txt", "a")
for item in estimated_color_list:
    f.write("%s\n" % item)
f.close()

# display the original and the estimated color for each phrase
f = open(r'data.txt', 'r')
original_data = {}
for x in f:
    original_data[x[8:][:-1]] = x[:7]
f.close()

f = open(r'data_estimated.txt', 'r')
estimated_data = {}
for x in f:
    estimated_data[x[8:][:-1]] = x[:7]
f.close()

print("\n\n\nEstimated Colors\n=======================")
for item in estimated_data:
    print(item + " " + original_data[item] + "(orig) " + estimated_data[item] + "(est)")

# calculate difference between the estimation and the original color
print("\n\n\nData Analysis\n==============")
print("Mean Difference: ", sc.calculate_mean(original_data, estimated_data))
print("Standard Deviation: ", sc.calculate_standard_deviation(original_data, estimated_data))
print("Variance: ", sc.calculate_variance(original_data, estimated_data))
