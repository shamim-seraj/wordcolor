import wordcolor.image_processor as ip
import time


if __name__ == '__main__':
    data_file = open('animals.txt', 'r')
    # print("No of phrases: ")
    estimated_color_list = []
    for phrase in data_file:
        phrase = phrase[:-1]
        common_color = ip.download_image_and_extract_color(phrase)
        estimated_color_list.append(common_color + " " + phrase)
        print("10s interval")
        time.sleep(10)
    data_file.close()

    # dump estimated color in a text file
    f = open("phrase_with_color.txt", "a")
    for item in estimated_color_list:
        f.write("%s\n" % item)
    f.close()