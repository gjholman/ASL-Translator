# ASL Video Recognition

## Purpose
Most ASL computer vision programs are good, but they lack a very important feature: motion. The programs I've found are able to recognize images of the ASL alphabet with great accuracy, however the letters J and Z are typically not included in the datasets, and are not processed into the machine learning algorithm. The goal of this project is to fill that gap and create a program that can quickly recognize ASL letters and words from moving picture input.

## How
Essentially, the goal is to be able to input a series of pictures to a neural network that will recognize what word or phrase is being displayed. Since there is very little on that, what I am going to do is record video as a series of pictures and stitch those pictures together and use that as my input into a neural network.

## Data Acquisition
Since the inputs to this project are unique, I will have to create my data manually. I will use OpenCV with Python to create a streamline process for acquiring data, as well as automatically knowing the output the image series should be mapped to.

## Training the Machine Learning Model
Tensorflow model for image recognition. Since the images recorded have to be compiled to one image, the tensorflow model will have to take in a large images. The model will be trained using the recorded and compiled images and then stored into a pickle (.pkl) file to load into the translating script.

## Translator
As fast as real time model recognition is possible, the script will record a limited number of frames (indicating to the user when to sign) and then input to the loaded trained model to predict which sign is being displayed.
