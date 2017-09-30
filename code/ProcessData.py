# -*- coding: utf-8 -*-
"""
Description: This file contains functions and a script that will take the original data and clean it as needed
             Original data is hosted in a WORM storage on Digital Ocean. 
"""

# ----------------------------------------- BEGIN FUNCTIONS -----------------------------------------#

def DropCols(df):
    
    # Import required package
    import pandas as pd
    
    # Drop columns labeled Distance and Duration from dataframe
    df.drop(labels = ["Distance","Duration","Option Name", "Rent", "Size"], axis = 1, inplace = True)
    
    # Return dataframe
    return(df)
    
def GetNames(df):
    
    # Import required package
    import re
    import pandas as pd
    
    # Create regular expression to find names within brackets
    nameRegex = re.compile(r'\[(.*?)\]')
    namesDF = pd.DataFrame(columns = ["Name"]) # Initiate empty dataframe to store names
    
    # Loop and use regular expression to get name and append to dataframe
    for element in df["Option Name"]:
        tempName = nameRegex.search(element).group(1)
        tempName = pd.DataFrame([tempName], columns = ["Name"])
        namesDF = namesDF.append(tempName, ignore_index = True)
    
    # Insert new column and return dataframe
    df.insert(loc = 0, column = "Name", value = namesDF)
    return(df)

def GetLinks(df):
    
    # Import required package
    import re
    import pandas as pd
    
    # Create regular expression to find link within parentheses
    linkRegex = re.compile(r'\((.*?)\)')
    linksDF = pd.DataFrame(columns = ["Link"]) # Initiate empty dataframe to store links
    
    # Loop and use regular expression to get link and append to dataframe
    for element in df["Option Name"]:
        tempLink = linkRegex.search(element).group(1)
        tempLink = pd.DataFrame([tempLink], columns = ["Link"])
        linksDF = linksDF.append(tempLink, ignore_index = True)
    
    # Insert new column and return dataframe
    df.insert(loc = 1, column = "Link", value = linksDF)
    return(df)
    
def GetAddresses(df):
    
    # Import required package
    import re
    import pandas as pd
    
    # Create regular expression to find address within brackets
    addressRegex = re.compile(r'\[(.*?)\]')
    addressesDF = pd.DataFrame(columns = ["Address"]) # Initiate empty dataframe to store address
    
    # Loop and use regular expression to get address and append to dataframe
    for element in df["Address"]:
        tempAddress = addressRegex.search(element).group(1)
        tempAddress = pd.DataFrame([tempAddress], columns = ["Address"])
        addressesDF = addressesDF.append(tempAddress, ignore_index = True)
    
    # Drop address column, insert created address column, and return dataframe
    df.drop(labels = "Address", axis = 1, inplace = True)
    df.insert(loc = 2, column = "Address", value = addressesDF)
    return(df)
    
def SplitAddresses(df):
    
    #Import required package
    import pandas as pd
    
    # Initialize empty data frames
    addressesDF = pd.DataFrame(columns = ["Address"]) # Initiate empty dataframe to store addresses
    cityDF = pd.DataFrame(columns = ["City"]) # Initiate empty dataframe to store city
    stateDF = pd.DataFrame(columns = ["State"]) # Initiate empty dataframe to store state
    zipCodeDF = pd.DataFrame(columns = ["Zip_Code"]) # Initiate empty dataframe to store zip codes

    # Loop through elements and grab address and zip code
    for element in df["Address"]:
        tempAddress = pd.DataFrame([element.split(",")[0]], columns = ["Address"])
        tempCity = pd.DataFrame([element.split(",")[1]], columns = ["City"])
        if tempCity.City[0] == " Washington":
            tempCity.at[0, "City"] = "District of Columbia"
        tempState = pd.DataFrame([element[len(element)-8:len(element) - 5]], columns = ["State"])
        if tempState.State[0] == "DC ":
            tempState.at[0, "State"] = "District of Columbia"
        tempZipCode = pd.DataFrame([element[len(element)-5:len(element)]], columns = ["Zip_Code"])

        addressesDF = addressesDF.append(tempAddress, ignore_index = True)
        cityDF = cityDF.append(tempCity, ignore_index = True)
        stateDF = stateDF.append(tempState, ignore_index = True)        
        zipCodeDF = zipCodeDF.append(tempZipCode, ignore_index = True)

    # Insert address, city, and zip code into dataframe and return dataframe
    df.drop(labels = "Address", axis = 1, inplace = True)
    df.insert(loc = 2, column = "Address", value = addressesDF)
    df.insert(loc = 3, column = "City", value = cityDF)
    df.insert(loc = 4, column = "State", value = stateDF) 
    df.insert(loc = 5, column = "Zip_Code", value = zipCodeDF)
    return(df)

