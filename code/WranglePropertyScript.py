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
folder = 'C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\DMV\\data\\property data\\'


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
Names = GetNames(Property) # Gets the names of the properties
Links = GetLinks(Property) # Get links to apartments.com page for property
Links["url"][3218] = "https://www.apartments.com/waverly-gardens-62-or-better-woodstock-md/3xvedvg/" # Manually set these links
Links["url"][6465] = "https://www.apartments.com/the-upton-res-rockville-md/2jsvz4c/" # Manually set these links
Contact = SplitPhone(Property)
PetsAllowed = GetPetPolicy(Property)
Parking = GetParkingPolicy(Property)
Features = GetFeatures(Property, "Features")
Gym = GetFeatures(Property, "Gym")
Kitchen = GetFeatures(Property, "Kitchen")
#Amenities = GetFeatures(df, "Amenities")
LivingSpace = GetFeatures(Property, "Living Space")
Services = GetFeatures(Property, "Services")
PropertyInfo = GetFeatures(Property, "Property Info")
PropertyInfo = UnpackPropInfo(PropertyInfo)
IndoorInfo = GetFeatures(Property, "Indoor Info")
OutdoorInfo = GetFeatures(Property, "Outdoor Info")
MonthlyFeesMin, MonthlyFeesMax = GetFees(Property, "Monthly Fees")
OneTimeFeesMin, OneTimeFeesMax = GetFees(Property, "One Time Fees")
FeaturesLU, GymLU, KitchenLU, LivingSpaceLU, ServicesLU, IndoorInfoLU, OutdoorInfoLU = GetLookupTables(True)

# Write outputs of script to CSV
Names.to_csv("Name.csv", index = False)
Links.to_csv("Link.csv", index = False)
Address.to_csv("Address.csv", index = False)
Contact.to_csv("Contact.csv", index = False)
PetsAllowed.to_csv("Pets.csv", index = False)
Parking.to_csv("Parking.csv", index = False)
Features.to_csv("Features.csv", index = False)
Gym.to_csv("Gym.csv", index = False)
Kitchen.to_csv("Kitchen.csv", index = False)
LivingSpace.to_csv("LivingSpace.csv", index = False)
Services.to_csv("Services.csv", index = False)
PropertyInfo.to_csv("PropertyInfo.csv", index = False)
IndoorInfo.to_csv("IndoorInfo.csv", index = False)
OutdoorInfo.to_csv("OutdoorInfo.csv", index = False)
MonthlyFeesMin.to_csv("MonthlyFeesMin.csv", index = False)
MonthlyFeesMax.to_csv("MonthlyFeesMax.csv", index = False)
OneTimeFeesMin.to_csv("OneTimeFeesMin.csv", index = False)
OneTimeFeesMax.to_csv("OneTimeFeesMax.csv", index = False)

# Sort the lookup tables alphabetically
FeaturesLU.sort_values(["desc"], inplace = True)
FeaturesLU.index = range(0, len(FeaturesLU))
GymLU.sort_values(["desc"], inplace = True)
GymLU.index = range(0, len(GymLU))
KitchenLU.sort_values(["desc"], inplace = True)
KitchenLU.index = range(0, len(KitchenLU))
LivingSpaceLU.sort_values(["desc"], inplace = True)
LivingSpaceLU.index = range(0, len(LivingSpaceLU))
ServicesLU.sort_values(["desc"], inplace = True)
ServicesLU.index = range(0, len(ServicesLU))
IndoorInfoLU.sort_values(["desc"], inplace = True)
IndoorInfoLU.index = range(0, len(IndoorInfoLU))
OutdoorInfoLU.sort_values(["desc"], inplace = True)
OutdoorInfoLU.index = range(0, len(OutdoorInfoLU))

# Write lookup tables to csv
FeaturesLU.to_csv("FeaturesLU.csv", index = False)
GymLU.to_csv("GymLU.csv", index = False)
KitchenLU.to_csv("KitchenLU.csv", index = False)
LivingSpaceLU.to_csv("LivingSpaceLU.csv", index = False)
ServicesLU.to_csv("ServicesLU.csv", index = False)
IndoorInfoLU.to_csv("IndoorInfoLU.csv", index = False)
OutdoorInfoLU.to_csv("OutdoorInfoLU.csv", index = False)

