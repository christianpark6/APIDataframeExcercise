import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from pandas import json_normalize
from PolygonApiDfSetup  import fun1

###Below Calls the function that carries the dataframe for Visualization Purposes
###The first Visualization shows a scatterplot with trading volume along the x axis and closing price along the y axis.
###The second visualization shows another scatterplot with opening price along the x axis and number of transactions along the y axis.

df2=fun1()



plt.scatter(df2.Volume, df2.Closing_Price)
plt.show()

plt.scatter(df2.Open_Price, df2.Number_of_Transactions, color="red")
plt.show()


