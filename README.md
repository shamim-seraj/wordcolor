# Features
For any given word or phrase, the software would be able to represent the word/phrase into a color. Currently, we are using traditional clustering algorithm KMeans to achieve this. We are also applying some image processing techniques and parallel processing to make the color estimation process faster.

# How to Run
Currently, the application has a web interface. We are planning to host the application and make it public so that users can easily input a word or a phrase from anywhere without having to run the whole application. 
To run the application now, download the code as a zip file, unzip it, move into the project(wordcolor-main) directory and run the following commands-

To download all the necessary libraries-
```
pip3 install -r requirements.txt
```
To set the flask app on Linux machine-
```
export FLASK_APP=word_color_main.py
```
To set up the flask app on Windows machine-
```
set FLASK_APP=word_color_main.py
```
To start the flask app-
```
python3 -m flask run
```
To run all the test codes-
```
python3 -m pytest
```
