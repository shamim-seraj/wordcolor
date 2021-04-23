# Features
For any given word or phrase, the software would be able to represent the word/phrase into a color. Currently, we are using traditional clustering algorithm KMeans to achieve this. We are also applying some image processing techniques and parallel processing to make the color estimation process faster.

# Working Principle
![alt text](https://ucb3e5ac2ee0ed797b4b48ba0a28.previews.dropboxusercontent.com/p/thumb/ABLRCDThQEPyXQHjLgq-gUxou3VyTd3FZJE9srTNRqRRDqAF2cwfhEE-jbmusCi0aiRamt5IrSF4uvfK1QmaKtgrncpPdYrxhRQ0MmXan3QKpq1LVMJuQuXch-Uc2qclr3kp17kpas7AjIy3sCAoXn7RC4II2nXNKCn-cYRmaRmmoYtoTZedcfKmN_e9NGN1_Z3jNPKWX6eLmV9vLQOJS9R0QgOMm_ChJY0DIASMTSB2rBQ2frYXkG5yB3idZIC53CZMftjY42gBnVO6j-3p1Bb0JXHjKcbG2kqUdtnw-pfH2uvckHsID0k8IEKKhjITGT7re-Iu0RMh2XIEGapxVvGEgB4TVztnXbDCsTxeIFokDaflCeIey4IeYOA9EOa6eynLG8bJWpJ7BPZh3Vj_BeFd/p.jpeg?fv_content=true&size_mode=5)

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
![alt text](https://uce52550f73058f36d8f9beea504.previews.dropboxusercontent.com/p/thumb/ABITys6bO2MNoSyFRnPRq-5e7vSlrkxCSDlMNF35Y47UszFMYWOMgNnOQFbux4QcXABfdIP1BECzfe5Lr7tRRVO9f_q2_dHS2Bdn-yLCNBzjTUWoJehW3jSkjeJUhbwxVsZA_mIPl1hxa23u6LkYdT9TZObfW3D1bwVgI0hS4sVU2SoKruFjVOk4EkzafTmhkw5xYBHOYmPeS2-jxIhrTuCSvzeQz4ZX7_KVDhSJcGaH2uRCRv0-_d68WTjRp37lI_073jmsX1yC4Lk5QU3pV86Ywgck4i5RC_fbicLYXZMqj71j4RmB2hoTVuKkng1pn6CRn_17N8DANA4fzHttenOeHLLzbYag_PCpX_tDQ9O3NcqHQIZXZ-Tm4yuMqZyRnm8hFHgx5ERP3vnJI1JmtIdV/p.png?fv_content=true&size_mode=5)

You can input any word/phrase here to get a color. When you click on the _Get Color_ button you will get your desired color in another page-
![alt_text](https://uc1283bacb09aa70c536e35153f0.previews.dropboxusercontent.com/p/thumb/ABKY6CSlAii7ejYRQtAiJEH1kO2LJvtPylLF9wxf7HGeDG62rFDuYUk9OBLD3Y6-tW_2rKPm3Gyyd95prepa-I5Q3kZc3kJbIlRMe3JZs_nyvpUfmdJcCmryYld_FTS4vi02L9YrLCfeT2zk0hhT7jktsofoJ_AwRFmE8Wd1ajYlPDii9SW6IwVzONi_ylLXZtmALxxJo9RON18iP-JK1NShBbbbpx3NacWcmmURWuvZVDVcOBJurzT4X28n1GOIDI4Ibe9-gYlWux1xLQg0v-AHfZAYzdnIv8cM3Jqc28limtFKdix0zEyfmJNP_EFO4lCVSDMTAvFR4Q0hdLUhC8BgURROpVyFmErDtsiGAg3Hqtxku-yb-9STB_M7iPkRvrqQEtZQdL_uOXRMep9vJ6Mp/p.jpeg?fv_content=true&size_mode=5)

By clicking on the _Go Back_ button you can redirect to the home page and repeat the process.