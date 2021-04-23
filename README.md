# Features
For any given word or phrase, the software would be able to represent the word/phrase into a color. Currently, we are using traditional clustering algorithm KMeans to achieve this. We are also applying some image processing techniques and parallel processing to make the color estimation process faster.

# Working Principle
![alt text](https://ucb3e5ac2ee0ed797b4b48ba0a28.previews.dropboxusercontent.com/p/thumb/ABLRCDThQEPyXQHjLgq-gUxou3VyTd3FZJE9srTNRqRRDqAF2cwfhEE-jbmusCi0aiRamt5IrSF4uvfK1QmaKtgrncpPdYrxhRQ0MmXan3QKpq1LVMJuQuXch-Uc2qclr3kp17kpas7AjIy3sCAoXn7RC4II2nXNKCn-cYRmaRmmoYtoTZedcfKmN_e9NGN1_Z3jNPKWX6eLmV9vLQOJS9R0QgOMm_ChJY0DIASMTSB2rBQ2frYXkG5yB3idZIC53CZMftjY42gBnVO6j-3p1Bb0JXHjKcbG2kqUdtnw-pfH2uvckHsID0k8IEKKhjITGT7re-Iu0RMh2XIEGapxVvGEgB4TVztnXbDCsTxeIFokDaflCeIey4IeYOA9EOa6eynLG8bJWpJ7BPZh3Vj_BeFd/p.jpeg?fv_content=true&size_mode=5)

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
To run coverage test-
```
coverage run --omit 'venv/*' -m pytest
coverage report -m
```