# -------------------------- Use the above code to clean the data from its original form 
# ----------------------------------------- END SCRIPT -----------------------------------------#

""" ----------------------------------------- BEGIN THINGS TO DO -----------------------------------------

1. **Condense features in Amenities column and PropertyInfo column**
2. Add function to extract number of images
3. Change encoding of description column
4. Should we try to parse the Lease column or just ignore it?
5. Add feature to extract whether parking is assigned/unassigned
6. **Add function for lookup tables for Amenities and PropertyInfo columns**
7. Extract apartment type (apartment, townhome, etc...)
    See reviewUtils in html code
8. Scrape apartment ratings?

# ----------------------------------------- END THINGS TO DO -----------------------------------------"""

# ----------------------------------------- BEGIN OLD CODE -----------------------------------------#
#def DropCols(df):
#    
#    # Import required package
#    import pandas as pd
#    
#    # Drop columns labeled Distance and Duration from dataframe
#    df.drop(labels = ["Distance","Duration","Option Name", "Rent", "Size"], axis = 1, inplace = True)
#    
#    # Return dataframe
#    return(df)
#test = AllCities.loc[(AllCities["City"] == " Fredericksburg") | (AllCities["City"] == " Frederick")]
#
#def GetPetPolicy(df):
#    
#    # Import required packages
#    import pandas as pd
#    
#    # Initialize empty data frame to store pet policy
#    petPolicy = pd.DataFrame()
#    
#    for policy in df["Pet Policy"]:
#        if isinstance(policy, str):
#            if "Dogs Allowed" in policy:
#                petPolicy = petPolicy.append([1], ignore_index = True)
#            elif "Cats Allowed" in policy:
#                petPolicy = petPolicy.append([2], ignore_index = True)
#            elif "Dogs and Cats Allowed" in policy:
#                petPolicy = petPolicy.append([3], ignore_index = True)
#            elif "No Pets Allowed" in policy:
#                petPolicy = petPolicy.append([4], ignore_index = True)
#            elif "Pets Negotiable" in policy:
#                petPolicy = petPolicy.append([5], ignore_index = True)
#            elif "Other Pets Allowed" in policy:
#                petPolicy = petPolicy.append([6], ignore_index = True)
#            elif "Birds Allowed" in policy:
#                petPolicy = petPolicy.append([7], ignore_index = True)
#            elif "Birds and Fish Allowed" in policy:
#                petPolicy = petPolicy.append([8], ignore_index = True)
#            elif "Dogs, Cats and Other Pets Allowed" in policy:
#                petPolicy = petPolicy.append([9], ignore_index = True)
#            elif "Dogs, Cats, Birds, Fish, Reptiles and Other Pets Allowed" in policy:
#                petPolicy = petPolicy.append([10], ignore_index = True)
#            elif "Cats and Fish Allowed" in policy:
#                petPolicy = petPolicy.append([11], ignore_index = True)
#            elif "Cats, Birds and Fish Allowed" in policy:
#                petPolicy = petPolicy.append([12], ignore_index = True)
#            elif "Cats, Birds, Fish and Reptiles Allowed" in policy:
#                petPolicy = petPolicy.append([13], ignore_index = True)
#            elif "Cats, Birds, Fish, Reptiles and Other Pets Allowed" in policy:
#                petPolicy = petPolicy.append([14], ignore_index = True)
#        else:
#            petPolicy = petPolicy.append([15], ignore_index = True)
#            
#    df.insert(loc = 10, column = "Pet_Policy", value = petPolicy)
#
#    return(df)
#
#def GetGym(df):
#    
#    import pandas as pd
#    
#    gymDF = pd.DataFrame()
#    i = 0
#    pid = pd.DataFrame()
#    
#    for elements in df["Gym"]:
#        if isinstance(elements, str):
#            tempElements = elements.split("* ")
#            tempElements2 = []
#            for x in tempElements[1:]:
#                tempElements2.append(x.strip().replace("\n", ""))
#            gymDF = gymDF.append(tempElements2, ignore_index = True)
#            pid = pid.append([i]*len(tempElements2), ignore_index = True)
#            i+=1
#        else:
#            gymDF = gymDF.append(["NA"], ignore_index = True)
#            pid = pid.append([i], ignore_index = True)
#            i+=1
#
#    GymDF = pd.DataFrame()
#    GymDF["pid"] = pid[0]
#    GymDF["gymfeat"] = gymDF[0]
#    
#    return(GymDF)
#    
#def GetKitchen(df):
#    
#    import pandas as pd
#    
#    kitchDF = pd.DataFrame()
#    i = 0
#    pid = pd.DataFrame()
#    
#    for elements in df["Kitchen"]:
#        if isinstance(elements, str):
#            tempElements = elements.split("* ")
#            tempElements2 = []
#            for x in tempElements[1:]:
#                tempElements2.append(x.strip().replace("\n", ""))
#            kitchDF = kitchDF.append(tempElements2, ignore_index = True)
#            pid = pid.append([i]*len(tempElements2), ignore_index = True)
#            i+=1
#        else:
#            kitchDF = kitchDF.append(["NA"], ignore_index = True)
#            pid = pid.append([i], ignore_index = True)
#            i+=1
#
#    KitchenDF = pd.DataFrame()
#    KitchenDF["pid"] = pid[0]
#    KitchenDF["kitchenfeat"] = kitchDF[0]
#    
#    return(KitchenDF)
#    
#def GetAmenities(df):
# 
#    
#    import pandas as pd
#    
#    amenDF = pd.DataFrame()
#    i = 0
#    pid = pd.DataFrame()
#    
#    for elements in df["Amenities"]:
#        if isinstance(elements, str):
#            tempElements = elements.split("* ")
#            tempElements2 = []
#            for x in tempElements[1:]:
#                tempElements2.append(x.strip().replace("\n", ""))
#            amenDF = amenDF.append(tempElements2, ignore_index = True)
#            pid = pid.append([i]*len(tempElements2), ignore_index = True)
#            i+=1
#        else:
#            amenDF = amenDF.append(["NA"], ignore_index = True)
#            pid = pid.append([i], ignore_index = True)
#            i+=1
#
#    AmenitiesDF = pd.DataFrame()
#    AmenitiesDF["pid"] = pid[0]
#    AmenitiesDF["amenfeat"] = amenDF[0]
#    
#    return(AmenitiesDF)  
#    
#def GetLivingSpace(df):
#
#    
#    import pandas as pd
#    
#    livspaceDF = pd.DataFrame()
#    i = 0
#    pid = pd.DataFrame()
#    
#    for elements in df["Living Space"]:
#        if isinstance(elements, str):
#            tempElements = elements.split("* ")
#            tempElements2 = []
#            for x in tempElements[1:]:
#                tempElements2.append(x.strip().replace("\n", ""))
#            livspaceDF = livspaceDF.append(tempElements2, ignore_index = True)
#            pid = pid.append([i]*len(tempElements2), ignore_index = True)
#            i+=1
#        else:
#            livspaceDF = livspaceDF.append(["NA"], ignore_index = True)
#            pid = pid.append([i], ignore_index = True)
#            i+=1
#
#    LivingSpaceDF = pd.DataFrame()
#    LivingSpaceDF["pid"] = pid[0]
#    LivingSpaceDF["livingspacefeat"] = livspaceDF[0]
#    
#    return(LivingSpaceDF)  
#
#def GetServices(df):
#    
#    import pandas as pd
#    
#    servDF = pd.DataFrame()
#    i = 0
#    pid = pd.DataFrame()
#    
#    for elements in df["Services"]:
#        if isinstance(elements, str):
#            tempElements = elements.split("* ")
#            tempElements2 = []
#            for x in tempElements[1:]:
#                tempElements2.append(x.strip().replace("\n", ""))
#            servDF = servDF.append(tempElements2, ignore_index = True)
#            pid = pid.append([i]*len(tempElements2), ignore_index = True)
#            i+=1
#        else:
#            servDF = servDF.append(["NA"], ignore_index = True)
#            pid = pid.append([i], ignore_index = True)
#            i+=1
#
#    ServicesDF = pd.DataFrame()
#    ServicesDF["pid"] = pid[0]
#    ServicesDF["servicesfeat"] = servDF[0]
#    
#    return(ServicesDF)
#    
#def GetPropertyInfo(df):
#
#    
#    import pandas as pd
#    
#    propinfoDF = pd.DataFrame()
#    i = 0
#    pid = pd.DataFrame()
#    
#    for elements in df["Property Info"]:
#        if isinstance(elements, str):
#            tempElements = elements.split("* ")
#            tempElements2 = []
#            for x in tempElements[1:]:
#                tempElements2.append(x.strip().replace("\n", ""))
#            propinfoDF = propinfoDF.append(tempElements2, ignore_index = True)
#            pid = pid.append([i]*len(tempElements2), ignore_index = True)
#            i+=1
#        else:
#            propinfoDF = propinfoDF.append(["NA"], ignore_index = True)
#            pid = pid.append([i], ignore_index = True)
#            i+=1
#
#    PropertyInfoDF = pd.DataFrame()
#    PropertyInfoDF["pid"] = pid[0]
#    PropertyInfoDF["propertyfeat"] = propinfoDF[0]
#    
#    return(PropertyInfoDF)
#    
#def GetIndoorInfo(df):
#
#    
#    import pandas as pd
#    
#    indoorinfoDF = pd.DataFrame()
#    i = 0
#    pid = pd.DataFrame()
#    
#    for elements in df["Indoor Info"]:
#        if isinstance(elements, str):
#            tempElements = elements.split("* ")
#            tempElements2 = []
#            for x in tempElements[1:]:
#                tempElements2.append(x.strip().replace("\n", ""))
#            indoorinfoDF = indoorinfoDF.append(tempElements2, ignore_index = True)
#            pid = pid.append([i]*len(tempElements2), ignore_index = True)
#            i+=1
#        else:
#            indoorinfoDF = indoorinfoDF.append(["NA"], ignore_index = True)
#            pid = pid.append([i], ignore_index = True)
#            i+=1
#
#    IndoorInfoDF = pd.DataFrame()
#    IndoorInfoDF["pid"] = pid[0]
#    IndoorInfoDF["indoorfeat"] = indoorinfoDF[0]
#    
#    return(IndoorInfoDF)
#    
#def GetOutdoorInfo(df):
#
#    
#    import pandas as pd
#    
#    outdoorinfoDF = pd.DataFrame()
#    i = 0
#    pid = pd.DataFrame()
#    
#    for elements in df["Outdoor Info"]:
#        if isinstance(elements, str):
#            tempElements = elements.split("* ")
#            tempElements2 = []
#            for x in tempElements[1:]:
#                tempElements2.append(x.strip().replace("\n", ""))
#            outdoorinfoDF = outdoorinfoDF.append(tempElements2, ignore_index = True)
#            pid = pid.append([i]*len(tempElements2), ignore_index = True)
#            i+=1
#        else:
#            outdoorinfoDF = outdoorinfoDF.append(["NA"], ignore_index = True)
#            pid = pid.append([i], ignore_index = True)
#            i+=1
#
#    OutdoorInfoDF = pd.DataFrame()
#    OutdoorInfoDF["pid"] = pid[0]
#    OutdoorInfoDF["outdoorfeat"] = outdoorinfoDF[0]
#    
#    return(OutdoorInfoDF)
#
#def GetMinMaxRent(df):
#    
#    # Import required packages
#    import re
#    import math
#    
#    rentDF = pd.DataFrame() # Initiate empty dataframe to store min/max rent
#    
#    # Loop through rent and get min/max rent
#    for rent in df["Rent"]:
#        if isinstance(rent, str):
#            tempRent = re.sub("\$", "", rent)
#            tempRentSplit = tempRent.split(" - ") 
#            if len(tempRentSplit) == 2: #Rent could be given as a range
#                tempRentSplit[0] = int(re.sub(",", "", tempRentSplit[0]))
#                tempRentSplit[1] = int(re.sub(",", "", tempRentSplit[1]))
#                rentDF = rentDF.append([tempRentSplit], ignore_index = True)
#            elif tempRent == "Call for Rent": # Rent might not be listed
#                rentDF = rentDF.append([[math.nan, math.nan]], ignore_index = True)
#            else: # Else rent is a single value
#                tempRent = int(re.sub(",", "", tempRent))
#                rentDF = rentDF.append([[tempRent, tempRent]], ignore_index = True)
#        else:
#            rentDF = rentDF.append([[math.nan, math.nan]], ignore_index = True)
#
#            
#    
#    
#    # Rename columns, insert into dataframe and return dataframe
#    rentDF.rename(index=str, columns={"0": "Min_Rent", "1": "Max_Rent"})
#    df.insert(loc = 6, column = "Min_Rent", value = rentDF[0])
#    df.insert(loc = 7, column = "Max_Rent", value = rentDF[1])
#
#    return(df)
#    
#def GetSqFt(df):
#    
#    # Import required packages
#    import pandas as pd
#    import math
#    import re
#    
#    sqFtDF = pd.DataFrame() # Initiate empty dataframe to store square feet
#    
#    # Loop trough square foot and get the square footage
#    for sqft in df["Size"]:
#        if isinstance(sqft, str) == True:
#            tempSqFt = sqft.split(" Sq Ft")[0]
#            tempSqFtSplit = tempSqFt.split(" - ") 
#            if len(tempSqFtSplit) == 2:
#                tempSqFtSplit[0] = int(re.sub(",", "", tempSqFtSplit[0]))
#                tempSqFtSplit[1] = int(re.sub(",", "", tempSqFtSplit[1]))
#                sqFtDF = sqFtDF.append([tempSqFtSplit], ignore_index = True)
#            else:
#                tempSqFt = int(re.sub(",", "", tempSqFt))
#                sqFtDF = sqFtDF.append([[tempSqFt, tempSqFt]], ignore_index = True)
#        else:
#            sqFtDF = sqFtDF.append([[math.nan, math.nan]], ignore_index = True)
#
#        
#    # Insert column and return dataframe
#    sqFtDF.rename(index=str, columns={"0": "Min_Sq_Ft", "1": "Max_Sq_Ft"})
#    df.insert(loc = 8, column = "Min_Sq_Ft", value = sqFtDF[0])
#    df.insert(loc = 9, column = "Max_Sq_Ft", value = sqFtDF[1])
#
#    return(df)
#
#def GetOneTimeFees(df):
#    
#    import pandas as pd
#    import math
#    
#    feesDF = pd.DataFrame()
#    PropertyID = pd.DataFrame()
#    
#    i = 0
#    for fees in df["One Time Fees"]:
#        if isinstance(fees, str):
#            tempFees = fees.split("* ")
#            feesDF = feesDF.append(tempFees[1:], ignore_index = True)
#            PropertyID = PropertyID.append([i]*len(tempFees[1:]), ignore_index = True)
#            i+=1
#        else:
#            feesDF = feesDF.append(["NA"], ignore_index = True)
#            PropertyID = PropertyID.append([i], ignore_index = True)
#            i+=1
#    
#    df_final = pd.DataFrame()
#    df_final["fees"] = feesDF[0]
#    df_final["PropertyID"] = PropertyID[0]
#    
#    Description = pd.DataFrame()
#    Cost = pd.DataFrame()
#    
#    for fees in df_final["fees"]:
#        tempFees = fees.strip().split(":")
#        if len(tempFees) == 1:
#            Description = Description.append(tempFees, ignore_index = True)
#            Cost = Cost.append(tempFees, ignore_index = True)
#        else:
#            Description = Description.append([tempFees[0]], ignore_index = True)
#            Cost = Cost.append([tempFees[1]], ignore_index = True)
#
#    df_final["desc"] = Description[0]
#    df_final["cost"] = Cost[0]
#
#    i = 0
#    Split = pd.DataFrame()
#    PropertyID2 = pd.DataFrame()
#    MinCost = pd.DataFrame()
#    MaxCost = pd.DataFrame()
#    
#    for desc in df_final["desc"]:
#        temp = desc.split(",")
#        Split = Split.append(temp, ignore_index = True)
#        if len(temp) == 1:
#            PropertyID2 = PropertyID2.append([df_final.PropertyID[i]], ignore_index = True)
#        else:
#            PropertyID2 = PropertyID2.append([df_final.PropertyID[i]]*len(temp), ignore_index = True)
#        tempCost = df_final["cost"][i].replace("$", "")
#        tempCost = tempCost.replace(",", "")
#        tempCost = tempCost.replace("\n", "")
#        tempCost = tempCost.split(" - ")
#        if len(tempCost) == 2:
#            MinCost = MinCost.append([int(tempCost[0])], ignore_index = True)
#            MaxCost = MaxCost.append([int(tempCost[1])], ignore_index = True)
#        elif "Included" in tempCost[0]:
#            MinCost = MinCost.append([0]*len(temp), ignore_index = True)
#            MaxCost = MaxCost.append([0]*len(temp), ignore_index = True)
#        elif "NA" == tempCost[0]:
#            MinCost = MinCost.append([math.nan], ignore_index = True)
#            MaxCost = MaxCost.append([math.nan], ignore_index = True)
#        else:
#            MinCost = MinCost.append([int(tempCost[0])], ignore_index = True)
#            MaxCost = MaxCost.append([int(tempCost[0])], ignore_index = True)
#
#        i+=1
#    
#    Split = pd.DataFrame(Split[0].apply(lambda x: x.strip()))
#    
#    df_final2 = pd.DataFrame()
#    df_final2["pid"] = PropertyID2[0]
#    df_final2["desc"] = Split[0]
#    df_final2["mincost"] = MinCost[0]
#    df_final2["maxcost"] = MaxCost[0]
#    
#    return(df_final2)
#
#def RenameColumns(df, column):
#    
#    import pandas as pd
#    
#    if column == "One Time Fees":
#        df.loc[df["desc"] == "Cat Deposit",  "desc"] = "Cat Fee"
#        df.loc[df["desc"] == "Dog Deposit",  "desc"] = "Dog Fee"
#        df.loc[df["desc"] == "Other",  "desc"] = "Other Fee"
#        df.loc[df["desc"] == "Other Deposit",  "desc"] = "Other Fee"
#        df.loc[df["desc"] == "Bird Deposit",  "desc"] = "Bird Fee"
#        df.loc[df["desc"] == "Fish Deposit",  "desc"] = "Fish Fee"
#        df.loc[df["desc"] == "Reptile Deposit",  "desc"] = "Reptile Fee"
#    else:
#        df.loc[df["desc"] == "Unassigned Surface Lot Parking",  "desc"] = "Lot Parking Fee"
#        df.loc[df["desc"] == "Assigned Covered Parking",  "desc"] = "Covered Parking Fee"
#        df.loc[df["desc"] == "Trash Removal",  "desc"] = "Trash Removal Fee"
#        df.loc[df["desc"] == "Sewer",  "desc"] = "Sewer Fee"
#        df.loc[df["desc"] == "Assigned Surface Lot Parking",  "desc"] = "Lot Parking Fee"
#        df.loc[df["desc"] == "Gas",  "desc"] = "Gas Fee"
#        df.loc[df["desc"] == "Water",  "desc"] = "Water Fee"
#        df.loc[df["desc"] == "Unassigned Garage Parking",  "desc"] = "Covered Parking Fee"        
#        df.loc[df["desc"] == "Assigned Other Parking",  "desc"] = "Parking Fee"
#        df.loc[df["desc"] == "Unassigned Covered Parking",  "desc"] = "Covered Parking Fee"
#        df.loc[df["desc"] == "Electricity",  "desc"] = "Electricity Fee"
#        df.loc[df["desc"] == "Heat",  "desc"] = "Heat Fee"
#        df.loc[df["desc"] == "Air Conditioning",  "desc"] = "Air Conditioning Fee"
#        df.loc[df["desc"] == "Assigned Garage Parking",  "desc"] = "Covered Parking Fee"
#        df.loc[df["desc"] == "Unassigned Other Parking",  "desc"] = "Parking Fee"
#        df.loc[df["desc"] == "Cable",  "desc"] = "Cable Fee"
#        df.loc[df["desc"] == "Bird Rent",  "desc"] = "Bird Fee"
#        df.loc[df["desc"] == "Fish Rent",  "desc"] = "Fish Fee"
#        df.loc[df["desc"] == "Reptile Rent",  "desc"] = "Reptile Fee"
#        df.loc[df["desc"] == "Other Rent",  "desc"] = "Other Fee"
#        df.loc[df["desc"] == "Unassigned Street Parking",  "desc"] = "Street Parking Fee"
#        
#    return(df)
#
# ----------------------------------------- END OLD CODE -----------------------------------------#
