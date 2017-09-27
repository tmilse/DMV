# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:10:41 2017

@author: NKallfa
"""

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

def GetParkingPolicy(df):
    
    # Import required packages
    import pandas as pd
    
    # Initialize empty data frame to store parking policy
    parkPolicy = pd.DataFrame()

    for parking in df["Parking"]:
        if isinstance(parking, str):
            if "Surface Lot and Covered" in parking:
                parkPolicy = parkPolicy.append([5], ignore_index = True)
            elif "Surface Lot and Garage" in parking:
                parkPolicy = parkPolicy.append([6], ignore_index = True)
            elif "Surface Lot and Other" in parking:
                parkPolicy = parkPolicy.append([7], ignore_index = True)
            elif "Surface Lot and Street" in parking:
                parkPolicy = parkPolicy.append([8], ignore_index = True)
            elif "Surface Lot, Covered and Garage" in parking:
                parkPolicy = parkPolicy.append([9], ignore_index = True)
            elif "Surface Lot, Covered and Other" in parking:
                parkPolicy = parkPolicy.append([10], ignore_index = True)
            elif "Surface Lot, Covered, Garage and Other" in parking:
                parkPolicy = parkPolicy.append([11], ignore_index = True)
            elif "Surface Lot, Garage and Other" in parking:
                parkPolicy = parkPolicy.append([12], ignore_index = True)
            elif "Covered" in parking:
                parkPolicy = parkPolicy.append([1], ignore_index = True)
            elif "Garage" in parking:
                parkPolicy = parkPolicy.append([1], ignore_index = True)
            elif "Street" in parking:
                parkPolicy = parkPolicy.append([2], ignore_index = True)
            elif "Other" in parking:
                parkPolicy = parkPolicy.append([3], ignore_index = True)
            elif "Surface Lot" in parking:
                parkPolicy = parkPolicy.append([4], ignore_index = True)
        else:
            parkPolicy = parkPolicy.append([13], ignore_index = True)
    
    df.insert(loc = 11, column = "Park_Policy", value = parkPolicy)
    return(df)
    
def GetFeatures(df):
    
    import pandas as pd
    
    featuresDF = pd.DataFrame()
    
    for elements in df["Features"]:
        if isinstance(elements, str):
            tempElements = elements.split("* ")
            featuresDF = featuresDF.append(tempElements[1:], ignore_index = True)
        else:
            featuresDF = featuresDF.append(["NA"], ignore_index = True)
        
    return(featuresDF)
    
def GetMonthlyFees(df):
    
    import pandas as pd
    
    feesDF = pd.DataFrame()
    
    for fees in df["Monthly Fees"]:
        if isinstance(fees, str):
            tempFees = fees.split("* ")
            feesDF = feesDF.append(tempFees[1:], ignore_index = True)
        else:
            feesDF = feesDF.append(["NA"], ignore_index = True)
        
    return(feesDF)
    
def GetGym(df):
    
    import pandas as pd
    
    gymDF = pd.DataFrame()
    
    for gym in df["Gym"]:
        if isinstance(gym, str):
            tempGym = gym.split("* ")
            gymDF = gymDF.append(tempGym[1:], ignore_index = True)
        else:
            gymDF = gymDF.append(["NA"], ignore_index = True)
        
    return(gymDF)
    
def GetKitchen(df):
    
    import pandas as pd
    
    kitchenDF = pd.DataFrame()
    
    for kitchen in df["Kitchen"]:
        if isinstance(kitchen, str):
            tempKitchen = kitchen.split("* ")
            kitchenDF = kitchenDF.append(tempKitchen[1:], ignore_index = True)
        else:
            kitchenDF = kitchenDF.append(["NA"], ignore_index = True)
        
    return(kitchenDF)   
    
def GetAmenities(df):
    
    import pandas as pd
    
    amenitiesDF = pd.DataFrame()
    
    for amenity in df["Amenities"]:
        if isinstance(amenity, str):
            tempAmenity = amenity.split("* ")
            amenitiesDF = amenitiesDF.append(tempAmenity[1:], ignore_index = True)
        else:
            amenitiesDF = amenitiesDF.append(["NA"], ignore_index = True)
        
    return(amenitiesDF)    
    
def GetLivingSpace(df):
    
    import pandas as pd
    
    livspaceDF = pd.DataFrame()
    
    for thing in df["Living Space"]:
        if isinstance(thing, str):
            tempThing = thing.split("* ")
            livspaceDF = livspaceDF.append(tempThing[1:], ignore_index = True)
        else:
            livspaceDF = livspaceDF.append(["NA"], ignore_index = True)
        
    return(livspaceDF)    

dfa = GetPetPolicy(AllCities)
dfa = GetParkingPolicy(dfa)
feat = GetFeatures(dfa)
monthlyFees = GetMonthlyFees(dfa) 
gym = GetGym(dfa)    
kitchen = GetKitchen(dfa)   
amenities = GetAmenities(dfa)   
livspace = GetLivingSpace(dfa)            

# Code to get unique values
#pd.DataFrame(df.Parking.unique()).sort_values(by = 0)
#featuresDF[0].unique()  
#pd.DataFrame(monthlyFees[0].unique()).sort_values(by = 0)
#gym[0].unique()
#kitchen[0].unique()