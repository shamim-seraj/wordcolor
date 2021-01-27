# ColorMappingProject
Project Outline:
The goal of this project is that given any word or phrase, it will be able to represent that input data in its HTML color form
  
First Phase Tasks:
* Collect about 200 data samples in this format- (e.g.- #ffffff milk) and create a text file with that:
    About 150 words have been listed with their html hex code values for initial input sample dataset. This file consists of random words or phrases that are used in daily lives and can be easily represented with any color. The colors have been searched manually from the internet and have been listed with the respective word or phrase.
* Develop a test environment for this dataset and derive its mean, standard deviation and variance distance of the text file from a predefined(#ffffff) color:
    Following functions have been implemnted: A function for converting the color which for now only returns the predefined color(#ffffff) and separate functions for mean (m), standard deviation (sd) and variance (var) which calculates the values. Also, a function is implemented that loads the data from the text file. In built numpy functions have been used to calculate the m, sd, var values.
* Collect images for the sample dataset from duckduckgo
* Develop the color generator function which produces the most common color out of all the 20 images for a particular data sample
