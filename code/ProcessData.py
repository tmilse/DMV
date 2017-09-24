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
    zipCodeDF = pd.DataFrame(columns = ["Zip_Code"]) # Initiate empty dataframe to store zip codes

    # Loop through elements and grab address and zip code
    for element in df["Address"]:
        tempAddress = pd.DataFrame([element.split(",")[0]], columns = ["Address"])
        tempZipCode = pd.DataFrame([element[len(element)-5:len(element)]], columns = ["Zip_Code"])
        addressesDF = addressesDF.append(tempAddress, ignore_index = True)
        zipCodeDF = zipCodeDF.append(tempZipCode, ignore_index = True)

    # Insert address, city, and zip code into dataframe and return dataframe
    df.drop(labels = "Address", axis = 1, inplace = True)
    df.insert(loc = 2, column = "Address", value = addressesDF)
    df.insert(loc = 3, column = "City", value = ["District of Columbia"]*len(zipCodeDF)) # NEED TO CHANGE THIS TO THE APPROPRIATE CITY IN THE FUTURE
    df.insert(loc = 4, column = "Zip_Code", value = zipCodeDF)
    return(df)

def GetMinMaxRent(df):
    
    # Import required packages
    import re
    
    rentDF = pd.DataFrame() # Initiate empty dataframe to store min/max rent
    
    # Loop through rent and get min/max rent
    for rent in df["Rent"]:
        tempRent = re.sub("\$", "", rent)
        tempRentSplit = tempRent.split(" - ") 
        if len(tempRentSplit) == 2: #Rent could be given as a range
            rentDF = rentDF.append([tempRentSplit], ignore_index = True)
        elif tempRent == "Call for Rent": # Rent might not be listed
            rentDF = rentDF.append([["NA", "NA"]], ignore_index = True)
        else: # Else rent is a single value
            rentDF = rentDF.append([[tempRent, tempRent]], ignore_index = True)
    
    # Rename columns, insert into dataframe and return dataframe
    rentDF.rename(index=str, columns={"0": "Min_Rent", "1": "Max_Rent"})
    df.insert(loc = 5, column = "Min_Rent", value = rentDF[0])
    df.insert(loc = 6, column = "Max_Rent", value = rentDF[1])

    return(df)
    
def GetSqFt(df):
    
    # Import required packages
    import pandas as pd
    
    sqFtDF = pd.DataFrame() # Initiate empty dataframe to store square feet
    
    # Loop trough square foot and get the square footage
    for sqft in df["Size"]:
        if isinstance(sqft, str) == True:
            tempSqFt = sqft.split(" Sq Ft")[0]
            tempSqFtSplit = tempSqFt.split(" - ") 
            if len(tempSqFtSplit) == 2:
                sqFtDF = sqFtDF.append([tempSqFtSplit], ignore_index = True)
            else:
                sqFtDF = sqFtDF.append([[tempSqFt, tempSqFt]], ignore_index = True)
        else:
            sqFtDF = sqFtDF.append([["NA", "NA"]], ignore_index = True)

        
    # Insert column and return dataframe
    sqFtDF.rename(index=str, columns={"0": "Min_Sq_Ft", "1": "Max_Sq_Ft"})
    df.insert(loc = 7, column = "Min_Sq_Ft", value = sqFtDF[0])
    df.insert(loc = 8, column = "Max_Sq_Ft", value = sqFtDF[1])

    return(df)
        
# ----------------------------------------- END FUNCTIONS -----------------------------------------#
# ----------------------------------------- BEGIN SCRIPT -----------------------------------------#

# Import required packages
import pandas as pd

# Just for DC apartments for now
df = pd.read_csv("https://worm.nyc3.digitaloceanspaces.com/apartmentsDC.csv", encoding = "latin-1")
df = GetNames(df)
df = GetLinks(df)
df = GetAddresses(df)
df = SplitAddresses(df)
df = GetMinMaxRent(df)
df = GetSqFt(df)
df = DropCols(df)
