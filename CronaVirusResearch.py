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
from pyecharts.charts import *
from pyecharts import options as opts

url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
response = requests.get(url).json()

data = json.loads(response['data'])
#print(data.keys())

areaTree = data["areaTree"]
chinaData = areaTree[0]["children"]
#print(chinaData)

china_list = []
for i in range(len(chinaData)):
    province = chinaData[i]["name"]
    today_new = chinaData[i]["today"]["confirm"]
    total_confirmed = chinaData[i]["total"]["confirm"]
    total_suspect = chinaData[i]["total"]["suspect"]
    total_dead = chinaData[i]["total"]["dead"]
    total_heal = chinaData[i]["total"]["heal"]
    province_data = {}
    province_data["province"] = province
    province_data["new"] = today_new
    province_data["confirm"] = total_confirmed
    province_data["suspect"] = total_suspect
    province_data["dead"] = total_dead
    province_data["heal"] = total_heal

    china_list.append(province_data)
    
#print(china_list)

china_data = pd.DataFrame(china_list, columns=["province","new","confirm","suspect","dead","heal"])

print(china_data)

bar = Bar()
bar.add_xaxis(list(china_data["province"]))
bar.add_yaxis("新增", list(china_data["new"]))
#bar.add_yaxis("累计确诊", list(china_data["confirm"]))
#bar.add_yaxis("疑似", list(china_data["suspect"]))
#bar.add_dataset(china_data)
bar.set_global_opts(title_opts= opts.TitleOpts(title="新冠肺炎疫情"))
bar.render()

map = Map()
xData = list(china_data["province"])
yData = list(china_data["confirm"])
map.add("", [list(z) for z in zip(xData, yData)], "china", is_map_symbol_show=False)
map.set_global_opts(title_opts=opts.TitleOpts("新冠肺炎中国疫情分布图"), 
    visualmap_opts= opts.VisualMapOpts(is_piecewise=True, pieces=[
        {"min": 1001, "label": "> 1000", "color": "#893448"},
        {"min": 501, "max": 1000, "label": "500 - 1000", "color": "#ff585e"},
        {"min": 101, "max": 500, "label": "100 - 500", "color": "#fb8146"},
        {"max": 100, "label": "< 100", "color": "#fff2d1"},
    ]))
map.render_notebook()

page = Page()
page.add(bar)
page.add(map)
page.render(r"c:\temp\新冠肺炎疫情.html")