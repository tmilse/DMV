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
    DogsA = pd.DataFrame()
    CatsA = pd.DataFrame()
    NoPet = pd.DataFrame()
    NegPe = pd.DataFrame()
    OtheA = pd.DataFrame()
    BirdA = pd.DataFrame()
    FishA = pd.DataFrame()
    ReptA = pd.DataFrame()
    UnknP= pd.DataFrame()

    
    
    for policy in df["Pet Policy"]:
        if isinstance(policy, str):
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

                petPolicy = petPolicy.append([1], ignore_index = True)
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

                petPolicy = petPolicy.append([2], ignore_index = True)
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

                petPolicy = petPolicy.append([3], ignore_index = True)
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

                petPolicy = petPolicy.append([4], ignore_index = True)
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

                petPolicy = petPolicy.append([5], ignore_index = True)
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

                petPolicy = petPolicy.append([6], ignore_index = True)
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

                petPolicy = petPolicy.append([7], ignore_index = True)
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

                petPolicy = petPolicy.append([8], ignore_index = True)
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

                petPolicy = petPolicy.append([9], ignore_index = True)
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

                petPolicy = petPolicy.append([10], ignore_index = True)
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

                petPolicy = petPolicy.append([11], ignore_index = True)
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

                petPolicy = petPolicy.append([12], ignore_index = True)
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

                petPolicy = petPolicy.append([13], ignore_index = True)
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

                petPolicy = petPolicy.append([14], ignore_index = True)
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

            petPolicy = petPolicy.append([15], ignore_index = True)

            
    #df.insert(loc = 10, column = "Pet_Policy", value = petPolicy)

    df = pd.DataFrame()
    
    df["pid"] = range(0,6037)
    df["dogsallowed"] = DogsA[0]
    df["catsallowed"] = CatsA[0] 
    df["nopets"] = NoPet[0] 
    df["petsnegotiable"] = NegPe[0] 
    df["otherpetsallowed"] = OtheA[0] 
    df["birdsallowed"] = BirdA[0]
    df["fishallowed"] = FishA[0] 
    df["reptileallowed"] = ReptA[0] 
    df["unknownpets"] = UnknP[0]
    
    return(df)

