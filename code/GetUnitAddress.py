# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:57:18 2017

@author: NKallfa
"""

def GetUnitAddress(path):
    
    from bs4 import BeautifulSoup
    import re
    import pandas as pd
    import math
    
    # Open, read, and parse html file
    file = open(path, "r") # Open html file
    #test = open("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\PropertyID0.html", "r")
    file = file.read() # Read into memory
    soup = BeautifulSoup(file, "lxml") # Parse html file
    
#    name = soup.find_all("title")[0].text.split(" - ")[0].strip()
#    city = soup.find_all("title")[0].text.split(" - ")[1].split(",")[0].strip()
#    state = soup.find_all("title")[0].text.split(" - ")[1].split(",")[1].split(" | ")[0].strip()
    
    addr = soup.find_all(attrs = {"itemprop":"streetAddress"})[0].text.strip()
    if addr == "":
        addr = soup.find_all(attrs = {"itemprop":"streetAddress"})[0]["content"].strip()
    city = soup.find_all(attrs = {"itemprop":"addressLocality"})[0].text.strip()
    if city == "":
        city = soup.find_all(attrs = {"itemprop":"addressLocality"})[0]["content"].strip()
    state = soup.find_all(attrs = {"itemprop":"addressRegion"})[0].text.strip()
    if state == "":
        state = soup.find_all(attrs = {"itemprop":"addressRegion"})[0]["content"].strip()

    
    return(addr, city, state)
    
import pandas as pd
import re

Name = []
City = []
State = []
IDl = []
dffinal = pd.DataFrame(columns = ["name", "city", "state"])

files = os.listdir("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data")
numRegex = re.compile(r"\d{1,4}")
i = 0

# For each file in directory
for file in files:
    ID = numRegex.search(file).group() # Get property ID
    if ID == "954": # File with property ID = 954 treat separately because we're having trouble parsing it
        IDl.append(ID)
        Name.append("4510 S 31st St")
        City.append("Arlington")
        State.append("VA")
        continue # Goes back to beginning of for loop
    # Parse unit-level data and output unit-level data for that property and local metro station data
    n,c,s = GetUnitAddress("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\"+file)
    IDl.append(ID)
    Name.append(n)
    City.append(c)
    State.append(s)
    if i%100 == 0:
        print(i)
    i+=1
    
dffinal["pid"] = IDl    
dffinal["address"] = Name
dffinal["city"] = City
dffinal["state"] = State



