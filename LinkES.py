import requests
import json

ES_URL = "http://localhost:9200/_sql?format=txt"

body = { "query": "select MonitorData.MonitorDataID from mlau1_hq_v1 where MonitorData.SerialNumber='1413802014'"}

result = requests.post(ES_URL, json=body, headers={'Content-Type':'application/json'})
print(result.text)