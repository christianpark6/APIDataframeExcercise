import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from pandas import json_normalize

###Code Below helps create a function that will create our df gathering inforamation using the web api.
def fun1():
    API_KEY = 'Input API Key Here Found on Polygon.io'
    BASE_URL = 'https://api.polygon.io/v2/aggs/ticker/'
    TICKER = input("Type in Ticker: ")
    END = '?adjusted=true&sort=asc&limit=120&apiKey='
    Range= input("Type in Range in Fomrat: year-month-day/year-month-day")
    requests_url = f'{BASE_URL}{TICKER}/range/1/day/{Range}{END}{API_KEY}'

    data = requests.get(requests_url)


    json = data.json()
    if data.status_code == 200:
        print(json)
    else:
        print("Error")

    df = pd.read_json(requests_url, orient = 'records')
    df1 = df['ticker'].apply(pd.Series)
    df_p = df['resultsCount'].apply(pd.Series)
    df_new = pd.json_normalize(df['results'])
    print(df_new)
    """df = pd.read_json(json, orient ='index')
    print(df)"""

    df2= pd.merge(df1, df_new, left_index=True, right_index=True)
    df2=df2.rename(columns={"v": "Volume", "vw": "Volume_Weighted_Average_Price","o":"Open_Price","c":"Closing_Price","h":"High_Price", "l": "Lowest_Price", "t":"Time_Stamp", "n":"Number_of_Transactions"}, errors="raise")
    pd.set_option('display.max_rows', None)

    return df2


