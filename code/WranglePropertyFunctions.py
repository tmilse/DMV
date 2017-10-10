# -*- coding: utf-8 -*-
"""
Description: This file contains functions that will take the original property-level data and clean it as needed. A 
             separate script is used to run the functions to clean the data. 

"""

# ----------------------------------------- BEGIN FUNCTIONS -----------------------------------------#

def RemoveDuplicates(df):

    import os
    
    index = []
    
    for i in range(0, len(df)):
        if os.path.isfile("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data Rename\\PropertyID"+str(i)+".html") == True:
            index.append(i)
    
    outputDF = df.loc[index,:]
    outputDF.index = range(0, len(outputDF))
    
    return(outputDF)
    
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
    
    # Initialize data frame for output
    outputDF = pd.DataFrame()
    L = len(df)
    
    # Put data into data frame for output
    outputDF["pid"] = range(0, L)
    outputDF["name"] = namesDF
    
    # Return data frame
    return(outputDF)

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
    
    # Initialize data frame for output
    outputDF = pd.DataFrame()
    L = len(df)
    
    # Put data into data frame for output
    outputDF["pid"] = range(0, L)
    outputDF["url"] = linksDF
    
    # Return data frame
    return(outputDF)
    
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
    
    # Initialize data frame for output
    outputDF = pd.DataFrame()
    L = len(df)
    
    # Put data into data frame for output
    outputDF["pid"] = range(0, L)
    outputDF["address"] = addressesDF["Address"]
    
    # Return data frame
    return(outputDF)
    
def SplitAddresses(df):
    
    #Import required package
    import pandas as pd
    
    # Initialize empty data frames
    addressesDF = pd.DataFrame(columns = ["Address"]) # Initiate empty dataframe to store addresses
    cityDF = pd.DataFrame(columns = ["City"]) # Initiate empty dataframe to store city
    stateDF = pd.DataFrame(columns = ["State"]) # Initiate empty dataframe to store state
    zipCodeDF = pd.DataFrame(columns = ["Zip_Code"]) # Initiate empty dataframe to store zip codes

    # Loop through elements and grab address and zip code
    for element in df["address"]:
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

    # Initialize data frame for output
    outputDF = pd.DataFrame()
    L = len(df)
    
    # Put data into data frame for output
    outputDF["pid"] = range(0, L)
    outputDF["address"] = addressesDF["Address"]
    outputDF["city"] = cityDF["City"]
    outputDF["state"] = stateDF["State"]
    outputDF["zip"] = zipCodeDF["Zip_Code"]
    
    # Return data frame
    return(outputDF)
    
def SplitPhone(df):
    
    # Import required packages
    import pandas as pd
    import math
    
    # Get area code and rest of phone number
    areacode = df["Contact"].apply(lambda x: x.split("-")[0] if isinstance(x,str) else math.nan)
    phone = df["Contact"].apply(lambda x: "".join(x.split("-")[1:]) if isinstance(x,str) else math.nan)
    
    # Create data frame for the area code and phone number for the property
    contact = pd.DataFrame()
    contact["pid"] = range(0,len(df))
    contact["areacode"] = areacode
    contact["phone"] = phone
    
    # Return data frame
    return(contact)
    
