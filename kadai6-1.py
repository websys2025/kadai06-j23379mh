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

response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)