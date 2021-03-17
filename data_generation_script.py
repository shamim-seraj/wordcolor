import wordcolor.image_processor as ip
import time


if __name__ == '__main__':
    data_file = open('animals.txt', 'r')
    # print("No of phrases: ")
    estimated_color_list = []
    counter = 1
    for phrase in data_file:
        print(f"Image No: {counter}")
        print("===============")
        phrase = phrase[:-1]
        common_color = ip.download_image_and_extract_color(phrase)
        estimated_color_list.append(common_color + " " + phrase)
        print("10s interval\n\n")
        time.sleep(10)
        counter = counter + 1
    data_file.close()

    # dump estimated color in a text file
    f = open("phrase_with_color.txt", "a")
    for item in estimated_color_list:
        f.write("%s\n" % item)
    f.close()