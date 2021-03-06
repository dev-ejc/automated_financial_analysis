from datetime import datetime, timezone
import pandas as pd
import requests
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv("FINNHUB")
class FinnhubExtractor(object):

    @classmethod
    def extract(self,ticker,start,end):
        try:
            headers = {
                'Content-Type': 'application/json'
            }
            params = {
                "token":token,
                "symbol":ticker,
                "resolution":"D",
                "from":int(datetime.strptime(start,"%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp()),
                "to":int(datetime.strptime(end,"%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp()),
                "adjusted":True,
            }
            url = "https://finnhub.io/api/v1/stock/candle"
            requestResponse = requests.get(url,headers=headers,params=params)
            return requestResponse.json()
        except Exception as e:
            print(str(e))
    
    @classmethod
    def quote(self,ticker):
        try:
            headers = {
                'Content-Type': 'application/json'
            }
            params = {
                "token":token,
                "symbol":ticker
            }
            url = "https://finnhub.io/api/v1/quote"
            requestResponse = requests.get(url,headers=headers,params=params)
            return requestResponse.json()
        except Exception as e:
            print(str(e))