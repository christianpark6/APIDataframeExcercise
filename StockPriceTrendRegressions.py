import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from pandas import json_normalize
from PolygonApiDfSetup import fun1
###In this file, calling the function to access our database in the setup script
###Below I run a few regressions in order to see the effect that trading volume has on Closing Price
###along with the effect that opening price has one the number of transactions.
df2=fun1()

x= df2.Volume
y= df2.Closing_Price
x = x.values.reshape(-1,1)
reg = LinearRegression()
reg.fit(x, y)
print(reg.coef_)
print(reg.intercept_)


x1= df2.Open_Price
y1= df2.Number_of_Transactions
x1 = x1.values.reshape(-1,1)
reg1 = LinearRegression()
reg1.fit(x1, y1)
print(reg1.coef_)
print(reg1.intercept_)


