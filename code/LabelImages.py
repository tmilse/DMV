# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:46:20 2017

@author: NKallfa
"""

# Import required packages and functions
import io
import os
import pandas as pd

from google.cloud import vision
from google.cloud.vision import types

# Set Google API authentication and set folder where images are stored
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\NKallfa\\Desktop\\NKGoogleAPI-91c0493130be.json'
ImageFolder = 'C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\DMV\\cleaned data\\images\\'

# Placeholders to store data
ImageID = []
MID = []
Description = []
Score = []

# Create empty data frame and vision API client
ImageLabels = pd.DataFrame()
client = vision.ImageAnnotatorClient()

# Get labels and scores for every image in folder
for file in os.listdir(ImageFolder):
    filename = os.path.basename(file).split('.')[0] # Get image ID
    image_file = io.open(ImageFolder+file, 'rb') # Open image
    content = image_file.read() # Read image into memory
    image = types.Image(content=content) # Does something
    response = client.label_detection(image=image) # Gets response from API for image
    labels = response.label_annotations # Get labels from response
    Nlabels = len(labels) # Get the number of labels that were returned
    for i in range(0, Nlabels): # For each label we will store the MID, label, and score
        ImageID.append(filename) # Keep track Image ID
        MID.append(labels[i].mid) # Store MID
        Description.append(labels[i].description) # Store label
        Score.append(labels[i].score) # Store score of label

# Put Image ID, MID, label, and score into data frame
ImageLabels["imageid"] = ImageID
ImageLabels["mid"] = MID
ImageLabels["desc"] = Description
ImageLabels["score"] = Score

