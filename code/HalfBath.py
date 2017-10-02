# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:30:31 2017

@author: NKallfa
"""

def HalfBath(x):
    
    import re
    numRegex = re.compile(r'\d')
    
    if x == "Unknown":
        return("Unknown")
    elif x == numRegex.search(x).group():
        return(x)
    else:
        return(x[0]+".5")
    
    #AllUnits.baths = AllUnits.baths.apply(lambda x: x if x == numRegex.search(x).group() else x[0]+".5")