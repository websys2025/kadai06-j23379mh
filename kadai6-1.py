# 戸籍統計 種類別届出事件数
# 氏や名の変更許可の申立をして、認められた人数
# 読みづらい(キラキラネームなど)、性別違和・性別不合など正当な理由がある場合に認められる

import requests

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

meta_info = json['GET_STATS_DATA']['STATISTICAL_DATA']['CLASS_INF']['CLASS_OBJ']

year = {}
for d in meta_info:
    if d["@id"] == "time":
        for y in d["CLASS"]:
            year[y["@code"]] = y["@name"]

name0 = []#氏の変更
name1 = []#名の変更


for value in data:
    #総数、取り消しは含まない
    if value["@cat02"] == "100" and value["@cat01"] == "100":
        if value["@cat03"] == "370":name0.append(year[value['@time']]+" "+value['$']+value['@unit'])
        elif value["@cat03"] == "420":name1.append(value['$']+value['@unit'])
        
print("氏の変更, 名の変更")
for i in range(len(name0)-1):print(name0[i]+", "+name1[i])