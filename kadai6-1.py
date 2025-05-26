# 戸籍統計 種類別届出事件数

import requests
import pandas as pd

APP_ID = ""
API_URL  = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
  "appId": APP_ID,
  "lang": "J",  # 日本語を指定
  "statsDataId": "0003322640",
  "metaGetFlg":"Y",
  "cntGetFlg":"N",
  "explanationGetFlg":"Y",
  "annotationGetFlg":"Y",
  "sectionHeaderFlg":"1",
  "replaceSpChars":"0"
}

json = requests.get(API_URL, params=params).json()
data = json["GET_STATS_DATA"]['STATISTICAL_DATA']['DATA_INF']['VALUE']

df = pd.DataFrame(data)
meta_info = json['GET_STATS_DATA']['STATISTICAL_DATA']['CLASS_INF']['CLASS_OBJ']

year = {}
cat = {}
for d in meta_info:
    if d["@id"] == "cat03":
        for c in d["CLASS"]:
            cat[c["@code"]] = c["@name"]

    if d["@id"] == "time":
        for y in d["CLASS"]:
            year[y["@code"]] = y["@name"]

for value in data:
    #総数、取り消しは含まない
    if value["@cat03"] == "370" and value["@cat02"] == "100" and value["@cat01"] == "100":
        print(f"{cat[value["@cat03"]]} {year[value['@time']]} {value['$']}{value['@unit']}")
