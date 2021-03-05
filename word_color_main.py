"""
This is the driver module
"""


import wordcolor.image_processor as ip
import DuckDuckGoImages as ddg
import turtle


def populate_output_window(eng_phrase, color):
    t = turtle.Turtle()
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    style = ('Courier', 30, 'italic')
    t.setposition(0, -50)
    t.write(eng_phrase, font=style, align='center')
    turtle.done()


if __name__ == '__main__':
    phrase = input("Enter the phrase: ")
    print("Downloading images...\n\n")
    ddg.download(phrase, "images/" + phrase, 10)
    common_color = ip.get_common_color_v2("images/" + phrase)
    populate_output_window(phrase, common_color)


