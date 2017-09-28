# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:09:00 2017

@author: NKallfa
"""

import os
from ParseUnitData import Parse
import re

files = os.listdir("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data")
#AllCities = pd.read_csv("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Partly Cleaned September 24\\AllCities.csv", encoding = "latin-1")


Property = []
Transportation = []

numRegex = re.compile(r"\d{1,4}")

for file in files:
    ID = numRegex.search(file).group()
    T = Parse("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\"+file, ID)
    Transportation.append(T)
    #Transportation.append(Transport)
    