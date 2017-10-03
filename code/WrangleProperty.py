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
    
    #outputDF = outputDF.pivot(index = "pid", columns = "feature", values = "value").fillna(value = 0)
    #outputDF.insert(loc = 0, column = "pid", value = range(0, len(df)))

    
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
        outputDF.loc[outputDF["desc"] == "Cat Deposit",  "desc"] = "dog"
        outputDF.loc[outputDF["desc"] == "Dog Deposit",  "desc"] = "cat"
        outputDF.loc[outputDF["desc"] == "Other",  "desc"] = "unknown"
        outputDF.loc[outputDF["desc"] == "Other Deposit",  "desc"] = "other"
        outputDF.loc[outputDF["desc"] == "Bird Deposit",  "desc"] = "bird"
        outputDF.loc[outputDF["desc"] == "Fish Deposit",  "desc"] = "fish"
        outputDF.loc[outputDF["desc"] == "Reptile Deposit",  "desc"] = "reptile"
    else:
        outputDF.loc[outputDF["desc"] == "Unassigned Surface Lot Parking",  "desc"] = "unlotpark"
        outputDF.loc[outputDF["desc"] == "Assigned Covered Parking",  "desc"] = "ascovpark"
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
        outputDF.loc[outputDF["desc"] == "Unassigned Street Parking",  "desc"] = "stpark"
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
        
# ----------------------------------------- END FUNCTIONS -----------------------------------------#
# ----------------------------------------- BEGIN SCRIPT -----------------------------------------#

# Import required packages
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import os

### -------------------------- Use the below code to get all data in its original form in a single data frame
##DataList = requests.get("https://worm.nyc3.digitaloceanspaces.com/") # Request html from data store
##soup = BeautifulSoup(DataList.text, "lxml") # Parse html
##DataList = soup.find_all("key") # Find the name of each csv file and store
##
### Initialize empty list to store url to files
#Data = []
##
###Loop through csv files in list of data and append rest of url
##for files in DataList:
##    Data.append("https://worm.nyc3.digitaloceanspaces.com/"+files.text)
#        
#
## Locally
#folderpath = "C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Capstone Project Original Data Copy\\"
#
#for files in os.listdir(folderpath):
#    Data.append(folderpath+files)
#
## Initialize empty data frame to store all original data in a single data frame
#df = pd.DataFrame()
#
## Loop through all csv files and append 
#for files in Data:
#    tempDF = pd.read_csv(files, encoding = "latin-1")
#    df = df.append(tempDF, ignore_index = True) 
## -------------------------- Use the above code to get all data in its original form in a single data frame
#
## -------------------------- Use the below code to clean the data from its original form 
#Names = GetNames(df) # Gets the names of the properties
#Links = GetLinks(df) # Gets the link to property-level information 
#PropertyAddress = SplitAddresses(GetAddresses(df)) # Splits the address into street, city, state, zip
#Contact = SplitPhone(df)
##df = DropCols(df) # Drops columns no longer necessary
#PetsAllowed = GetPetPolicy(df)
#Parking = GetParkingPolicy(df)
#Features = GetFeatures(df, "Features")
#Gym = GetFeatures(df, "Gym")
#Kitchen = GetFeatures(df, "Kitchen")
#Amenities = GetFeatures(df, "Amenities")
#LivingSpace = GetFeatures(df, "Living Space")
#Services = GetFeatures(df, "Services")
#PropertyInfo = GetFeatures(df, "Property Info")
#IndoorInfo = GetFeatures(df, "Indoor Info")
#OutdoorInfo = GetFeatures(df, "Outdoor Info")
#MonthlyFees = GetFees(df, "Monthly Fees")
#OneTimeFees = GetFees(df, "One Time Fees")
# -------------------------- Use the above code to clean the data from its original form 
# ----------------------------------------- END SCRIPT -----------------------------------------#

""" ----------------------------------------- BEGIN THINGS TO DO -----------------------------------------

1. Rename features in GetFees.py so that they are shorter
2. Add function to extract number of images
3. Change encoding of description column
4. Should we try to parse the Lease column or just ignore it?
5. Add feature to extract whether parking is assigned/unassigned
6. Add function to remove instances that are in Fredericksburg, VA and Frederick MD. 

# ----------------------------------------- END THINGS TO DO -----------------------------------------"""


# ----------------------------------------- BEGIN OLD CODE -----------------------------------------#
        
#test = AllCities.loc[(AllCities["City"] == " Fredericksburg") | (AllCities["City"] == " Frederick")]

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

# ----------------------------------------- END OLD CODE -----------------------------------------#