def GetParkingPolicy(df):
    
    # Import required packages
    import pandas as pd
    
    # Initialize empty data frame to store parking policy
    parkPolicy = pd.DataFrame()
    CoveredPark = pd.DataFrame()
    LotPark = pd.DataFrame()
    StreetPark = pd.DataFrame()
    OtherPark = pd.DataFrame()


    for parking in df["Parking"]:
        if isinstance(parking, str):
            if "Surface Lot and Covered" in parking:
                CoveredPark = CoveredPark.append([1], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([0], ignore_index = True)
                parkPolicy = parkPolicy.append([5], ignore_index = True)
            elif "Surface Lot and Garage" in parking:
                CoveredPark = CoveredPark.append([1], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([0], ignore_index = True)
                parkPolicy = parkPolicy.append([6], ignore_index = True)
            elif "Surface Lot and Other" in parking:
                CoveredPark = CoveredPark.append([0], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([1], ignore_index = True)
                parkPolicy = parkPolicy.append([7], ignore_index = True)
            elif "Surface Lot and Street" in parking:
                CoveredPark = CoveredPark.append([0], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StreetPark = StreetPark.append([1], ignore_index = True)
                OtherPark = OtherPark.append([0], ignore_index = True)
                parkPolicy = parkPolicy.append([8], ignore_index = True)
            elif "Surface Lot, Covered and Garage" in parking:
                CoveredPark = CoveredPark.append([1], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([0], ignore_index = True)
                parkPolicy = parkPolicy.append([9], ignore_index = True)
            elif "Surface Lot, Covered and Other" in parking:
                CoveredPark = CoveredPark.append([1], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([1], ignore_index = True)
                parkPolicy = parkPolicy.append([10], ignore_index = True)
            elif "Surface Lot, Covered, Garage and Other" in parking:
                CoveredPark = CoveredPark.append([1], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([1], ignore_index = True)
                parkPolicy = parkPolicy.append([11], ignore_index = True)
            elif "Surface Lot, Garage and Other" in parking:
                CoveredPark = CoveredPark.append([1], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([1], ignore_index = True)
                parkPolicy = parkPolicy.append([12], ignore_index = True)
            elif "Covered" in parking:
                CoveredPark = CoveredPark.append([1], ignore_index = True)
                LotPark = LotPark.append([0], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([0], ignore_index = True)
                parkPolicy = parkPolicy.append([1], ignore_index = True)
            elif "Garage" in parking:
                CoveredPark = CoveredPark.append([1], ignore_index = True)
                LotPark = LotPark.append([0], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([0], ignore_index = True)
                parkPolicy = parkPolicy.append([1], ignore_index = True)
            elif "Street" in parking:
                CoveredPark = CoveredPark.append([0], ignore_index = True)
                LotPark = LotPark.append([0], ignore_index = True)
                StreetPark = StreetPark.append([1], ignore_index = True)
                OtherPark = OtherPark.append([0], ignore_index = True)
                parkPolicy = parkPolicy.append([2], ignore_index = True)
            elif "Other" in parking:
                CoveredPark = CoveredPark.append([0], ignore_index = True)
                LotPark = LotPark.append([0], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([1], ignore_index = True)
                parkPolicy = parkPolicy.append([3], ignore_index = True)
            elif "Surface Lot" in parking:
                CoveredPark = CoveredPark.append([0], ignore_index = True)
                LotPark = LotPark.append([1], ignore_index = True)
                StreetPark = StreetPark.append([0], ignore_index = True)
                OtherPark = OtherPark.append([0], ignore_index = True)
                parkPolicy = parkPolicy.append([4], ignore_index = True)
        else:
            CoveredPark = CoveredPark.append([0], ignore_index = True)
            LotPark = LotPark.append([0], ignore_index = True)
            StreetPark = StreetPark.append([0], ignore_index = True)
            OtherPark = OtherPark.append([1], ignore_index = True)
            parkPolicy = parkPolicy.append([13], ignore_index = True)
    
    #df.insert(loc = 11, column = "Park_Policy", value = parkPolicy)
    
    df2 = pd.DataFrame()
    df2["pid"] = range(0,6037)
    df2["covpark"] = CoveredPark[0]
    df2["lotpark"] = LotPark[0]
    df2["stpark"] = StreetPark[0]
    df2["unkpark"] = OtherPark[0]
    return(df2)
    
def GetFeatures(df):
    
    import pandas as pd
    
    featuresDF = pd.DataFrame()
    i = 0
    pid = pd.DataFrame()
    
    for elements in df["Features"]:
        if isinstance(elements, str):
            tempElements = elements.split("* ")
            tempElements2 = []
            for x in tempElements[1:]:
                tempElements2.append(x.strip().replace("\n", ""))
            featuresDF = featuresDF.append(tempElements2, ignore_index = True)
            pid = pid.append([i]*len(tempElements2), ignore_index = True)
            i+=1
        else:
            featuresDF = featuresDF.append(["NA"], ignore_index = True)
            pid = pid.append([i], ignore_index = True)
            i+=1

    featDF = pd.DataFrame()
    featDF["pid"] = pid[0]
    featDF["feature"] = featuresDF[0]
    
    return(featDF)
    
def GetMonthlyFees(df):
    
    import pandas as pd
    import math
    
    feesDF = pd.DataFrame()
    PropertyID = pd.DataFrame()
    
    i = 0
    for fees in df["Monthly Fees"]:
        if isinstance(fees, str):
            tempFees = fees.split("* ")
            feesDF = feesDF.append(tempFees[1:], ignore_index = True)
            PropertyID = PropertyID.append([i]*len(tempFees[1:]), ignore_index = True)
            i+=1
        else:
            feesDF = feesDF.append(["NA"], ignore_index = True)
            PropertyID = PropertyID.append([i], ignore_index = True)
            i+=1
    
    df_final = pd.DataFrame()
    df_final["MFees"] = feesDF[0]
    df_final["PropertyID"] = PropertyID[0]
    
    Description = pd.DataFrame()
    Cost = pd.DataFrame()
    
    for fees in df_final["MFees"]:
        tempFees = fees.strip().split(":")
        if len(tempFees) == 1:
            Description = Description.append(tempFees, ignore_index = True)
            Cost = Cost.append(tempFees, ignore_index = True)
        else:
            Description = Description.append([tempFees[0]], ignore_index = True)
            Cost = Cost.append([tempFees[1]], ignore_index = True)

    df_final["Desc"] = Description[0]
    df_final["Cost"] = Cost[0]

    i = 0
    Split = pd.DataFrame()
    PropertyID2 = pd.DataFrame()
    MinCost = pd.DataFrame()
    MaxCost = pd.DataFrame()
    
    for desc in df_final["Desc"]:
        temp = desc.split(",")
#        if len(temp) == 1:
#            continue
#        else:
        Split = Split.append(temp, ignore_index = True)
        if len(temp) == 1:
            PropertyID2 = PropertyID2.append([df_final.PropertyID[i]], ignore_index = True)
        else:
            PropertyID2 = PropertyID2.append([df_final.PropertyID[i]]*len(temp), ignore_index = True)
        tempCost = df_final["Cost"][i].replace("$", "")
        tempCost = tempCost.replace(",", "")
        tempCost = tempCost.replace("\n", "")
        tempCost = tempCost.split(" - ")
        if len(tempCost) == 2:
            MinCost = MinCost.append([int(tempCost[0])], ignore_index = True)
            MaxCost = MaxCost.append([int(tempCost[1])], ignore_index = True)
        elif "Included" in tempCost[0]:
            MinCost = MinCost.append([0]*len(temp), ignore_index = True)
            MaxCost = MaxCost.append([0]*len(temp), ignore_index = True)
        elif "NA" == tempCost[0]:
            MinCost = MinCost.append([math.nan], ignore_index = True)
            MaxCost = MaxCost.append([math.nan], ignore_index = True)
        else:
            MinCost = MinCost.append([int(tempCost[0])], ignore_index = True)
            MaxCost = MaxCost.append([int(tempCost[0])], ignore_index = True)

        
        #MinCost = MinCost.append([df_final["Cost"][i]]*len(temp), ignore_index = True)
        
        i+=1
    
    Split = pd.DataFrame(Split[0].apply(lambda x: x.strip()))
    
    df_final2 = pd.DataFrame()
    df_final2["PropertyID"] = PropertyID2[0]
    df_final2["Desc"] = Split[0]
    df_final2["MinCost"] = MinCost[0]
    df_final2["MaxCost"] = MaxCost[0]
    
    return(df_final2)
    
def GetGym(df):
    
    import pandas as pd
    
    gymDF = pd.DataFrame()
    i = 0
    pid = pd.DataFrame()
    
    for elements in df["Gym"]:
        if isinstance(elements, str):
            tempElements = elements.split("* ")
            tempElements2 = []
            for x in tempElements[1:]:
                tempElements2.append(x.strip().replace("\n", ""))
            gymDF = gymDF.append(tempElements2, ignore_index = True)
            pid = pid.append([i]*len(tempElements2), ignore_index = True)
            i+=1
        else:
            gymDF = gymDF.append(["NA"], ignore_index = True)
            pid = pid.append([i], ignore_index = True)
            i+=1

    GymDF = pd.DataFrame()
    GymDF["pid"] = pid[0]
    GymDF["gymfeat"] = gymDF[0]
    
    return(GymDF)
    
def GetKitchen(df):
    
    import pandas as pd
    
    kitchDF = pd.DataFrame()
    i = 0
    pid = pd.DataFrame()
    
    for elements in df["Kitchen"]:
        if isinstance(elements, str):
            tempElements = elements.split("* ")
            tempElements2 = []
            for x in tempElements[1:]:
                tempElements2.append(x.strip().replace("\n", ""))
            kitchDF = kitchDF.append(tempElements2, ignore_index = True)
            pid = pid.append([i]*len(tempElements2), ignore_index = True)
            i+=1
        else:
            kitchDF = kitchDF.append(["NA"], ignore_index = True)
            pid = pid.append([i], ignore_index = True)
            i+=1

    KitchenDF = pd.DataFrame()
    KitchenDF["pid"] = pid[0]
    KitchenDF["kitchenfeat"] = kitchDF[0]
    
    return(KitchenDF)
    
def GetAmenities(df):
 
    
    import pandas as pd
    
    kitchDF = pd.DataFrame()
    i = 0
    pid = pd.DataFrame()
    
    for elements in df["Amenities"]:
        if isinstance(elements, str):
            tempElements = elements.split("* ")
            tempElements2 = []
            for x in tempElements[1:]:
                tempElements2.append(x.strip().replace("\n", ""))
            kitchDF = kitchDF.append(tempElements2, ignore_index = True)
            pid = pid.append([i]*len(tempElements2), ignore_index = True)
            i+=1
        else:
            kitchDF = kitchDF.append(["NA"], ignore_index = True)
            pid = pid.append([i], ignore_index = True)
            i+=1

    KitchenDF = pd.DataFrame()
    KitchenDF["pid"] = pid[0]
    KitchenDF["kitchenfeat"] = kitchDF[0]
    
    return(KitchenDF)
#    import pandas as pd
#    
#    amenitiesDF = pd.DataFrame()
#    
#    for amenity in df["Amenities"]:
#        if isinstance(amenity, str):
#            tempAmenity = amenity.split("* ")
#            amenitiesDF = amenitiesDF.append(tempAmenity[1:], ignore_index = True)
#        else:
#            amenitiesDF = amenitiesDF.append(["NA"], ignore_index = True)
#        
#    return(amenitiesDF)    
    
def GetLivingSpace(df):

    
    import pandas as pd
    
    kitchDF = pd.DataFrame()
    i = 0
    pid = pd.DataFrame()
    
    for elements in df["Living Space"]:
        if isinstance(elements, str):
            tempElements = elements.split("* ")
            tempElements2 = []
            for x in tempElements[1:]:
                tempElements2.append(x.strip().replace("\n", ""))
            kitchDF = kitchDF.append(tempElements2, ignore_index = True)
            pid = pid.append([i]*len(tempElements2), ignore_index = True)
            i+=1
        else:
            kitchDF = kitchDF.append(["NA"], ignore_index = True)
            pid = pid.append([i], ignore_index = True)
            i+=1

    KitchenDF = pd.DataFrame()
    KitchenDF["pid"] = pid[0]
    KitchenDF["kitchenfeat"] = kitchDF[0]
    
    return(KitchenDF)
#    import pandas as pd
#    
#    livspaceDF = pd.DataFrame()
#    
#    for thing in df["Living Space"]:
#        if isinstance(thing, str):
#            tempThing = thing.split("* ")
#            livspaceDF = livspaceDF.append(tempThing[1:], ignore_index = True)
#        else:
#            livspaceDF = livspaceDF.append(["NA"], ignore_index = True)
#        
#    return(livspaceDF)    

#dfa = GetPetPolicy(AllCities)
#dfa = GetParkingPolicy(dfa)
#feat = GetFeatures(dfa)
#monthlyFees = GetMonthlyFees(dfa) 
#gym = GetGym(dfa)    
#kitchen = GetKitchen(dfa)   
#amenities = GetAmenities(dfa)   
#livspace = GetLivingSpace(dfa)            

# Code to get unique values
#pd.DataFrame(df.Parking.unique()).sort_values(by = 0)
#featuresDF[0].unique()  
#pd.DataFrame(monthlyFees[0].unique()).sort_values(by = 0)
#gym[0].unique()
#kitchen[0].unique()
    
#TO DO
# 1. One Time Fees
# 2. Lease Info
# 3. Services
# 4. Property Info
# 5. Indoor Info
# 6. Outdoor Info
# 7. Images
# 8. Description