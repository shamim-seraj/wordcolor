# Features
For any given word or phrase, the software would be able to represent the word/phrase into a color. Currently, the software takes words/phrases from a data.txt file(included and can be updated), loops through all of them, download 5(can be updated) images per word/phrase and save them in corresponding directories. Then it again loops through all the directories, processes those images to finally decide/estimate a color for that phrase.

# How to Run
Currently, the application runs from terminal. The future plan is to develop a Graphical User Interface where users can easily input a word or a phrase. To run the application, download the code as a zip file, unzip it, move into the project(wordcolor) folder and run the following commands-
```
pip3 install -r requirements.txt
python3 word_color_main.py
```
