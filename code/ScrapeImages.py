# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:52:26 2017

@author: NKallfa
"""

import urllib

i = 0
for url in Im.imlink:
    urllib.request.urlretrieve(url, "C:\\Users\\NKallfa\\Desktop\\Documents\\Georgetown Data Science Certificate\\DMV\\\data\\images\\"+str(i)+".jpg")
    i+=1