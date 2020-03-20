# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:54:42 2020

@author: Administrator
"""

import numpy as np, pandas as pd

data = pd.read_excel(".\Data\外国驻广州领事馆一览表_1583142602148.xlsx", "Sheet1")
print(data)
data = data[:-2][:]
data.sort_values("设馆日期")


print(data.min())