
#                                           Filename: ScrapeUnitData.py
#
#   Description: This is a python script to scrape data from the web. In order to use this on your computer you will need to make
#                the following changes:
#                 
#                 1. Change the file path to point towards wherever you saved AllCities.csv. 
#                    This is done on the line with the pd.read_csv() command
#                 2. Change i depending on what your starting point is. For Maggie it's 1500, Tanya: 3000, Sanem: 4500
#                 3. Change the condition in the while loop. For Maggie, it's "while i < 3000:"
#                    For Tanya, it's "while i < 4500:"
#                    For Sanem, it's "while i < 6038:"
#                 4. Change file path in the open() command, but please note we need to keep track of which file we scrape 
#                    so you should only replace this text with your own path:
#                        
#                        C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\
#
#                       Try not to replace anything else because I'm using the PropertyID+str(i)+".html" part to keep track of the value of i                
#             MAC USERS: When writing file paths like above I think you need to use FORWARD SLASHES rather than BACKWARD SLASHES

# Import required packages
import requests # This package will scrape the data
from bs4 import BeautifulSoup # We won't use this package, but it will be used to parse the websites we scrape
import pandas as pd # We will use this to read in the csv I sent out over email

# You will need to change the directory here to point to wherever you are storing AllCities.csv
# NOTE: I BELIEVE ON MAC YOU NEED TO USE FORWARD SLASHES INSTEAD OF BACKWARD SLASHES LIKE I DO (since I'm on Windows)
AllCities = pd.read_csv("C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Partly Cleaned September 24\\AllCities.csv", encoding = "latin-1")

#i = 3000 #This is for Tanya (just remove the leading #)
#i = 4500 #This is for Sanem (just remove the leading #) 
i = 955 #This is for Maggie 
while i < 1500: #This is for Maggie, but for Tanya you'll need to change this to 4500 and for Sanem you'll need to change it to 6038 since we have 6037 properties in AllCities.csv
    page = requests.get(AllCities["Link"][i]) # This will scrape or get the html from the url in the ith row of the "Link" column in AllCities.sv
    
    # This will create a new HTML file
    # You just need to change the path to match to a path on your computer where you want to store the files
    # For example, if i = 0, this will create a file called PropertyID0.html in my folder called "Unit Data" and the path to my "Unit Data" folder is "C:\Users\NKallfa\Desktop\Documents\Georgetown Data Science Certificate\Capstone Project Data\Unit Data\"
    # We need to keep track of which property in AllCities.csv matches to the websites 
    # we scrape and that's what the '...PropertyID'+str(i)+ part does 
    Html_file = open('C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\Capstone Project Data\\Unit Data\\PropertyID'+str(i)+'.html', 'w')
    Html_file.write(page.text) # This will write the html to the file you created in the previous line
    Html_file.close # This will just close the file we created 
    i+=1 #This will increase i by 1 so we continue going down the rows of the "Link" column in "AllCities.csv". After this we go back to the beginning of the while loop