def GetMinMaxRent(df):
    
    # Import required packages
    import re
    import math
    
    rentDF = pd.DataFrame() # Initiate empty dataframe to store min/max rent
    
    # Loop through rent and get min/max rent
    for rent in df["Rent"]:
        if isinstance(rent, str):
            tempRent = re.sub("\$", "", rent)
            tempRentSplit = tempRent.split(" - ") 
            if len(tempRentSplit) == 2: #Rent could be given as a range
                tempRentSplit[0] = int(re.sub(",", "", tempRentSplit[0]))
                tempRentSplit[1] = int(re.sub(",", "", tempRentSplit[1]))
                rentDF = rentDF.append([tempRentSplit], ignore_index = True)
            elif tempRent == "Call for Rent": # Rent might not be listed
                rentDF = rentDF.append([[math.nan, math.nan]], ignore_index = True)
            else: # Else rent is a single value
                tempRent = int(re.sub(",", "", tempRent))
                rentDF = rentDF.append([[tempRent, tempRent]], ignore_index = True)
        else:
            rentDF = rentDF.append([[math.nan, math.nan]], ignore_index = True)

            
    
    
    # Rename columns, insert into dataframe and return dataframe
    rentDF.rename(index=str, columns={"0": "Min_Rent", "1": "Max_Rent"})
    df.insert(loc = 6, column = "Min_Rent", value = rentDF[0])
    df.insert(loc = 7, column = "Max_Rent", value = rentDF[1])

    return(df)
    
def GetSqFt(df):
    
    # Import required packages
    import pandas as pd
    import math
    import re
    
    sqFtDF = pd.DataFrame() # Initiate empty dataframe to store square feet
    
    # Loop trough square foot and get the square footage
    for sqft in df["Size"]:
        if isinstance(sqft, str) == True:
            tempSqFt = sqft.split(" Sq Ft")[0]
            tempSqFtSplit = tempSqFt.split(" - ") 
            if len(tempSqFtSplit) == 2:
                tempSqFtSplit[0] = int(re.sub(",", "", tempSqFtSplit[0]))
                tempSqFtSplit[1] = int(re.sub(",", "", tempSqFtSplit[1]))
                sqFtDF = sqFtDF.append([tempSqFtSplit], ignore_index = True)
            else:
                tempSqFt = int(re.sub(",", "", tempSqFt))
                sqFtDF = sqFtDF.append([[tempSqFt, tempSqFt]], ignore_index = True)
        else:
            sqFtDF = sqFtDF.append([[math.nan, math.nan]], ignore_index = True)

        
    # Insert column and return dataframe
    sqFtDF.rename(index=str, columns={"0": "Min_Sq_Ft", "1": "Max_Sq_Ft"})
    df.insert(loc = 8, column = "Min_Sq_Ft", value = sqFtDF[0])
    df.insert(loc = 9, column = "Max_Sq_Ft", value = sqFtDF[1])

    return(df)
    
