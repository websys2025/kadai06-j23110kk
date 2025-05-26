import requests
import pandas as pd

# ==========================================
# 取得したデータの種類：二人以上の世帯の家計収支 
# エンドポイント： https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
# 機能：指定された statsDataId に対応する情報をJSON形式で取得する
# 使い方：python kadai6-1.pyで実行
# ==========================================

APP_ID = "9a212f08709f57748edef459b6f6c67ef05fe8aa"
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0003348239",
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang":"J"
}

response = requests.get(API_URL , params=params)
data = response.json()
print(data)