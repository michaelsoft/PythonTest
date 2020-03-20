# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:39:22 2020

@author: Administrator
"""

result = [1, 1]

for i in range(2, 100):
  r = result[i-1] + result[i-2]
  result.append(r)

print(result)
    