def GetPetPolicy(df):
    
    # Import required packages
    import pandas as pd
    
    # Initialize empty data frames. These will be binary columns that will be put into data frame as output
    DogsA = pd.DataFrame() # Dogs allowed
    CatsA = pd.DataFrame() # Cats allowed
    NoPet = pd.DataFrame() # No pets allowed
    NegPe = pd.DataFrame() # Pets are negotiable
    OtheA = pd.DataFrame() # Other (unknown) pets allowed
    BirdA = pd.DataFrame() # Birds allowed
    FishA = pd.DataFrame() # Fish allowed
    ReptA = pd.DataFrame() # Reptile allowed
    UnknP= pd.DataFrame() # Unknown if pets allowed

    
    
    for policy in df["Pet Policy"]:
        if isinstance(policy, str):
            # Dogs allowed
            if "Dogs Allowed" in policy: 
                DogsA = DogsA.append([1], ignore_index = True)
                CatsA = CatsA.append([0], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([0], ignore_index = True)
                BirdA = BirdA.append([0], ignore_index = True)
                FishA = FishA.append([0], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)

            # Cats allowed
            elif "Cats Allowed" in policy:
                DogsA = DogsA.append([0], ignore_index = True)
                CatsA = CatsA.append([1], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([0], ignore_index = True)
                BirdA = BirdA.append([0], ignore_index = True)
                FishA = FishA.append([0], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)
            
            # Dogs and cats allowed
            elif "Dogs and Cats Allowed" in policy:
                DogsA = DogsA.append([1], ignore_index = True)
                CatsA = CatsA.append([1], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([0], ignore_index = True)
                BirdA = BirdA.append([0], ignore_index = True)
                FishA = FishA.append([0], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)

            # No pets allowed
            elif "No Pets Allowed" in policy:
                DogsA = DogsA.append([0], ignore_index = True)
                CatsA = CatsA.append([0], ignore_index = True)
                NoPet = NoPet.append([1], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([0], ignore_index = True)
                BirdA = BirdA.append([0], ignore_index = True)
                FishA = FishA.append([0], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)
            
            # Pets negotiable
            elif "Pets Negotiable" in policy:
                DogsA = DogsA.append([0], ignore_index = True)
                CatsA = CatsA.append([0], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([1], ignore_index = True)
                OtheA = OtheA.append([0], ignore_index = True)
                BirdA = BirdA.append([0], ignore_index = True)
                FishA = FishA.append([0], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)
            
            # Other (unknown) pets allowed
            elif "Other Pets Allowed" in policy:
                DogsA = DogsA.append([0], ignore_index = True)
                CatsA = CatsA.append([0], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([1], ignore_index = True)
                BirdA = BirdA.append([0], ignore_index = True)
                FishA = FishA.append([0], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)
            
            #Birds allowed
            elif "Birds Allowed" in policy:
                DogsA = DogsA.append([0], ignore_index = True)
                CatsA = CatsA.append([0], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([0], ignore_index = True)
                BirdA = BirdA.append([1], ignore_index = True)
                FishA = FishA.append([0], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)

            # Birds and fish allowed
            elif "Birds and Fish Allowed" in policy:
                DogsA = DogsA.append([0], ignore_index = True)
                CatsA = CatsA.append([0], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([0], ignore_index = True)
                BirdA = BirdA.append([1], ignore_index = True)
                FishA = FishA.append([1], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)

            # Dogs, cats, and other (unknown) pets allowed
            elif "Dogs, Cats and Other Pets Allowed" in policy:
                DogsA = DogsA.append([1], ignore_index = True)
                CatsA = CatsA.append([1], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([1], ignore_index = True)
                BirdA = BirdA.append([0], ignore_index = True)
                FishA = FishA.append([0], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)

            # Dogs, cats, birds, fish, reptiles, and other (unknown) pets allowed
            elif "Dogs, Cats, Birds, Fish, Reptiles and Other Pets Allowed" in policy:
                DogsA = DogsA.append([1], ignore_index = True)
                CatsA = CatsA.append([1], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([1], ignore_index = True)
                BirdA = BirdA.append([1], ignore_index = True)
                FishA = FishA.append([1], ignore_index = True)
                ReptA = ReptA.append([1], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)

            # Cats and fish allowed
            elif "Cats and Fish Allowed" in policy:
                DogsA = DogsA.append([0], ignore_index = True)
                CatsA = CatsA.append([1], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([0], ignore_index = True)
                BirdA = BirdA.append([0], ignore_index = True)
                FishA = FishA.append([1], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)

            # Cats, birds, and fish allowed
            elif "Cats, Birds and Fish Allowed" in policy:
                DogsA = DogsA.append([0], ignore_index = True)
                CatsA = CatsA.append([1], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([0], ignore_index = True)
                BirdA = BirdA.append([1], ignore_index = True)
                FishA = FishA.append([1], ignore_index = True)
                ReptA = ReptA.append([0], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)

            # Cats, birds, fish, and reptiles allowed
            elif "Cats, Birds, Fish and Reptiles Allowed" in policy:
                DogsA = DogsA.append([0], ignore_index = True)
                CatsA = CatsA.append([1], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([0], ignore_index = True)
                BirdA = BirdA.append([1], ignore_index = True)
                FishA = FishA.append([1], ignore_index = True)
                ReptA = ReptA.append([1], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)

            # Cats, birds, fish, reptiles, and other (unknown) pets allowed
            elif "Cats, Birds, Fish, Reptiles and Other Pets Allowed" in policy:
                DogsA = DogsA.append([0], ignore_index = True)
                CatsA = CatsA.append([1], ignore_index = True)
                NoPet = NoPet.append([0], ignore_index = True)
                NegPe = NegPe.append([0], ignore_index = True)
                OtheA = OtheA.append([1], ignore_index = True)
                BirdA = BirdA.append([1], ignore_index = True)
                FishA = FishA.append([1], ignore_index = True)
                ReptA = ReptA.append([1], ignore_index = True)
                UnknP = UnknP.append([0], ignore_index = True)

        # Otherwise we do not know if the property allows pets or not
        else:
            DogsA = DogsA.append([0], ignore_index = True)
            CatsA = CatsA.append([0], ignore_index = True)
            NoPet = NoPet.append([0], ignore_index = True)
            NegPe = NegPe.append([0], ignore_index = True)
            OtheA = OtheA.append([0], ignore_index = True)
            BirdA = BirdA.append([0], ignore_index = True)
            FishA = FishA.append([0], ignore_index = True)
            ReptA = ReptA.append([0], ignore_index = True)
            UnknP = UnknP.append([1], ignore_index = True)

    # Get length of data frame            
    L = len(df)        
    outputDF = pd.DataFrame() # Initialize empty data frame to be output
    
    # Place data into output data frame
    outputDF["pid"] = range(0, L)
    outputDF["dogsallowed"] = DogsA[0]
    outputDF["catsallowed"] = CatsA[0] 
    outputDF["nopets"] = NoPet[0] 
    outputDF["petsnegotiable"] = NegPe[0] 
    outputDF["otherpetsallowed"] = OtheA[0] 
    outputDF["birdsallowed"] = BirdA[0]
    outputDF["fishallowed"] = FishA[0] 
    outputDF["reptileallowed"] = ReptA[0] 
    outputDF["unknownpets"] = UnknP[0]
    
    # Return data frame
    return(outputDF)

def GetParkingPolicy(df):
    
    # Import required packages
    import pandas as pd
    
    # Initialize empty data frames. These will be binary columns that will be put into data frame as output
    CovPark = pd.DataFrame() # Covered parking
    GarPark = pd.DataFrame() # Garage parking
    LotPark = pd.DataFrame() # Lot parking
    StrPark = pd.DataFrame() # Street parking
    OthPark = pd.DataFrame() # Other parking

    for parking in df["Parking"]:
        if isinstance(parking, str):
            
            # Property has lot and covered parking
            if "Surface Lot and Covered" in parking:
                CovPark = CovPark.append([1], ignore_index = True)
                GarPark = GarPark.append([0], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([0], ignore_index = True)

            # Property has lot and covered parking
            elif "Surface Lot and Garage" in parking:
                CovPark = CovPark.append([0], ignore_index = True)
                GarPark = GarPark.append([1], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([0], ignore_index = True)

            # Property has lot and other (unknown) parking
            elif "Surface Lot and Other" in parking:
                CovPark = CovPark.append([0], ignore_index = True)
                GarPark = GarPark.append([0], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([1], ignore_index = True)

            # Property has lot and street parking
            elif "Surface Lot and Street" in parking:
                CovPark = CovPark.append([0], ignore_index = True)
                GarPark = GarPark.append([0], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StrPark = StrPark.append([1], ignore_index = True)
                OthPark = OthPark.append([0], ignore_index = True)

            # Property has lot and covered parking
            elif "Surface Lot, Covered and Garage" in parking:
                CovPark = CovPark.append([1], ignore_index = True)
                GarPark = GarPark.append([1], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([0], ignore_index = True)

            # Property has lot, covered, and other (unknown) parking
            elif "Surface Lot, Covered and Other" in parking:
                CovPark = CovPark.append([1], ignore_index = True)
                GarPark = GarPark.append([0], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([1], ignore_index = True)

            # Property has lot, covered, and other (unknown) parking
            elif "Surface Lot, Covered, Garage and Other" in parking:
                CovPark = CovPark.append([1], ignore_index = True)
                GarPark = GarPark.append([1], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([1], ignore_index = True)

            # Property has lot, covered, and other (unknown) parking
            elif "Surface Lot, Garage and Other" in parking:
                CovPark = CovPark.append([0], ignore_index = True)
                GarPark = GarPark.append([1], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([1], ignore_index = True)
                
            # Property has covered parking
            elif "Covered" in parking:
                CovPark = CovPark.append([1], ignore_index = True)
                GarPark = GarPark.append([0], ignore_index = True)
                LotPark = LotPark.append([0], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([0], ignore_index = True)

            # Property has covered parking
            elif "Garage" in parking:
                CovPark = CovPark.append([0], ignore_index = True)
                GarPark = GarPark.append([1], ignore_index = True)
                LotPark = LotPark.append([0], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([0], ignore_index = True)

            # Property has street parking
            elif "Street" in parking:
                CovPark = CovPark.append([0], ignore_index = True)
                GarPark = GarPark.append([0], ignore_index = True)
                LotPark = LotPark.append([0], ignore_index = True)
                StrPark = StrPark.append([1], ignore_index = True)
                OthPark = OthPark.append([0], ignore_index = True)

            # Property has other (unknown) parking
            elif "Other" in parking:
                CovPark = CovPark.append([0], ignore_index = True)
                GarPark = GarPark.append([0], ignore_index = True)
                LotPark = LotPark.append([0], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([1], ignore_index = True)

            # Property has lot parking
            elif "Surface Lot" in parking:
                CovPark = CovPark.append([0], ignore_index = True)
                GarPark = GarPark.append([0], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StrPark = StrPark.append([0], ignore_index = True)
                OthPark = OthPark.append([0], ignore_index = True)
        
        # Otherwise we have no information on the parking at the property
        else:
            CovPark = CovPark.append([0], ignore_index = True)
            GarPark = GarPark.append([0], ignore_index = True)
            LotPark = LotPark.append([0], ignore_index = True)
            StrPark = StrPark.append([0], ignore_index = True)
            OthPark = OthPark.append([1], ignore_index = True)
    
    # Get length of data frame            
    L = len(df)        
    outputDF = pd.DataFrame() # Initialize empty data frame as output

    # Place data into output data frame
    outputDF["pid"] = range(0, L)
    outputDF["covpark"] = CovPark[0]
    outputDF["garpark"] = GarPark[0]
    outputDF["lotpark"] = LotPark[0]
    outputDF["stpark"] = StrPark[0]
    outputDF["unkpark"] = OthPark[0]
    
    # Return data frame
    return(outputDF)
    
def GetFeatures(df, column):
# Used to get the following columns in the scraped data:
#    1. Features
#    2. Gym
#    3. Kitchen
#    4. Amenities
#    5. Living Space
#    6. Services
#    7. Property Info
#    8. Indoor Info
#    9. Outdoor Info
    
    # Import required packages
    import pandas as pd
    
    # Initialize empty data frame to store each unique features
    columnDF = pd.DataFrame()
    # Initialize empty data frame to store the unique property ID
    pid = pd.DataFrame()
    i = 0 # Use to keep track of the propert ID

    # Loop through each element of the specified column of the data frame
    for elements in df[column]:
        if isinstance(elements, str): # If the element is a string we perform the operations below
            splitElement = elements.split("* ") # Split string in cell based on an asterisk
            collectFeature = [] # Initialize empty data frame to store each unique feature of the property
            for feature in splitElement[1:]: # For each unique feature we will store it in the collectFeature list
                collectFeature.append(feature.strip().replace("\n", "")) # Append each unique feature in collectFeature list after stripping it of unnecessary blank space and removing unnecessary text
            columnDF = columnDF.append(collectFeature, ignore_index = True) # Place all the property's features into data frame
            pid = pid.append([i]*len(collectFeature), ignore_index = True) # Use to keep track of the property that is associated with the features we just collected
            i+=1 # Increase i by one (i.e. move to next property)
        else: # Else the element is not a string and is just an empty cell. We don't know anything about this element
            columnDF = columnDF.append(["NA"], ignore_index = True) # If we know of no features, append NA to data frame
            pid = pid.append([i], ignore_index = True) # Keep track of the property we're on
            i+=1 # Increase i by one (i.e. move to next property)
            
    # Initialize empty data frame as output
    outputDF = pd.DataFrame()
    
    # Place data into output data frame
    outputDF["pid"] = pid[0]
    outputDF["feature"] = columnDF[0]
    outputDF["value"] = [1]*len(outputDF)
    
    if column == "Features":
        outputDF.loc[outputDF["feature"] == "NA",  "feature"] = "na"
        outputDF.loc[outputDF["feature"] == "Washer/Dryer",  "feature"] = "washdry"
        outputDF.loc[outputDF["feature"] == "Air Conditioning",  "feature"] = "ac"
        outputDF.loc[outputDF["feature"] == "Ceiling Fans",  "feature"] = "ceilfans"
        outputDF.loc[outputDF["feature"] == "Cable Ready",  "feature"] = "cableready"
        outputDF.loc[outputDF["feature"] == "Fireplace",  "feature"] = "fireplace"
        outputDF.loc[outputDF["feature"] == "Alarm",  "feature"] = "alarm"
        outputDF.loc[outputDF["feature"] == "Storage Units",  "feature"] = "storage"
        outputDF.loc[outputDF["feature"] == "High Speed Internet Access",  "feature"] = "hsinternet"
        outputDF.loc[outputDF["feature"] == "Wi-Fi",  "feature"] = "wifi"
        outputDF.loc[outputDF["feature"] == "Heating",  "feature"] = "heating"
        outputDF.loc[outputDF["feature"] == "Tub/Shower",  "feature"] = "tubshower"
        outputDF.loc[outputDF["feature"] == "Sprinkler System",  "feature"] = "sprinklers"
        outputDF.loc[outputDF["feature"] == "Smoke Free",  "feature"] = "smokefree"
        outputDF.loc[outputDF["feature"] == "Satellite TV",  "feature"] = "sattv"
        outputDF.loc[outputDF["feature"] == "Wheelchair Accessible (Rooms)",  "feature"] = "wheelchacc"
        outputDF.loc[outputDF["feature"] == "Handrails",  "feature"] = "handrail"
        outputDF.loc[outputDF["feature"] == "Framed Mirrors",  "feature"] = "framedmirror"
        outputDF.loc[outputDF["feature"] == "Trash Compactor",  "feature"] = "trashcompact"
        outputDF.loc[outputDF["feature"] == "Washer/Dryer Hookup",  "feature"] = "washdryhookup"
        outputDF.loc[outputDF["feature"] == "Intercom",  "feature"] = "intercom"
        outputDF.loc[outputDF["feature"] == "Double Vanities",  "feature"] = "doublevanities"
        outputDF.loc[outputDF["feature"] == "Vacuum System",  "feature"] = "vacuumsys"
        outputDF.loc[outputDF["feature"] == "Surround Sound",  "feature"] = "ssound"
    elif column == "Gym":
        outputDF.loc[outputDF["feature"] == "NA",  "feature"] = "na"
        outputDF.loc[outputDF["feature"] == "Fitness Center",  "feature"] = "fitcenter"
        outputDF.loc[outputDF["feature"] == "Sauna",  "feature"] = "sauna"
        outputDF.loc[outputDF["feature"] == "Spa",  "feature"] = "spa"
        outputDF.loc[outputDF["feature"] == "Pool",  "feature"] = "pool"
        outputDF.loc[outputDF["feature"] == "Playground",  "feature"] = "playground"
        outputDF.loc[outputDF["feature"] == "Basketball Court",  "feature"] = "bballct"
        outputDF.loc[outputDF["feature"] == "Racquetball Court",  "feature"] = "rballct"
        outputDF.loc[outputDF["feature"] == "Tennis Court",  "feature"] = "tennisct"        
        outputDF.loc[outputDF["feature"] == "Cardio Machines",  "feature"] = "cardiomach"
        outputDF.loc[outputDF["feature"] == "Free Weights",  "feature"] = "freewghts"
        outputDF.loc[outputDF["feature"] == "Weight Machines",  "feature"] = "wghtmach"
        outputDF.loc[outputDF["feature"] == "Bike Storage",  "feature"] = "bikestore"
        outputDF.loc[outputDF["feature"] == "Gameroom",  "feature"] = "gameroom"
        outputDF.loc[outputDF["feature"] == "Fitness Programs",  "feature"] = "fitprog"
        outputDF.loc[outputDF["feature"] == "Volleyball Court",  "feature"] = "vballct"
        outputDF.loc[outputDF["feature"] == "Gaming Stations",  "feature"] = "gamestation"
        outputDF.loc[outputDF["feature"] == "Media Center/Movie Theatre",  "feature"] = "mediacenter"
        outputDF.loc[outputDF["feature"] == "Walking/Biking Trails",  "feature"] = "trails"
        outputDF.loc[outputDF["feature"] == "Health Club Facility",  "feature"] = "healthclub"
        outputDF.loc[outputDF["feature"] == "Putting Greens",  "feature"] = "putgreen"
        outputDF.loc[outputDF["feature"] == "Sport Court",  "feature"] = "sportct"
    elif column == "Kitchen":
        outputDF.loc[outputDF["feature"] == "NA",  "feature"] = "na"
        outputDF.loc[outputDF["feature"] == "Dishwasher",  "feature"] = "dwasher"
        outputDF.loc[outputDF["feature"] == "Disposal",  "feature"] = "disposal"
        outputDF.loc[outputDF["feature"] == "Granite Countertops",  "feature"] = "granctops"
        outputDF.loc[outputDF["feature"] == "Stainless Steel Appliances",  "feature"] = "ssteelapp"
        outputDF.loc[outputDF["feature"] == "Kitchen",  "feature"] = "kitchen"
        outputDF.loc[outputDF["feature"] == "Microwave",  "feature"] = "microwave"
        outputDF.loc[outputDF["feature"] == "Refrigerator",  "feature"] = "fridge"        
        outputDF.loc[outputDF["feature"] == "Ice Maker",  "feature"] = "icemaker"
        outputDF.loc[outputDF["feature"] == "Range",  "feature"] = "range"
        outputDF.loc[outputDF["feature"] == "Island Kitchen",  "feature"] = "islandkitch"
        outputDF.loc[outputDF["feature"] == "Pantry",  "feature"] = "pantry"
        outputDF.loc[outputDF["feature"] == "Oven",  "feature"] = "oven"
        outputDF.loc[outputDF["feature"] == "Freezer",  "feature"] = "freezer"
        outputDF.loc[outputDF["feature"] == "Warming Drawer",  "feature"] = "warmdrawer"
        outputDF.loc[outputDF["feature"] == "Eat-in Kitchen",  "feature"] = "eatinkitch"
        outputDF.loc[outputDF["feature"] == "Instant Hot Water",  "feature"] = "insthotwater"
        outputDF.loc[outputDF["feature"] == "Coffee System",  "feature"] = "coffeesys"
        outputDF.loc[outputDF["feature"] == "Breakfast Nook",  "feature"] = "breaknook"
    elif column == "Living Space":
        outputDF.loc[outputDF["feature"] == "Walk-In Closets",  "feature"] = "walkincloset"
        outputDF.loc[outputDF["feature"] == "NA",  "feature"] = "na"
        outputDF.loc[outputDF["feature"] == "Hardwood Floors",  "feature"] = "hwoodfloor"
        outputDF.loc[outputDF["feature"] == "Carpet",  "feature"] = "carpet"
        outputDF.loc[outputDF["feature"] == "Bay Window",  "feature"] = "baywindow"
        outputDF.loc[outputDF["feature"] == "Views",  "feature"] = "views"
        outputDF.loc[outputDF["feature"] == "Window Coverings",  "feature"] = "windowcov"
        outputDF.loc[outputDF["feature"] == "Tile Floors",  "feature"] = "tilefloor"        
        outputDF.loc[outputDF["feature"] == "Linen Closet",  "feature"] = "linencloset"
        outputDF.loc[outputDF["feature"] == "Vaulted Ceiling",  "feature"] = "vceil"
        outputDF.loc[outputDF["feature"] == "Vinyl Flooring",  "feature"] = "vfloor"
        outputDF.loc[outputDF["feature"] == "Dining Room",  "feature"] = "diningrm"
        outputDF.loc[outputDF["feature"] == "Den",  "feature"] = "den"
        outputDF.loc[outputDF["feature"] == "Sunroom",  "feature"] = "sunrm"
        outputDF.loc[outputDF["feature"] == "Loft Layout",  "feature"] = "loft"
        outputDF.loc[outputDF["feature"] == "Accent Walls",  "feature"] = "accentwalls"
        outputDF.loc[outputDF["feature"] == "Skylight",  "feature"] = "skylight"
        outputDF.loc[outputDF["feature"] == "Furnished",  "feature"] = "furnished"
        outputDF.loc[outputDF["feature"] == "Office",  "feature"] = "office"
        outputDF.loc[outputDF["feature"] == "Crown Molding",  "feature"] = "crownmold"
        outputDF.loc[outputDF["feature"] == "Double Pane Windows",  "feature"] = "doublepw"
        outputDF.loc[outputDF["feature"] == "Basement",  "feature"] = "basement"
        outputDF.loc[outputDF["feature"] == "Built-In Bookshelves",  "feature"] = "bshelves"
        outputDF.loc[outputDF["feature"] == "Attic",  "feature"] = "attic"
        outputDF.loc[outputDF["feature"] == "Wet Bar",  "feature"] = "wetbar"
        outputDF.loc[outputDF["feature"] == "Family Room",  "feature"] = "famrm"
        outputDF.loc[outputDF["feature"] == "Recreation Room",  "feature"] = "recrm"
        outputDF.loc[outputDF["feature"] == "Mother-in-law Unit",  "feature"] = "mothlawunit"
        outputDF.loc[outputDF["feature"] == "Mud Room",  "feature"] = "mudrm"
    elif column == "Services":
        outputDF.loc[outputDF["feature"] == "NA",  "feature"] = "na"
        outputDF.loc[outputDF["feature"] == "Package Service",  "feature"] = "packserv"
        outputDF.loc[outputDF["feature"] == "Maintenance on site",  "feature"] = "onsitemaint"
        outputDF.loc[outputDF["feature"] == "Concierge",  "feature"] = "concierge"
        outputDF.loc[outputDF["feature"] == "24 Hour Availability",  "feature"] = "avail24hr"
        outputDF.loc[outputDF["feature"] == "Recycling",  "feature"] = "recycling"
        outputDF.loc[outputDF["feature"] == "Renters Insurance Program",  "feature"] = "rentins"
        outputDF.loc[outputDF["feature"] == "Dry Cleaning Service",  "feature"] = "dryclean"        
        outputDF.loc[outputDF["feature"] == "Online Services",  "feature"] = "onlineserv"
        outputDF.loc[outputDF["feature"] == "Pet Play Area",  "feature"] = "petplay"
        outputDF.loc[outputDF["feature"] == "Pet Care",  "feature"] = "petcare"
        outputDF.loc[outputDF["feature"] == "Controlled Access",  "feature"] = "accesscontr"
        outputDF.loc[outputDF["feature"] == "On-Site ATM",  "feature"] = "atm"
        outputDF.loc[outputDF["feature"] == "Laundry Facilities",  "feature"] = "laundry"
        outputDF.loc[outputDF["feature"] == "Community-Wide WiFi",  "feature"] = "commwifi"
        outputDF.loc[outputDF["feature"] == "Bilingual",  "feature"] = "bilingual"
        outputDF.loc[outputDF["feature"] == "Courtesy Patrol",  "feature"] = "patrol"
        outputDF.loc[outputDF["feature"] == "Guest Apartment",  "feature"] = "guestapt"
        outputDF.loc[outputDF["feature"] == "Car Wash Area",  "feature"] = "carwash"
        outputDF.loc[outputDF["feature"] == "Energy Star Certified",  "feature"] = "energystar"
        outputDF.loc[outputDF["feature"] == "Pet Washing Station",  "feature"] = "petwash"
        outputDF.loc[outputDF["feature"] == "Car Charging Station",  "feature"] = "carcharge"
        outputDF.loc[outputDF["feature"] == "Property Manager on Site",  "feature"] = "onsitepropman"
        outputDF.loc[outputDF["feature"] == "Furnished Units Available",  "feature"] = "furnishavail"
        outputDF.loc[outputDF["feature"] == "Wi-Fi at Pool and Clubhouse",  "feature"] = "clubpoolwifi"
        outputDF.loc[outputDF["feature"] == "Trash Pickup - Door to Door",  "feature"] = "ddtrash"
        outputDF.loc[outputDF["feature"] == "Planned Social Activities",  "feature"] = "social"
        outputDF.loc[outputDF["feature"] == "Laundry Service",  "feature"] = "laundryservice"
        outputDF.loc[outputDF["feature"] == "Shuttle to Train",  "feature"] = "shuttle"
        outputDF.loc[outputDF["feature"] == "Health Club Discount",  "feature"] = "hclubdisc"
        outputDF.loc[outputDF["feature"] == "LEED Rating",  "feature"] = "leedrt"
        outputDF.loc[outputDF["feature"] == "On-Site Retail",  "feature"] = "onsiteretail"
        outputDF.loc[outputDF["feature"] == "Grocery Service",  "feature"] = "groceryserv"
        outputDF.loc[outputDF["feature"] == "Maid Service",  "feature"] = "maidserv"
        outputDF.loc[outputDF["feature"] == "Meal Service",  "feature"] = "mealserv"
        outputDF.loc[outputDF["feature"] == "Day Care",  "feature"] = "daycare"
        outputDF.loc[outputDF["feature"] == "Security System",  "feature"] = "securitysys"
        outputDF.loc[outputDF["feature"] == "House Sitter Services",  "feature"] = "housesitserv"
        outputDF.loc[outputDF["feature"] == "Video Patrol",  "feature"] = "videopatrol"
        outputDF.loc[outputDF["feature"] == "Local Vet / Pet Store Discount",  "feature"] = "petstoredisc"
        outputDF.loc[outputDF["feature"] == "Parking Security",  "feature"] = "parksec"
        outputDF.loc[outputDF["feature"] == "Doorman",  "feature"] = "doorman"
        outputDF.loc[outputDF["feature"] == "Trash Pickup - Curbside",  "feature"] = "cstrash"
        outputDF.loc[outputDF["feature"] == "Composting",  "feature"] = "compost"
        outputDF.loc[outputDF["feature"] == "Hearing Impaired Accessible",  "feature"] = "hearimpacc"
        outputDF.loc[outputDF["feature"] == "Vision Impaired Accessible",  "feature"] = "visimpacc"
        outputDF.loc[outputDF["feature"] == "Per Diem Accepted",  "feature"] = "perdiem"
    elif column == "Indoor Info":
        outputDF.loc[outputDF["feature"] == "Business Center",  "feature"] = "businesscent"
        outputDF.loc[outputDF["feature"] == "Storage Space",  "feature"] = "storagespace"
        outputDF.loc[outputDF["feature"] == "NA",  "feature"] = "na"
        outputDF.loc[outputDF["feature"] == "Clubhouse",  "feature"] = "clubhouse"
        outputDF.loc[outputDF["feature"] == "Elevator",  "feature"] = "elevator"
        outputDF.loc[outputDF["feature"] == "Lounge",  "feature"] = "lounge"
        outputDF.loc[outputDF["feature"] == "Conference Room",  "feature"] = "confrm"
        outputDF.loc[outputDF["feature"] == "Coffee Bar",  "feature"] = "coffeebar"        
        outputDF.loc[outputDF["feature"] == "Multi Use Room",  "feature"] = "multiuserm"
        outputDF.loc[outputDF["feature"] == "Disposal Chutes",  "feature"] = "dispchutes"
        outputDF.loc[outputDF["feature"] == "Library",  "feature"] = "library"
        outputDF.loc[outputDF["feature"] == "Corporate Suites",  "feature"] = "corpsuite"
        outputDF.loc[outputDF["feature"] == "Breakfast/Coffee Concierge",  "feature"] = "bcconcierge"
        outputDF.loc[outputDF["feature"] == "Two Story Lobby",  "feature"] = "twostorylobby"
        outputDF.loc[outputDF["feature"] == "Vintage Building",  "feature"] = "vintage"
        outputDF.loc[outputDF["feature"] == "Tanning Salon",  "feature"] = "tanningsal"
    elif column == "Outdoor Info":
        outputDF.loc[outputDF["feature"] == "Gated",  "feature"] = "gated"
        outputDF.loc[outputDF["feature"] == "NA",  "feature"] = "na"
        outputDF.loc[outputDF["feature"] == "Boat Docks",  "feature"] = "boatdock"
        outputDF.loc[outputDF["feature"] == "Cabana",  "feature"] = "cabana"
        outputDF.loc[outputDF["feature"] == "Sundeck",  "feature"] = "sundeck"
        outputDF.loc[outputDF["feature"] == "Balcony",  "feature"] = "balcony"
        outputDF.loc[outputDF["feature"] == "Lake Access",  "feature"] = "lake"
        outputDF.loc[outputDF["feature"] == "Courtyard",  "feature"] = "ctyard"
        outputDF.loc[outputDF["feature"] == "Grill",  "feature"] = "grill"
        outputDF.loc[outputDF["feature"] == "Patio",  "feature"] = "patio"        
        outputDF.loc[outputDF["feature"] == "Picnic Area",  "feature"] = "picnicarea"
        outputDF.loc[outputDF["feature"] == "Rooftop Lounge",  "feature"] = "rooflounge"
        outputDF.loc[outputDF["feature"] == "Waterfront",  "feature"] = "waterfront"
        outputDF.loc[outputDF["feature"] == "Zen Garden",  "feature"] = "zengarden"
        outputDF.loc[outputDF["feature"] == "Fenced Lot",  "feature"] = "fencedlot"
        outputDF.loc[outputDF["feature"] == "Yard",  "feature"] = "yard"
        outputDF.loc[outputDF["feature"] == "Lawn",  "feature"] = "lawn"
        outputDF.loc[outputDF["feature"] == "Garden",  "feature"] = "garden"
        outputDF.loc[outputDF["feature"] == "Porch",  "feature"] = "porch"
        outputDF.loc[outputDF["feature"] == "Deck",  "feature"] = "deck"
        outputDF.loc[outputDF["feature"] == "Barbecue Area",  "feature"] = "bbqarea"
        outputDF.loc[outputDF["feature"] == "Barbecue/Grill",  "feature"] = "bbq"
        outputDF.loc[outputDF["feature"] == "Pond",  "feature"] = "pond"
    
    if column != "Amenities":
        outputDF = outputDF.pivot(index = "pid", columns = "feature", values = "value").fillna(value = 0)
        outputDF.insert(loc = 0, column = "pid", value = range(0, len(df)))

    
    # Return data frame
    return(outputDF)
    
def GetFees(df, column):
# Used to get the following columns in the scraped data:
#   1. Monthly Fees
#   2. One time fees
    
    # Import required packages
    import pandas as pd
    import math
    
    # Initialize empty data frame to store fees and the property IDs
    feesDF = pd.DataFrame()
    PropertyID = pd.DataFrame()
    
    i = 0
    for fees in df[column]: # For each element of the monthly fees column
        if isinstance(fees, str): # Check if element is a string
            tempFees = fees.split("* ") # Split fees by asterisk
            feesDF = feesDF.append(tempFees[1:], ignore_index = True) # Append fees to data frame
            PropertyID = PropertyID.append([i]*len(tempFees[1:]), ignore_index = True) # Keep track of property IDs
            i+=1 # Move to next property
        else: # Else we encountering something that is not a string
            feesDF = feesDF.append(["NA"], ignore_index = True) # Append NA since we know nothing about the monthly fees
            PropertyID = PropertyID.append([i], ignore_index = True) # Keep track of property ID
            i+=1 # Move to next property
            
    # Initialize empty data frame
    feesDF2 = pd.DataFrame()
    
    # Place data into data frame 
    feesDF2["MFees"] = feesDF[0]
    feesDF2["PropertyID"] = PropertyID[0]
    
    # Initialize empty data frames to store the monthly fee and the description of what the fee is
    Description = pd.DataFrame()
    Cost = pd.DataFrame()
    
    for fees in feesDF2["MFees"]: # For each element of the monthly fees column
        tempFees = fees.strip().split(":") # Split by colon
        if len(tempFees) == 1: # If length of split element is 1
            Description = Description.append(tempFees, ignore_index = True) # Append description of fee to description data frame
            Cost = Cost.append(tempFees, ignore_index = True) # Append monthly fee to cost data frame
        else: # Else length of split element is more than one
            Description = Description.append([tempFees[0]], ignore_index = True) # Append description of fee to description data frame
            Cost = Cost.append([tempFees[1]], ignore_index = True) # Append monthly fee to cost data frame

    # Initialize empty data frame and store data in it
    feesDF3 = pd.DataFrame()
    feesDF3["Desc"] = Description[0]
    feesDF3["Cost"] = Cost[0]

    i = 0
    Split = pd.DataFrame() # Initialize empty data frame to store split text
    PropertyID2 = pd.DataFrame() # Initialize empty data frame to store property IDs
    MinCost = pd.DataFrame() # Initialize empty data frame to store minimum cost when cost is a range
    MaxCost = pd.DataFrame() # Initialize empty data frame to store maximum cost when cost is a range
    
    for desc in feesDF3["Desc"]: # For each description in the description column
        temp = desc.split(",") # Split it by a comma 
        Split = Split.append(temp, ignore_index = True) # Append split text to split data frame
        if len(temp) == 1: # If length of split text is 1 
            PropertyID2 = PropertyID2.append([feesDF2.PropertyID[i]], ignore_index = True) # Append property ID to data frame
        else: # Else length of split text is more than 1
            PropertyID2 = PropertyID2.append([feesDF2.PropertyID[i]]*len(temp), ignore_index = True) # Append property ID to data frame
        tempCost = feesDF3["Cost"][i].replace("$", "") # In Cost column, remove dollar sign
        tempCost = tempCost.replace(",", "") # Remove any commas
        tempCost = tempCost.replace("\n", "") # Remove \n
        tempCost = tempCost.split(" - ") # Split by dash 
        if len(tempCost) == 2: # If length of split cost is 2 that means we have a range for the monthly fee
            MinCost = MinCost.append([int(tempCost[0])], ignore_index = True) # Append to min cost data frame
            MaxCost = MaxCost.append([int(tempCost[1])], ignore_index = True) # Append to max cost data frame
        elif "Included" in tempCost[0]: # If Included is in the cell then the monthly fee is included and thus 0
            MinCost = MinCost.append([0]*len(temp), ignore_index = True) # Append 0 to min cost data frame
            MaxCost = MaxCost.append([0]*len(temp), ignore_index = True) # Append 0 to max cost data frame
        elif "NA" == tempCost[0]: # If NA in data frame
            MinCost = MinCost.append([math.nan], ignore_index = True) # Append nan to min cost data frame
            MaxCost = MaxCost.append([math.nan], ignore_index = True) # Append nan to max cost data frame
        else: # Else the length of the cell is 1
            MinCost = MinCost.append([int(tempCost[0])], ignore_index = True) # Append fee to min cost data frame
            MaxCost = MaxCost.append([int(tempCost[0])], ignore_index = True) # Append fee to max cost data frame
        i+=1 # Move on to next property
    
    Split = pd.DataFrame(Split[0].apply(lambda x: x.strip())) # Split element of unnecessary white space
    
    # Initialize empty data frame to be output
    outputDF = pd.DataFrame()
    
    # Put data into data frame for output
    outputDF["pid"] = PropertyID2[0]
    outputDF["desc"] = Split[0]
    outputDF["mincost"] = MinCost[0]
    outputDF["maxcost"] = MaxCost[0]
    
    if column == "One Time Fees":
        outputDF.loc[outputDF["desc"] == "Cat Deposit",  "desc"] = "dogdep"
        outputDF.loc[outputDF["desc"] == "Dog Deposit",  "desc"] = "catdep"
        outputDF.loc[outputDF["desc"] == "Other",  "desc"] = "unknown"
        outputDF.loc[outputDF["desc"] == "Other Deposit",  "desc"] = "otherdep"
        outputDF.loc[outputDF["desc"] == "Bird Deposit",  "desc"] = "birddep"
        outputDF.loc[outputDF["desc"] == "Fish Deposit",  "desc"] = "fishdep"
        outputDF.loc[outputDF["desc"] == "Reptile Deposit",  "desc"] = "reptiledep"
        outputDF.loc[outputDF["desc"] == "Admin Fee",  "desc"] = "admin"
        outputDF.loc[outputDF["desc"] == "Amenity Fee",  "desc"] = "amenity"
        outputDF.loc[outputDF["desc"] == "Application Fee",  "desc"] = "appfee"
        outputDF.loc[outputDF["desc"] == "Bird Fee",  "desc"] = "birdfee"
        outputDF.loc[outputDF["desc"] == "Cat Fee",  "desc"] = "catfee"
        outputDF.loc[outputDF["desc"] == "Dog Fee",  "desc"] = "dogfee"
        outputDF.loc[outputDF["desc"] == "Fish Fee",  "desc"] = "fishfee"
        outputDF.loc[outputDF["desc"] == "Move-In Fee",  "desc"] = "movein"
        outputDF.loc[outputDF["desc"] == "NA",  "desc"] = "na"
        outputDF.loc[outputDF["desc"] == "Reptile Fee",  "desc"] = "reptilefee"
    else:
        outputDF.loc[outputDF["desc"] == "Unassigned Surface Lot Parking",  "desc"] = "unlotpark"
        outputDF.loc[outputDF["desc"] == "Assigned Covered Parking",  "desc"] = "ascovpark"
        outputDF.loc[outputDF["desc"] == "Assigned Street Parking",  "desc"] = "asstpark"
        outputDF.loc[outputDF["desc"] == "Trash Removal",  "desc"] = "trashrem"
        outputDF.loc[outputDF["desc"] == "Sewer",  "desc"] = "sewer"
        outputDF.loc[outputDF["desc"] == "Assigned Surface Lot Parking",  "desc"] = "aslotpark"
        outputDF.loc[outputDF["desc"] == "Gas",  "desc"] = "gas"
        outputDF.loc[outputDF["desc"] == "Water",  "desc"] = "water"
        outputDF.loc[outputDF["desc"] == "Unassigned Garage Parking",  "desc"] = "ungarpark"        
        outputDF.loc[outputDF["desc"] == "Assigned Other Parking",  "desc"] = "asotherpark"
        outputDF.loc[outputDF["desc"] == "Unassigned Covered Parking",  "desc"] = "uncovpark"
        outputDF.loc[outputDF["desc"] == "Electricity",  "desc"] = "elect"
        outputDF.loc[outputDF["desc"] == "Heat",  "desc"] = "heat"
        outputDF.loc[outputDF["desc"] == "Air Conditioning",  "desc"] = "ac"
        outputDF.loc[outputDF["desc"] == "Assigned Garage Parking",  "desc"] = "asgarpark"
        outputDF.loc[outputDF["desc"] == "Unassigned Other Parking",  "desc"] = "unotherpark"
        outputDF.loc[outputDF["desc"] == "Cable",  "desc"] = "cable"
        outputDF.loc[outputDF["desc"] == "Bird Rent",  "desc"] = "bird"
        outputDF.loc[outputDF["desc"] == "Fish Rent",  "desc"] = "fish"
        outputDF.loc[outputDF["desc"] == "Reptile Rent",  "desc"] = "reptile"
        outputDF.loc[outputDF["desc"] == "Other Rent",  "desc"] = "otherfee"
        outputDF.loc[outputDF["desc"] == "Unassigned Street Parking",  "desc"] = "unstpark"
        outputDF.loc[outputDF["desc"] == "Dog Rent",  "desc"] = "cat"
        outputDF.loc[outputDF["desc"] == "Cat Rent",  "desc"] = "dog"
        outputDF.loc[outputDF["desc"] == "Storage Fee",  "desc"] = "storage"
        outputDF.loc[outputDF["desc"] == "NA",  "desc"] = "na"

    # Pivot table for minimum cost and pivote table for maximum cost
    output_mincostDF = outputDF.pivot(index = "pid", columns = "desc", values = "mincost")
    output_maxcostDF = outputDF.pivot(index = "pid", columns = "desc", values = "maxcost")
    
    # Insert Property ID column in each table
    output_mincostDF.insert(loc = 0, column = "pid", value = range(0, len(df)))
    output_maxcostDF.insert(loc = 0, column = "pid", value = range(0, len(df)))

        
    # Return data frames
    return(output_mincostDF, output_maxcostDF)
    
def GetLookupTables(boolean):
    
    if boolean == True:
        # Features
        featureslu = {"NA":"na",
                  "Washer/Dryer":"washdry",
                  "Air Conditioning":"ac",
                  "Ceiling Fans":"ceilfans",
                  "Cable Ready":"cableready",
                  "Fireplace":"fireplace",
                  "Alarm":"alarm",
                  "Storage Units":"storage",
                  "High Speed Internet Access":"hsinternet",
                  "Wi-Fi":"wifi",
                  "Heating":"heating",
                  "Tub/Shower":"tubshower",
                  "Sprinkler System":"sprinklers",
                  "Smoke Free":"smokefree",
                  "Satellite TV":"sattv",
                  "Wheelchair Accessible (Rooms)":"wheelchacc",
                  "Handrails":"handrail",
                  "Framed Mirrors":"framedmirror",
                  "Trash Compactor":"trashcompact",
                  "Washer/Dryer Hookup":"washdryhookup",
                  "Intercom":"intercom",
                  "Double Vanities":"doublevanities",
                  "Vacuum System":"vacuumsys",
                  "Surround Sound":"ssound"}
        featureslu = pd.DataFrame.from_dict(featureslu, orient = "index")
        featureslu.insert(loc = 0, column = "desc", value = featureslu.index)
        featureslu.rename(columns = {0:"column"}, inplace = True)
        featureslu.reset_index(inplace = True, drop = True)
        # Gym
        gymlu = {"Fitness Center":"fitcenter",
                 "NA":"na",
                 "Sauna":"sauna",
                 "Spa":"spa",
                 "Pool":"pool",
                 "Playground":"playground",
                 "Basketball Court":"bballct",
                 "Racquetball Court":"rballct",
                 "Tennis Court":"tennisct",        
                 "Cardio Machines":"cardiomach",
                 "Free Weights":"freewghts",
                 "Weight Machines":"wghtmach",
                 "Bike Storage":"bikestore",
                 "Gameroom":"gameroom",
                 "Fitness Programs":"fitprog",
                 "Volleyball Court":"vballct",
                 "Gaming Stations":"gamestation",
                 "Media Center/Movie Theatre":"mediacenter",
                 "Walking/Biking Trails":"trails",
                 "Health Club Facility":"healthclub",
                 "Putting Greens":"putgreen",
                 "Sport Court":"sportct"}
        gymlu = pd.DataFrame.from_dict(gymlu, orient = "index")
        gymlu.insert(loc = 0, column = "desc", value = gymlu.index)
        gymlu.rename(columns = {0:"column"}, inplace = True)
        gymlu.reset_index(inplace = True, drop = True)
        #Kitchen
        kitchenlu = {"NA":"na",
                     "Dishwasher":"dwasher",
                     "Disposal":"disposal",
                     "Granite Countertops":"granctops",
                     "Stainless Steel Appliances":"ssteelapp",
                     "Kitchen":"kitchen",
                     "Microwave":"microwave",
                     "Refrigerator":"fridge",        
                     "Ice Maker":"icemaker",
                     "Range":"range",
                     "Island Kitchen":"islandkitch",
                     "Pantry":"pantry",
                     "Oven":"oven",
                     "Freezer":"freezer",
                     "Warming Drawer":"warmdrawer",
                     "Eat-in Kitchen":"eatinkitch",
                     "Instant Hot Water":"insthotwater",
                     "Coffee System":"coffeesys",
                     "Breakfast Nook":"breaknook"}
        kitchenlu = pd.DataFrame.from_dict(kitchenlu, orient = "index")
        kitchenlu.insert(loc = 0, column = "desc", value = kitchenlu.index)
        kitchenlu.rename(columns = {0:"column"}, inplace = True)
        kitchenlu.reset_index(inplace = True, drop = True)
        #Living Space
        livingspacelu = {"Walk-In Closets":"walkincloset",
                         "NA":"na",
                         "Hardwood Floors":"hwoodfloor",
                         "Carpet":"carpet",
                         "Bay Window":"baywindow",
                         "Views":"views",
                         "Window Coverings":"windowcov",
                         "Tile Floors":"tilefloor",        
                         "Linen Closet":"linencloset",
                         "Vaulted Ceiling":"vceil",
                         "Vinyl Flooring":"vfloor",
                         "Dining Room":"diningrm",
                         "Den":"den",
                         "Sunroom":"sunrm",
                         "Loft Layout":"loft",
                         "Accent Walls":"accentwalls",
                         "Skylight":"skylight",
                         "Furnished":"furnished",
                         "Office":"office",
                         "Crown Molding":"crownmold",
                         "Double Pane Windows":"doublepw",
                         "Basement":"basement",
                         "Built-In Bookshelves":"bshelves",
                         "Attic":"attic",
                         "Wet Bar":"wetbar",
                         "Family Room":"famrm",
                         "Recreation Room":"recrm",
                         "Mother-in-law Unit":"mothlawunit",
                         "Mud Room":"mudrm"}
        livingspacelu = pd.DataFrame.from_dict(livingspacelu, orient = "index")
        livingspacelu.insert(loc = 0, column = "desc", value = livingspacelu.index)
        livingspacelu.rename(columns = {0:"column"}, inplace = True)
        livingspacelu.reset_index(inplace = True, drop = True)
        #Services
        serviceslu = {"NA":"na",
                      "Package Service":"packserv",
                      "Maintenance on site":"onsitemaint",
                      "Concierge":"concierge",
                      "24 Hour Availability":"avail24hr",
                      "Recycling":"recycling",
                      "Renters Insurance Program":"rentins",
                      "Dry Cleaning Service":"dryclean",        
                      "Online Services":"onlineserv",
                      "Pet Play Area":"petplay",
                      "Pet Care":"petcare",
                      "Controlled Access":"accesscontr",
                      "On-Site ATM":"atm",
                      "Laundry Facilities":"laundry",
                      "Community-Wide WiFi":"commwifi",
                      "Bilingual":"bilingual",
                      "Courtesy Patrol":"patrol",
                      "Guest Apartment":"guestapt",
                      "Car Wash Area":"carwash",
                      "Energy Star Certified":"energystar",
                      "Pet Washing Station":"petwash",
                      "Car Charging Station":"carcharge",
                      "Property Manager on Site":"onsitepropman",
                      "Furnished Units Available":"furnishavail",
                      "Wi-Fi at Pool and Clubhouse":"clubpoolwifi",
                      "Trash Pickup - Door to Door":"ddtrash",
                      "Planned Social Activities":"social",
                      "Laundry Service":"laundryservice",
                      "Shuttle to Train":"shuttle",
                      "Health Club Discount":"hclubdisc",
                      "LEED Rating":"leedrt",
                      "On-Site Retail":"onsiteretail",
                      "Grocery Service":"groceryserv",
                      "Maid Service":"maidserv",
                      "Meal Service":"mealserv",
                      "Day Care":"daycare",
                      "Security System":"securitysys",
                      "House Sitter Services":"housesitserv",
                      "Video Patrol":"videopatrol",
                      "Local Vet / Pet Store Discount":"petstoredisc",
                      "Parking Security":"parksec",
                      "Doorman":"doorman",
                      "Trash Pickup - Curbside":"cstrash",
                      "Composting":"compost",
                      "Hearing Impaired Accessible":"hearimpacc",
                      "Vision Impaired Accessible":"visimpacc",
                      "Per Diem Accepted":"perdiem"}
        serviceslu = pd.DataFrame.from_dict(serviceslu, orient = "index")
        serviceslu.insert(loc = 0, column = "desc", value = serviceslu.index)
        serviceslu.rename(columns = {0:"column"}, inplace = True)
        serviceslu.reset_index(inplace = True, drop = True)
        #Indoor Info
        indoorinfolu = {"Business Center":"businesscent",
                        "Storage Space":"storagespace",
                        "NA":"na",
                        "Clubhouse":"clubhouse",
                        "Elevator":"elevator",
                        "Lounge":"lounge",
                        "Conference Room":"confrm",
                        "Coffee Bar":"coffeebar",     
                        "Multi Use Room":"multiuserm",
                        "Disposal Chutes":"dispchutes",
                        "Library":"library",
                        "Corporate Suites":"corpsuite",
                        "Breakfast/Coffee Concierge":"bcconcierge",
                        "Two Story Lobby":"twostorylobby",
                        "Vintage Building":"vintage",
                        "Tanning Salon":"tanningsal"}
        indoorinfolu = pd.DataFrame.from_dict(indoorinfolu, orient = "index")
        indoorinfolu.insert(loc = 0, column = "desc", value = indoorinfolu.index)
        indoorinfolu.rename(columns = {0:"column"}, inplace = True)
        indoorinfolu.reset_index(inplace = True, drop = True)
        # Outdoor Info
        outdoorinfolu = {"Gated":"gated",
                         "NA":"na",
                         "Boat Dock":"boatdock",
                         "Cabana":"cabana",
                         "Sundeck":"sundeck",
                         "Balcony":"balcony",
                         "Lake Access":"lake",
                         "Courtyard":"ctyard",
                         "Grill":"grill",
                         "Patio":"patio",       
                         "Picnic Area":"picnicarea",
                         "Rooftop Lounge":"rooflounge",
                         "Waterfront":"waterfront",
                         "Zen Garden":"zengarden",
                         "Fenced Lot":"fencedlot",
                         "Yard":"yard",
                         "Lawn":"lawn",
                         "Garden":"garden",
                         "Porch":"porch",
                         "Deck":"deck",
                         "Barbecue Area":"bbqarea",
                         "Barbecue/Grill":"bbq",
                         "Pond":"pond"}
        outdoorinfolu = pd.DataFrame.from_dict(outdoorinfolu, orient = "index")
        outdoorinfolu.insert(loc = 0, column = "desc", value = outdoorinfolu.index)
        outdoorinfolu.rename(columns = {0:"column"}, inplace = True)
        outdoorinfolu.reset_index(inplace = True, drop = True)
    
    return(featureslu, gymlu, kitchenlu, livingspacelu, serviceslu, indoorinfolu, outdoorinfolu)
    
def UnpackPropInfo(df):
    
    # Import required package
    import math
    import pandas as pd
    
    NumUnits = [] # Empty list to store the number of units for each property
    df.columns = [x.lower() for x in df.columns] # Make column headers lowecase
    tempdf = df[[x for x in df.columns if "unit" in x]] # Keep the columns where the number of units is listed
    tempdf.columns = [int(x.split(" ")[0]) for x in tempdf.columns] # Get number of units and convert to integer store as column name
    for i in range(0, len(tempdf)):
        if tempdf.sum(axis = 1)[i] == 0: # If the number of units isn't given
            NumUnits.append(math.nan)
        else: # Else the number of units is given so we extract the number of units
            NumUnit = tempdf.columns[tempdf.loc[i,:] == 1].tolist()[0]
            NumUnits.append(NumUnit)
            
    print('NumUnits Done')
    BuiltIn = []
    tempdf = df[[x for x in df.columns if "built in" in x]] # Keep the columns where the year built is listed
    tempdf.columns = [int(x.split(" ")[2]) for x in tempdf.columns] # Get year built and convert to integer store as column name
    for i in range(0, len(tempdf)):
        if tempdf.sum(axis = 1)[i] == 0: # If the year built isn't given
            BuiltIn.append(math.nan)
        else: # Else year built is given so we extract the year
            Year = tempdf.columns[tempdf.loc[i,:] == 1].tolist()[0]
            BuiltIn.append(Year)
    
    print('BuiltIn Done')

    RenovatedIn = []
    tempdf = df[[x for x in df.columns if "renovated in" in x]] # Keep the columns where the year renovated is listed
    tempdf.columns = [int(x.split(" ")[3]) for x in tempdf.columns] # Get year renovated and convert to integer store as column name
    for i in range(0, len(tempdf)):
        if tempdf.sum(axis = 1)[i] == 0: # If the year renovated isn't given
            RenovatedIn.append(math.nan)
        else: # Else year renovated is given so we extract the year
            Year = tempdf.columns[tempdf.loc[i,:] == 1].tolist()[0]
            RenovatedIn.append(Year)

    print('Renin Done')

        
    LotSize = []
    tempdf = df[[x for x in df.columns if "lot size" in x]] # Keep the columns where the lot size is listed
    tempdf.columns = [float(x.split(" ")[2]) for x in tempdf.columns] # Get lot size and convert to float store as column name
    for i in range(0, len(tempdf)):
        if tempdf.sum(axis = 1)[i] == 0: # If the lot size isn't given
            LotSize.append(math.nan)
        else: # Else lot size is given so we extract the lot size
            Size = tempdf.columns[tempdf.loc[i,:] == 1].tolist()[0]
            LotSize.append(Size)
   
    print('LotSize Done')
    
    Story = []
    colnames = []
    tempdf = df[[x for x in df.columns if ("story" in x) | ("stories" in x)]] # Keep the columns where the lot size is listed
    tempdf2 = [x.strip().split("/") for x in tempdf.columns] # Get lot size and run loop to store as column names
    for element in tempdf2:
        if len(element) == 1:
            colnames.append(int(element[0].split(" ")[0]))
        else:
            colnames.append(int(element[1].split(" ")[0]))
    
    tempdf.columns = colnames
    for i in range(0, len(tempdf)):
        if tempdf.sum(axis = 1)[i] == 0: # If the lot size isn't given
            Story.append(math.nan)
        else: # Else lot size is given so we extract the lot size
            NumStory = tempdf.columns[tempdf.loc[i,:] == 1].tolist()[0]
            Story.append(NumStory)
   
    print('Story Done')


    outputDF = pd.DataFrame()
    outputDF["pid"] = range(0, len(df))
    outputDF["nunit"] = NumUnits
    outputDF["yearbuilt"] = BuiltIn
    outputDF["yearren"] = RenovatedIn
    outputDF["lotsize"] = LotSize
    outputDF["nstory"] = Story
    
    return(outputDF)
            
# ----------------------------------------- END FUNCTIONS -----------------------------------------#