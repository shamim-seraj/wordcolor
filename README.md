# Features
For any given word or phrase, the software would be able to represent the word/phrase into a color. Currently, we are using traditional clustering algorithm KMeans to achieve this. We are also applying some image processing techniques and parallel processing to make the color estimation process faster.

# Working Principle
![alt text](https://i.ibb.co/88GktXZ/working-principle.jpg)

# Dataset Generation
We collected 10K color data. We managed to find 8000 bird names, 769 animal names, and 1334 minaral names. We used our software to collect color codes for all these phrases. The data can be found in the _exported_data_ directory.

# How to Run
Currently, the application has a web interface. We are planning to host the application and make it public so that users can easily input a word or a phrase from anywhere without having to run the whole application. 
To run the application now, download the code as a zip file, unzip it. Now from terminal, move into the project(wordcolor-main) directory and run the following commands-

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
To run coverage test-
```
coverage run --omit 'venv/*' -m pytest
coverage report -m
```
# How to Use the Software
The project is a web app now. Once the server is started, you can see the following web interface by going to http://127.0.0.1:5000/ from your browser-
![alt text](https://i.ibb.co/995TQ5F/Interface-1-1.png)

You can input any word/phrase here to get a color. When you click on the _Get Color_ button you will get your desired color in another page-
![alt_text](https://i.ibb.co/tmHMgnV/Interface-2.jpg)

By clicking on the _Go Back_ button you can redirect to the home page and repeat the process.