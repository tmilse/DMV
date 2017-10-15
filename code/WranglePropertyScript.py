# -*- coding: utf-8 -*-
"""
Description: This file contains a script that can be used to run functions that will clean the property-level data.

"""

# ----------------------------------------- BEGIN SCRIPT -----------------------------------------#

# Import required packages
import pandas as pd
import os
from WranglePropertyFunctions import *

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
Property = pd.DataFrame()
folder = '//Users//nicholaskallfa//DMV//data//property data//'


for file in os.listdir(folder):
    df = pd.read_csv(folder+file, encoding = "latin-1")   
    Property = Property.append(df, ignore_index = True)
    
# -------------------------- Use the above code to get all data in its original form in a single data frame

# -------------------------- Use the below code to clean the data from its original form 
Address = SplitAddresses(GetAddresses(Property)) # Get addresses
Address.drop_duplicates(subset = ["address", "city", "state", "zip"], keep = "first", inplace = True) # Get and remove duplicates
Address.pid = range(0,len(Address)) # Rewrite pid
Property = Property.loc[Address.index] # Remove duplicates from Property
Property.index = range(0, len(Property)) # Rewrite index
Address.index = range(0,len(Address)) # Rewrite index
#NumImage, Images = GetImage(Property) # Get number of images for each property and image links/descriptions
#Names = GetNames(Property) # Gets the names of the properties
#Links = GetLinks(Property) # Get links to apartments.com page for property
#Links["url"][3218] = "https://www.apartments.com/waverly-gardens-62-or-better-woodstock-md/3xvedvg/" # Manually set these links
#Links["url"][6465] = "https://www.apartments.com/the-upton-res-rockville-md/2jsvz4c/" # Manually set these links
#Contact = SplitPhone(Property)
#PetsAllowed = GetPetPolicy(Property)
#Parking = GetParkingPolicy(Property)
#Features = GetFeatures(Property, "Features")
#Gym = GetFeatures(Property, "Gym")
#Kitchen = GetFeatures(Property, "Kitchen")
#Amenities = GetFeatures(df, "Amenities")
#LivingSpace = GetFeatures(Property, "Living Space")
#Services = GetFeatures(Property, "Services")
#PropertyInfo = GetFeatures(Property, "Property Info")
#PropertyInfo = UnpackPropInfo(PropertyInfo)
#IndoorInfo = GetFeatures(Property, "Indoor Info")
#OutdoorInfo = GetFeatures(Property, "Outdoor Info")
#MonthlyFeesMin, MonthlyFeesMax = GetFees(Property, "Monthly Fees")
OneTimeFeesMin, OneTimeFeesMax = GetFees(Property, "One Time Fees")
#FeaturesLU, GymLU, KitchenLU, LivingSpaceLU, ServicesLU, IndoorInfoLU, OutdoorInfoLU = GetLookupTables(True)
#PropertyDesc = Property[["Description"]]
#PropertyDesc["pid"] = range(0, len(PropertyDesc))
#PropertyDesc = PropertyDesc[["pid", "Description"]]
#PropertyDesc.rename(columns = {"Description": "desc"}, inplace = True)
#PropertyDesc = GetCapitalization(PropertyDesc)
#
## Write outputs of script to CSV
#Names.to_csv("Name.csv", index = False)
#Links.to_csv("Link.csv", index = False)
#Address.to_csv("Address.csv", index = False)
#Contact.to_csv("Contact.csv", index = False)
#PetsAllowed.to_csv("Pets.csv", index = False)
#Parking.to_csv("Parking.csv", index = False)
#Features.to_csv("Features.csv", index = False)
#Gym.to_csv("Gym.csv", index = False)
#Kitchen.to_csv("Kitchen.csv", index = False)
#LivingSpace.to_csv("LivingSpace.csv", index = False)
#Services.to_csv("Services.csv", index = False)
#PropertyInfo.to_csv("PropertyInfo.csv", index = False)
#IndoorInfo.to_csv("IndoorInfo.csv", index = False)
#OutdoorInfo.to_csv("OutdoorInfo.csv", index = False)
#MonthlyFeesMin.to_csv("MonthlyFeesMin.csv", index = False)
#MonthlyFeesMax.to_csv("MonthlyFeesMax.csv", index = False)
#OneTimeFeesMin.to_csv("OneTimeFeesMin.csv", index = False)
#OneTimeFeesMax.to_csv("OneTimeFeesMax.csv", index = False)
#NumImage.to_csv("NumImage.csv", index = False)
#Im.to_csv("Images.csv", index = False)


## Sort the lookup tables alphabetically
#FeaturesLU.sort_values(["desc"], inplace = True)
#FeaturesLU.index = range(0, len(FeaturesLU))
#GymLU.sort_values(["desc"], inplace = True)
#GymLU.index = range(0, len(GymLU))
#KitchenLU.sort_values(["desc"], inplace = True)
#KitchenLU.index = range(0, len(KitchenLU))
#LivingSpaceLU.sort_values(["desc"], inplace = True)
#LivingSpaceLU.index = range(0, len(LivingSpaceLU))
#ServicesLU.sort_values(["desc"], inplace = True)
#ServicesLU.index = range(0, len(ServicesLU))
#IndoorInfoLU.sort_values(["desc"], inplace = True)
#IndoorInfoLU.index = range(0, len(IndoorInfoLU))
#OutdoorInfoLU.sort_values(["desc"], inplace = True)
#OutdoorInfoLU.index = range(0, len(OutdoorInfoLU))
#
## Write lookup tables to csv
#FeaturesLU.to_csv("FeaturesLU.csv", index = False)
#GymLU.to_csv("GymLU.csv", index = False)
#KitchenLU.to_csv("KitchenLU.csv", index = False)
#LivingSpaceLU.to_csv("LivingSpaceLU.csv", index = False)
#ServicesLU.to_csv("ServicesLU.csv", index = False)
#IndoorInfoLU.to_csv("IndoorInfoLU.csv", index = False)
#OutdoorInfoLU.to_csv("OutdoorInfoLU.csv", index = False)

# -------------------------- Use the above code to clean the data from its original form 
# ----------------------------------------- END SCRIPT -----------------------------------------#

""" ----------------------------------------- BEGIN THINGS TO DO -----------------------------------------

1. Change encoding of description column
2. Scrape apartment ratings?
3. Optionally choose to remove rows with zip codes 21236, 21234, 21128, 21117, 21208
4. Columns of onetimefees

# ----------------------------------------- END THINGS TO DO -----------------------------------------"""

# ----------------------------------------- BEGIN OLD CODE -----------------------------------------#

# ----------------------------------------- END OLD CODE -----------------------------------------#
