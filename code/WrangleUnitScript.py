# -*- coding: utf-8 -*-
"""
Description: This file contains a script that can be used to run functions that will clean the unit-level data.

"""

# ----------------------------------------- BEGIN SCRIPT -----------------------------------------#
    
# Import required packages
import os
import re
import pandas as pd
import math
from WrangleUnitFunctions import *


# List files in directory
folder = "C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\DMV\\data\\unit data dedup\\"
#AllCities = pd.read_csv("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Partly Cleaned September 24\\AllCities.csv", encoding = "latin-1")
#files = ["PropertyID954.html", "PropertyID1014.html", "PropertyID2323.html"]

# Initialize variables to store output
Property = []
CommuterRail = []
MetroStation = []

# Create regular expression to search for a single digit number to a 4-digit number
numRegex = re.compile(r"\d{1,4}")

count = 0

# For each file in directory
for file in os.listdir(folder):
    ID = numRegex.search(file).group() # Get property ID
    # Parse unit-level data and output unit-level data for that property and local metro station data
    P, CR = GetAvailableApts(folder+file, ID)
    MS = GetMetroStation(folder+file, ID)
    Property.append(P) # Append unit-level data to list
    CommuterRail.append(CR) # Append local commuter rail data to list
    MetroStation.append(MS) # Append local metro station data to list
    if count%100 == 0:
        print(count)
    count+=1
    
# Append unit-level datand local metro station data to single data frame
PropertyDF = pd.DataFrame()
CommuterRailDF = pd.DataFrame()
MetroStationDF = pd.DataFrame()

for df in Property:
    PropertyDF = PropertyDF.append(df, ignore_index = True)

PropertyDF.loc[PropertyDF['baths'] == '', 'baths'] = math.nan
PropertyDF.baths = PropertyDF.baths.apply(lambda x: HalfBath(x))
PropertyDF.baths = PropertyDF.baths.apply(lambda x: float(x))
    
for df in CommuterRail:
    CommuterRailDF = CommuterRailDF.append(df, ignore_index = True)
    
for df in MetroStation:
    MetroStationDF = MetroStationDF.append(df, ignore_index = True)

# Initialize list to store data
Parent = []

i = 0
# For each file in the directory
for file in os.listdir(folder):
    ID = numRegex.search(file).group() # Get property ID
    # Parse the data to find the parent company
    df = GetParentCompany(folder+file, ID)    
    Parent.append(df) # Append to list
    
    # Use to keep track of progress
    if i%100 == 0:
        print(i)
    i+=1

ParentDF = pd.DataFrame()

for df in Parent:
    ParentDF = ParentDF.append(df, ignore_index = True)
    
Type = []

i = 0
# For each file in the directory
for j in range(0,7244):
    ID = j#ID = numRegex.search(file).group() # Get property ID
    # Parse the data to find the type
    df = GetType(folder+"PropertyID"+str(j)+".html", ID)    
    Type.append(df) # Append to list
    
    # Use to keep track of progress
    if i%100 == 0:
        print(i)
    i+=1

TypeDF = pd.DataFrame()

for df in Type:
    TypeDF = TypeDF.append(df, ignore_index = True)
    

ParentLU = pd.DataFrame(ParentDF.parent.unique(), columns = ["parent"])
ParentLU["parentid"] = range(0, len(ParentLU))
ParentLU = ParentLU[["parentid", "parent"]]

ParentDF = ParentDF.merge(ParentLU, how = "inner", on = "parent")
ParentDF = ParentDF[["pid", "parentid"]]
ParentDF.sort_values("pid", inplace = True)
ParentDF.index = range(0, len(ParentDF))

CommuterRailDF.sort_values(["pid", "distance"], inplace = True)
CommuterRailDF.index = range(0, len(CommuterRailDF))
MetroStationDF.sort_values(["pid", "distance"], inplace = True)
MetroStationDF.index = range(0, len(MetroStationDF))

PropertyDF.sort_values(["pid", "beds", "baths"], inplace = True)
PropertyDF.index = range(0, len(PropertyDF))


# Write outputs of script to CSV
    
PropertyDF.to_csv("Units.csv", index = False)
CommuterRailDF.to_csv("UnitCommuterRail.csv", index = False)
MetroStationDF.to_csv("UnitMetroStation.csv", index = False)
ParentDF.to_csv("Parent.csv", index = False)
ParentLU.to_csv("ParentLU.csv", index = False)
TypeDF.to_csv("Type.csv", index = False)


# ----------------------------------------- END SCRIPT -----------------------------------------#
""" ----------------------------------------- BEGIN THINGS TO DO -----------------------------------------

1. Add function to get type of apartment (apartment, home, townhome, condo, etc...)
# ----------------------------------------- END THINGS TO DO -----------------------------------------"""


# ----------------------------------------- BEGIN OLD CODE -----------------------------------------#

# ----------------------------------------- END OLD CODE -----------------------------------------#

