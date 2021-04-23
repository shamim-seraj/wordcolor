"""
This is data generation script
"""

import time
import wordcolor.image_processor as ip


def dump_data(data):
    """
    :param data: data to be dumped in file
    :return: nothing
    """
    # dump estimated color in a text file
    file = open("phrase_with_color.txt", "a")
    for item in data:
        file.write("%s\n" % item)
    file.close()


if __name__ == '__main__':
    data_file = open('birds.txt', 'r')
    # print("No of phrases: ")
    estimated_color_list = []
    COUNTER = 1
    for phrase in data_file:
        print(f"Phrase No: {COUNTER}")
        print("===============")
        phrase = phrase[:-1]
        common_color = ip.download_image_and_extract_color(phrase)
        estimated_color_list.append(common_color + " " + phrase)
        print("10s interval\n\n")
        time.sleep(10)

        # if the counter is 100 write to the file
        if COUNTER % 100 == 0:
            dump_data(estimated_color_list)
            estimated_color_list = []
        COUNTER = COUNTER + 1
    data_file.close()
    dump_data(estimated_color_list)
