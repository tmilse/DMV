# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:51:03 2017

@author: NKallfa
"""

# ----------------------------------------- BEGIN FUNCTIONS -----------------------------------------#

def Parse(path, i):
    
    # Import required packages
    from bs4 import BeautifulSoup
    import re
    import pandas as pd
    import math
    
    # Open, read, and parse html file
    file = open(path, "r") # Open html file
    #test = open("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\PropertyID0.html", "r")
    file = file.read() # Read into memory
    soup = BeautifulSoup(file, "lxml") # Parse html file

    # Initialize variables to store information
    numRegex = re.compile(r"\d") # Number regular expression
    beds = ["bed0", "bed1", "bed2", "bed3", "bed4", "bed5"] # Search for studios, 1BR, 2BR, 3BR, ..., 5BR
    Beds = [] 
    Baths = []
    MinRent = []
    MaxRent = []
    MinSqFt = []
    MaxSqFt = []
    
    check = 0 # Check will be used to look to see if there are no rooms available
    for numbeds in beds:
        
        table = soup.find_all("div", attrs = {"data-tab-content-id" : numbeds})
        if table == []: # If we can't find any rooms available update check
            check +=1
            continue # Continue goes back to the for loop
        else: 
            baths = table[0].find_all("td", attrs = {"class" : "baths"}) # Get the number of baths for all of the rooms
            rent = table[0].find_all("td", attrs = {"class" : "rent"})  # Get the rent for all of the rooms
            sqft = table[0].find_all("td", attrs = {"class" : "sqft"}) # Get the sqft of all of the rooms
            NumUnits = len(baths) # Get number of units available
                
            for num in range(0,NumUnits):
                Beds.append(int(numbeds[3])) # Get number of bedrooms in the apartment
        
            # Loop to get the number of bathrooms in the apartment
            for elements in baths:
                temp = elements.find_all("span", attrs = {"class" : "longText"})[0].text.strip().split(" ")[0]
                Baths.append(temp) 
            
            # Loop to get the rent for each of the apartments
            for cost in rent:
                temp = cost.text
                if "Call for Rent" in temp: # Sometimes rent is not specified so we store those as NAN
                    MinRent.append(math.nan)
                    MaxRent.append(math.nan)
                else: # Else the rent is specified
                    temp = temp.split("$")[1].replace("\n", "").replace(",", "").strip() # Get rent of the apartment
                    if len(temp.split(" - ")) == 2: # If the rent is a range of values
                        MinRent.append(int(temp.split(" - ")[0])) # Split range and get first value
                        MaxRent.append(int(temp.split(" - ")[1])) # Split range and get second vlaue
                    elif len(temp.split(" - ")) == 1: # Else the rent is a single value so we append the same value to min rent and max rent lists
                        MinRent.append(int(temp)) 
                        MaxRent.append(int(temp))
            
            # Loop to get sqft
            for unit in sqft:
                temp = unit.text.split(" ")[0].replace(",", "") # Get sqft of apartment
                if len(temp.split(" - ")) == 2: # If the sqft is a range of values
                    MinSqFt.append(int(temp.split(" - ")[0])) # Split the range and get first value
                    MaxSqFt.append(int(temp.split(" - ")[1])) # Split the range and get second value
                elif temp.split(" - ")[0] == "": # In case the sqft is not given append NAN
                    MinSqFt.append(math.nan)
                    MaxSqFt.append(math.nan)
                else: # Else the sqft is a single value so we append the same value to min sqft and max sqft lists
                    MinSqFt.append(int(temp))
                    MaxSqFt.append(int(temp))
        
        
        PropertyID = [i]*len(Beds) # Keep track of the property
    
    if check == 6: # If there are no apartments available at this property then we assign everything as NAN
        if  ("Apartments for Rent in" in soup.find_all("title")[0].text) or (soup.find_all("span", attrs = {"class" : "noAvailability"}) != []):
            PropertyID = i
            Beds = math.nan
            Baths = math.nan
            MinRent = math.nan
            MaxRent = math.nan
            MinSqFt = math.nan
            MaxSqFt = math.nan
            Property = pd.DataFrame({"PropertyID" : PropertyID, "Beds" : Beds, "Baths" : Baths, "MinRent" : MinRent, "MaxRent" : MaxRent, "MinSqFt" : MinSqFt, "MaxSqFt" : MaxSqFt}, index = range(0,1))
        else: # Else look for just studios
            table = soup.find_all("td", attrs = {"class" : "beds"})
            if "Studio" in table[0].find_all("span", attrs = {"class" : "longText"})[0].text:
                beds = 0
            else:
                beds = numRegex.search(table[0].find_all("span", attrs = {"class" : "longText"})[0].text).group()
            Beds.append(int(beds))
            table = soup.find_all("td", attrs = {"class" : "baths"})
            baths = table[0].find_all("span", attrs = {"class" : "longText"})[0].text.strip().split(" ")[0]
            Baths.append(baths)
            temp = soup.find_all("td", attrs = {"class" : "rent"})[0].text
            if "Call for Rent" in temp:
                MinRent.append(math.nan)
                MaxRent.append(math.nan)
            else:
                temp = temp.split("$")[1].replace("\n", "").replace(",", "").strip()
                if len(temp.split(" - ")) == 2:
                    MinRent.append(int(temp.split(" - ")[0]))
                    MaxRent.append(int(temp.split(" - ")[1]))
                elif len(temp.split(" - ")) == 1:
                    MinRent.append(int(temp))
                    MaxRent.append(int(temp))
            temp = soup.find_all("td", attrs = {"class" : "sqft"})[0].text
            temp = temp.split(" ")[0].replace(",", "")
            if len(temp.split(" - ")) == 2:
                MinSqFt.append(int(temp.split(" - ")[0]))
                MaxSqFt.append(int(temp.split(" - ")[1]))
            elif temp.split(" - ")[0] == "":
                MinSqFt.append(math.nan)
                MaxSqFt.append(math.nan)
            else:
                MinSqFt.append(int(temp))
                MaxSqFt.append(int(temp))
            PropertyID = [i]
            Property = pd.DataFrame({"PropertyID" : PropertyID, "Beds" : Beds, "Baths" : Baths, "MinRent" : MinRent, "MaxRent" : MaxRent, "MinSqFt" : MinSqFt, "MaxSqFt" : MaxSqFt})
    
    else: # If we found more than one apartment
        if len(Beds) > 1:
            Property = pd.DataFrame({"PropertyID" : PropertyID, "Beds" : Beds, "Baths" : Baths, "MinRent" : MinRent, "MaxRent" : MaxRent, "MinSqFt" : MinSqFt, "MaxSqFt" : MaxSqFt})
        else: # If no apartments are available
            PropertyID = i
            Beds = math.nan
            Baths = math.nan
            MinRent = math.nan
            MaxRent = math.nan
            MinSqFt = math.nan
            MaxSqFt = math.nan
            Property = pd.DataFrame({"PropertyID" : PropertyID, "Beds" : Beds, "Baths" : Baths, "MinRent" : MinRent, "MaxRent" : MaxRent, "MinSqFt" : MinSqFt, "MaxSqFt" : MaxSqFt}, index = range(0,1))
        
    # Now we try to extract local metro station information
    MetroStation = []
    Distance = []
    Time = []
    
    # Find the transportation table
    transport = soup.find_all("div", attrs = {"class" : "transportationDetail"})
    for element in transport:
        if "Commuter" in element.find("th").text: # Look for commuter rail
            look = element.find_all("td")
            for row in look:
                if " min" in row.text: # Look for the time from metro station
                    Time.append(int(row.text.split(" ")[0]))
                elif row.text[len(row.text) - 2:len(row.text)] == "mi": # Look for distance from metro station
                    Distance.append(float(row.text.split(" ")[0]))
                else: # Else it's the name of the metro station
                    MetroStation.append(row.text)
        else: # Else keep looking for commuter rail table
            continue # Go back to for loop
    
    # Use in case there are no nearby metro stations
    if len(MetroStation) == 0:
        PropertyID = [i]
        MetroStation = ["None"]
        Distance = [math.nan]
        Time = [math.nan]
        Transportation = pd.DataFrame({"PropertyID" : PropertyID, "MetroStation" : MetroStation,"Distance" : Distance, "Time" : Time})
    else: # Else there are nearby metro stations so we store those   
        PropertyID = [i]*len(MetroStation)
        Transportation = pd.DataFrame({"PropertyID" : PropertyID, "MetroStation" : MetroStation,"Distance" : Distance, "Time" : Time})
    
    # Return property date and local metro transportation data
    return(Property, Transportation)
    
def GetParentCompany(path, i):
    
    # Import required packages
    from bs4 import BeautifulSoup
    import pandas as pd
    
    # Open file in path, read file, and parse file
    file = open(path, "r")   
    #test = open("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\PropertyID0.html", "r")
    file = file.read()
    soup = BeautifulSoup(file, "lxml")
    
    # Look for name of parent company
    parent = soup.find("img", attrs = {"class":"logo"})
    
    if parent is None: # If no parent company is found
        parent = "Unknown"
    else: # If parent company is found, get name of parent company
        parent = parent.get("alt", "")
    
    # Initialize empty data frame and store property ID and parent company name
    outputDF = pd.DataFrame()
    outputDF["pid"] = [i]
    outputDF["parent"] = [parent]
    
    # Return data frame
    return(outputDF)

# ----------------------------------------- END FUNCTIONS -----------------------------------------#
# ----------------------------------------- BEGIN SCRIPT -----------------------------------------#
    
# Import required packages
import os
import re
import pandas as pd


# List files in directory
files = os.listdir("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data")
#AllCities = pd.read_csv("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Partly Cleaned September 24\\AllCities.csv", encoding = "latin-1")
#files = ["PropertyID954.html", "PropertyID1014.html", "PropertyID2323.html"]

# Initialize variables to store output
Property = []
Transportation = []

# Create regular expression to search for a single digit number to a 4-digit number
numRegex = re.compile(r"\d{1,4}")


# For each file in directory
for file in files:
    ID = numRegex.search(file).group() # Get property ID
    # Parse unit-level data and output unit-level data for that property and local metro station data
    P,T = Parse("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\"+file, ID)
    Property.append(P) # Append unit-level data to list
    Transportation.append(T) # Append local metro station data to list
    

# Initialize list to store data
Parent = []

i = 0
# For each file in the directory
for file in files:
    ID = numRegex.search(file).group() # Get property ID
    if ID == "954": # File with property ID = 954 treat separately because we're having trouble parsing it
        df = pd.DataFrame()
        df["pid"] = 954
        df["parent"] = "Unknown"
        Parent.append(df)
        continue # Goes back to beginning of for loop
    # Otherwise parse the data to find the parent company
    df = GetParentCompany("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\"+file, ID)    
    Parent.append(df) # Append to list
    
    # Use to keep track of progress
    if i%100 == 0:
        print(i)
    i+=1