# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:30:31 2017

@author: NKallfa
"""

def HalfBath(x):
    
    import re
    numRegex = re.compile(r'\d')
    
    if isinstance(x,str) == True:
        if len(x) > 1:
            return(float(numRegex.search(x).group()+".5"))
        else:
            return(float(x))
    
    #AllUnits.baths = AllUnits.baths.apply(lambda x: x if x == numRegex.search(x).group() else x[0]+".5")