def GetPetPolicy(df):
    
    # Import required packages
    import pandas as pd
    
    # Initialize empty data frame to store pet policy
    petPolicy = pd.DataFrame()
    
    for policy in df["Pet Policy"]:
        if isinstance(policy, str):
            if "Dogs Allowed" in policy:
                petPolicy = petPolicy.append([1], ignore_index = True)
            elif "Cats Allowed" in policy:
                petPolicy = petPolicy.append([2], ignore_index = True)
            elif "Dogs and Cats Allowed" in policy:
                petPolicy = petPolicy.append([3], ignore_index = True)
            elif "No Pets Allowed" in policy:
                petPolicy = petPolicy.append([4], ignore_index = True)
            elif "Pets Negotiable" in policy:
                petPolicy = petPolicy.append([5], ignore_index = True)
            elif "Other Pets Allowed" in policy:
                petPolicy = petPolicy.append([6], ignore_index = True)
            elif "Birds Allowed" in policy:
                petPolicy = petPolicy.append([7], ignore_index = True)
            elif "Birds and Fish Allowed" in policy:
                petPolicy = petPolicy.append([8], ignore_index = True)
            elif "Dogs, Cats and Other Pets Allowed" in policy:
                petPolicy = petPolicy.append([9], ignore_index = True)
            elif "Dogs, Cats, Birds, Fish, Reptiles and Other Pets Allowed" in policy:
                petPolicy = petPolicy.append([10], ignore_index = True)
            elif "Cats and Fish Allowed" in policy:
                petPolicy = petPolicy.append([11], ignore_index = True)
            elif "Cats, Birds and Fish Allowed" in policy:
                petPolicy = petPolicy.append([12], ignore_index = True)
            elif "Cats, Birds, Fish and Reptiles Allowed" in policy:
                petPolicy = petPolicy.append([13], ignore_index = True)
            elif "Cats, Birds, Fish, Reptiles and Other Pets Allowed" in policy:
                petPolicy = petPolicy.append([14], ignore_index = True)
        else:
            petPolicy = petPolicy.append([15], ignore_index = True)
            
    df.insert(loc = 10, column = "Pet_Policy", value = petPolicy)

    return(df)
        
# ----------------------------------------- END FUNCTIONS -----------------------------------------#
# ----------------------------------------- BEGIN SCRIPT -----------------------------------------#

# Import required packages
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import os

## -------------------------- Use the below code to get all data in its original form in a single data frame
#DataList = requests.get("https://worm.nyc3.digitaloceanspaces.com/") # Request html from data store
#soup = BeautifulSoup(DataList.text, "lxml") # Parse html
#DataList = soup.find_all("key") # Find the name of each csv file and store
#
## Initialize empty list to store url to files
Data = []
#
##Loop through csv files in list of data and append rest of url
#for files in DataList:
#    Data.append("https://worm.nyc3.digitaloceanspaces.com/"+files.text)
        

# Locally
folderpath = "C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Newly Obtained Property Data 9-29-17\\"

for files in os.listdir(folderpath):
    Data.append(folderpath+files)

# Initialize empty data frame to store all original data in a single data frame
df = pd.DataFrame()

# Loop through all csv files and append 
for files in Data:
    tempDF = pd.read_csv(files, encoding = "latin-1")
    df = df.append(tempDF, ignore_index = True) 
# -------------------------- Use the above code to get all data in its original form in a single data frame

# -------------------------- Use the below code to clean the data from its original form 
df = GetNames(df) # Gets the names of the properties
df = GetLinks(df) # Gets the link to property-level information 
df = GetAddresses(df) # Gets the addresses of each property
df = SplitAddresses(df)#, CityState[i][0:len(CityState[i]) - 2], CityState[i][len(CityState[i]) - 2:len(CityState[i])]) # Splits the address into street, city, state, zip
#df = GetMinMaxRent(df) # Creates new columns for minimum rent and maximum rent
#df = GetSqFt(df) # Creates new columns for minimum sq ft, maximum sq fit
#df = GetPetPolicy(df) # In progress working on how to unpack pet policy
df = DropCols(df) # Drops columns no longer necessary
# -------------------------- Use the above code to clean the data from its original form 


# ----------------------------------------- END SCRIPT -----------------------------------------#
        
