# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:38:56 2020

@author: Administrator
"""

import time 
import json
import requests
from datetime import datetime
import pandas as pd 
import numpy as np 

url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
response = requests.get(url).json()

data = json.loads(response['data'])
#print(data.keys())

areaTree = data["areaTree"]
chinaData = areaTree[0]["children"]
print(chinaData)

for i in range(len(chinaData)):
    province = chinaData["name"]
    today_new = chinaData["today"]["confirm"]
    
