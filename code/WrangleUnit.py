# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:51:03 2017

@author: NKallfa
"""

# ----------------------------------------- BEGIN FUNCTIONS -----------------------------------------#

def HalfBath(x):
    
    import re
    numRegex = re.compile(r'\d')
    
    if isinstance(x,str) == True:
        if len(x) > 1:
            output = numRegex.search(x).group()+".5"
        else:
            output = x
    else:
        output = x
        
    return(output)

def GetAvailableApts(path, i):
    
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
        
        
        PropertyID = [int(i)]*len(Beds) # Keep track of the property
    
    if check == 6: # If there are no apartments available at this property then we assign everything as NAN
        if  ("Apartments for Rent in" in soup.find_all("title")[0].text) or (soup.find_all("span", attrs = {"class" : "noAvailability"}) != []):
            PropertyID = int(i)
            Beds = math.nan
            Baths = math.nan
            MinRent = math.nan
            MaxRent = math.nan
            MinSqFt = math.nan
            MaxSqFt = math.nan
            Property = pd.DataFrame({"pid" : PropertyID, "beds" : Beds, "baths" : Baths, "minrent" : MinRent, "maxrent" : MaxRent, "minsqft" : MinSqFt, "maxsqft" : MaxSqFt}, index = range(0,1))
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
            PropertyID = [int(i)]
            Property = pd.DataFrame({"pid" : PropertyID, "beds" : Beds, "baths" : Baths, "minrent" : MinRent, "maxrent" : MaxRent, "minsqft" : MinSqFt, "maxsqft" : MaxSqFt})
    
    else: # If we found more than one apartment
        if len(Beds) > 1:
            Property = pd.DataFrame({"pid" : PropertyID, "beds" : Beds, "baths" : Baths, "minrent" : MinRent, "maxrent" : MaxRent, "minsqft" : MinSqFt, "maxsqft" : MaxSqFt})
        else: # If no apartments are available
            PropertyID = int(i)
            Beds = math.nan
            Baths = math.nan
            MinRent = math.nan
            MaxRent = math.nan
            MinSqFt = math.nan
            MaxSqFt = math.nan
            Property = pd.DataFrame({"pid" : PropertyID, "beds" : Beds, "baths" : Baths, "minrent" : MinRent, "maxrent" : MaxRent, "minsqft" : MinSqFt, "maxsqft" : MaxSqFt}, index = range(0,1))
        
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
        PropertyID = [int(i)]
        MetroStation = ["None"]
        Distance = [math.nan]
        Time = [math.nan]
        Transportation = pd.DataFrame({"pid" : PropertyID, "station" : MetroStation,"distance" : Distance, "time" : Time})
    else: # Else there are nearby metro stations so we store those   
        PropertyID = [int(i)]*len(MetroStation)
        Transportation = pd.DataFrame({"pid" : PropertyID, "station" : MetroStation,"distance" : Distance, "time" : Time})
        
        
    Property = Property[["pid", "beds", "baths", "minrent", "maxrent", "minsqft", "maxsqft"]]
    Transportation = Transportation[["pid", "station", "distance", "time"]]
    
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
    outputDF["pid"] = [int(i)]
    outputDF["parent"] = [parent]
    
    # Return data frame
    return(outputDF)

def GetType(path, i):
    
    # Import required packages
    from bs4 import BeautifulSoup
    import pandas as pd
    
    # Open file in path, read file, and parse file
    file = open(path, "r")   
    #test = open("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\PropertyID0.html", "r")
    file = file.read()
    soup = BeautifulSoup(file, "lxml")
    
    # Look for name of parent company
    typeapt = soup.find_all("h2", attrs = {"class":"subHeading"})
    
    if typeapt is None: # If no parent company is found
        typeapt = "Unknown"
    elif typeapt == []:
        typeapt = "Unknown"
    elif typeapt[0].text.strip().split(" ")[0] == "Reviews":
        typeapt = "Unknown"
    else: # If parent company is found, get name of parent company
        typeapt = typeapt[0].text.strip().split(" ")[0]
    
    # Initialize empty data frame and store property ID and parent company name
    outputDF = pd.DataFrame()
    outputDF["pid"] = [int(i)]
    outputDF["type"] = [typeapt]
    
    # Return data frame
    return(outputDF)
# ----------------------------------------- END FUNCTIONS -----------------------------------------#
# ----------------------------------------- BEGIN SCRIPT -----------------------------------------#
    
# Import required packages
import os
import re
import pandas as pd
import math


# List files in directory
folder = "C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\DMV\\data\\unit data dedup\\"
#AllCities = pd.read_csv("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Partly Cleaned September 24\\AllCities.csv", encoding = "latin-1")
#files = ["PropertyID954.html", "PropertyID1014.html", "PropertyID2323.html"]

# Initialize variables to store output
Property = []
Transportation = []

# Create regular expression to search for a single digit number to a 4-digit number
numRegex = re.compile(r"\d{1,4}")

count = 0

# For each file in directory
for file in os.listdir(folder):
    ID = numRegex.search(file).group() # Get property ID
    # Parse unit-level data and output unit-level data for that property and local metro station data
    P, T = GetAvailableApts(folder+file, ID)
    Property.append(P) # Append unit-level data to list
    Transportation.append(T) # Append local metro station data to list
    if count%100 == 0:
        print(count)
    count+=1
    
# Append unit-level datand local metro station data to single data frame
PropertyDF = pd.DataFrame()
TransportationDF = pd.DataFrame()

for df in Property:
    PropertyDF = PropertyDF.append(df, ignore_index = True)

PropertyDF.loc[PropertyDF['baths'] == '', 'baths'] = math.nan
PropertyDF.baths = PropertyDF.baths.apply(lambda x: HalfBath(x))
PropertyDF.baths = PropertyDF.baths.apply(lambda x: float(x))
    
for df in Transportation:
    TransportationDF = TransportationDF.append(df, ignore_index = True)

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

TransportationDF.sort_values(["pid", "distance"], inplace = True)
TransportationDF.index = range(0, len(TransportationDF))

PropertyDF.sort_values(["pid", "beds", "baths"], inplace = True)
PropertyDF.index = range(0, len(PropertyDF))


# Write outputs of script to CSV
    
PropertyDF.to_csv("Units.csv", index = False)
TransportationDF.to_csv("UnitTransport.csv", index = False)
ParentDF.to_csv("Parent.csv", index = False)
ParentLU.to_csv("ParentLU.csv", index = False)
TypeDF.to_csv("Type.csv", index = False)


# ----------------------------------------- END SCRIPT -----------------------------------------#
""" ----------------------------------------- BEGIN THINGS TO DO -----------------------------------------

1. Add function to get type of apartment (apartment, home, townhome, condo, etc...)
# ----------------------------------------- END THINGS TO DO -----------------------------------------"""


# ----------------------------------------- BEGIN OLD CODE -----------------------------------------#

# ----------------------------------------- END OLD CODE -----------------------------------------#