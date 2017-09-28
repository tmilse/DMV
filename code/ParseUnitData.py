# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:51:03 2017

@author: NKallfa
"""

def Parse(path, i):
    
    from bs4 import BeautifulSoup
    import re
    import pandas as pd
    import math
    
    test = open(path, "r")   
    #test = open("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\PropertyID0.html", "r")
    test2 = test.read()
    soup = BeautifulSoup(test2, "lxml")
    
    beds = ["bed0", "bed1", "bed2", "bed3", "bed4", "bed5"]
    numRegex = re.compile(r"\d")
    
#    Beds = []
#    Baths = []
#    MinRent = []
#    MaxRent = []
#    MinSqFt = []
#    MaxSqFt = []
#    
#    check = 0
#    for numbeds in beds:
#        
#        table = soup.find_all("div", attrs = {"data-tab-content-id" : numbeds})
#        if table == []:
#            check +=1
#            continue
#        else:
#            baths = table[0].find_all("td", attrs = {"class" : "baths"})
#            rent = table[0].find_all("td", attrs = {"class" : "rent"})
#            sqft = table[0].find_all("td", attrs = {"class" : "sqft"})
#            NumUnits = len(baths)
#                
#            for num in range(0,NumUnits):
#                Beds.append(int(numbeds[3]))
#        
#            for elements in baths:
#                temp = elements.find_all("span", attrs = {"class" : "longText"})[0].text.strip().split(" ")[0]
#                Baths.append(temp)
#            
#            for cost in rent:
#                temp = cost.text
#                if "Call for Rent" in temp:
#                    MinRent.append(math.nan)
#                    MaxRent.append(math.nan)
#                else:
#                    temp = temp.split("$")[1].replace("\n", "").replace(",", "").strip()
#                    if len(temp.split(" - ")) == 2:
#                        MinRent.append(int(temp.split(" - ")[0]))
#                        MaxRent.append(int(temp.split(" - ")[1]))
#                    elif len(temp.split(" - ")) == 1:
#                        MinRent.append(int(temp))
#                        MaxRent.append(int(temp))
#            
#            for unit in sqft:
#                temp = unit.text.split(" ")[0].replace(",", "")
#                if len(temp.split(" - ")) == 2:
#                    MinSqFt.append(int(temp.split(" - ")[0]))
#                    MaxSqFt.append(int(temp.split(" - ")[1]))
#                elif temp.split(" - ")[0] == "":
#                    MinSqFt.append(math.nan)
#                    MaxSqFt.append(math.nan)
#                else:
#                    MinSqFt.append(int(temp))
#                    MaxSqFt.append(int(temp))
#        
#        
#        PropertyID = [i]*len(Beds)
#    
#    if check == 6:
#        if  ("Apartments for Rent in" in soup.find_all("title")[0].text) or (soup.find_all("span", attrs = {"class" : "noAvailability"}) != []):
#        #if soup.find_all("span", attrs = {"class" : "noAvailability"}) != []:
#            PropertyID = i
#            Beds = math.nan
#            Baths = math.nan
#            MinRent = math.nan
#            MaxRent = math.nan
#            MinSqFt = math.nan
#            MaxSqFt = math.nan
#            Property = pd.DataFrame({"PropertyID" : PropertyID, "Beds" : Beds, "Baths" : Baths, "MinRent" : MinRent, "MaxRent" : MaxRent, "MinSqFt" : MinSqFt, "MaxSqFt" : MaxSqFt}, index = range(0,1))
#        else:
#            table = soup.find_all("td", attrs = {"class" : "beds"})
#            if "Studio" in table[0].find_all("span", attrs = {"class" : "longText"})[0].text:
#                beds = 0
#            else:
#                beds = numRegex.search(table[0].find_all("span", attrs = {"class" : "longText"})[0].text).group()
#            Beds.append(int(beds))
#            table = soup.find_all("td", attrs = {"class" : "baths"})
#            baths = table[0].find_all("span", attrs = {"class" : "longText"})[0].text.strip().split(" ")[0]
#            Baths.append(baths)
#            temp = soup.find_all("td", attrs = {"class" : "rent"})[0].text
#            if "Call for Rent" in temp:
#                MinRent.append(math.nan)
#                MaxRent.append(math.nan)
#            else:
#                temp = temp.split("$")[1].replace("\n", "").replace(",", "").strip()
#                if len(temp.split(" - ")) == 2:
#                    MinRent.append(int(temp.split(" - ")[0]))
#                    MaxRent.append(int(temp.split(" - ")[1]))
#                elif len(temp.split(" - ")) == 1:
#                    MinRent.append(int(temp))
#                    MaxRent.append(int(temp))
#            temp = soup.find_all("td", attrs = {"class" : "sqft"})[0].text
#            temp = temp.split(" ")[0].replace(",", "")
#            if len(temp.split(" - ")) == 2:
#                MinSqFt.append(int(temp.split(" - ")[0]))
#                MaxSqFt.append(int(temp.split(" - ")[1]))
#            elif temp.split(" - ")[0] == "":
#                MinSqFt.append(math.nan)
#                MaxSqFt.append(math.nan)
#            else:
#                MinSqFt.append(int(temp))
#                MaxSqFt.append(int(temp))
#            PropertyID = [i]
#            Property = pd.DataFrame({"PropertyID" : PropertyID, "Beds" : Beds, "Baths" : Baths, "MinRent" : MinRent, "MaxRent" : MaxRent, "MinSqFt" : MinSqFt, "MaxSqFt" : MaxSqFt})
#    
#    else:
#        if len(Beds) > 1:
#            Property = pd.DataFrame({"PropertyID" : PropertyID, "Beds" : Beds, "Baths" : Baths, "MinRent" : MinRent, "MaxRent" : MaxRent, "MinSqFt" : MinSqFt, "MaxSqFt" : MaxSqFt})
#        else:
#            PropertyID = i
#            Beds = math.nan
#            Baths = math.nan
#            MinRent = math.nan
#            MaxRent = math.nan
#            MinSqFt = math.nan
#            MaxSqFt = math.nan
#            Property = pd.DataFrame({"PropertyID" : PropertyID, "Beds" : Beds, "Baths" : Baths, "MinRent" : MinRent, "MaxRent" : MaxRent, "MinSqFt" : MinSqFt, "MaxSqFt" : MaxSqFt}, index = range(0,1))
        
    
    MetroStation = []
    Distance = []
    Time = []
    
    transport = soup.find_all("div", attrs = {"class" : "transportationDetail"})
    for element in transport:
        if "Commuter" in element.find("th").text:
            look = element.find_all("td")
            for row in look:
                if " min" in row.text:
                    Time.append(int(row.text.split(" ")[0]))
                elif row.text[len(row.text) - 2:len(row.text)] == "mi":
                    Distance.append(float(row.text.split(" ")[0]))
                else:
                    MetroStation.append(row.text)
        else:
            continue
    
    if len(MetroStation) == 0:
        PropertyID = [i]
        MetroStation = ["None"]
        Distance = [math.nan]
        Time = [math.nan]
        Transportation = pd.DataFrame({"PropertyID" : PropertyID, "MetroStation" : MetroStation,"Distance" : Distance, "Time" : Time})
    else:    
        PropertyID = [i]*len(MetroStation)
        Transportation = pd.DataFrame({"PropertyID" : PropertyID, "MetroStation" : MetroStation,"Distance" : Distance, "Time" : Time})
    
    return(Transportation)
    #NumBaths = baths[0].find_all("span", attrs = {"class" : "longText"})
    #
    #Rent = table[0].find_all("td", attrs = {"class" : "rent"})
    #Deposit = table[0].find_all("td", attrs = {"class" : "deposit"})
    #SqFt = table[0].find_all("td", attrs = {"class" : "sqft"})
    #
    #Transport = soup.find_all("div", attrs = {"class" : "transportationDetail"})
    #NumMetro = len(Transport[1].find_all("td"))/3
    #Transport[1].find_all("td")[0].text
    
    
    #MetroStations = Transport[1].find_all("div", attrs = {"class" : "transportationName"})
    #NumMetroStations = len(MetroStations)
    #MetroStations[0].text
