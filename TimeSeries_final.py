import itertools
import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.tsa.api as smt
import seaborn as sns
import time
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.linear_model import LinearRegression
from scipy import stats
from statistics import mean
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from datetime import datetime
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import adfuller
import pmdarima as pm
from statsmodels.tsa.api import SimpleExpSmoothing

df = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="1", header=0, index_col=0)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)
df.head()

Decompose= seasonal_decompose(df)
Decompose.plot()

plot_acf(df)
plot_pacf(df)

#Dickey-Fuller test
adf, pval, usedlag, nobs, crit_vals, icbest =  adfuller(df.values)
print('ADF test statistic:', adf)
print('ADF p-values:', pval)
print('ADF number of lags used:', usedlag)
print('ADF number of observations:', nobs)
print('ADF critical values:', crit_vals)
print('ADF best information criterion:', icbest)
#Seri Durağan değil.

#Differencing
prev_df = df.shift()
differenced_df = df - prev_df
differenced_df.plot()

differenced_df


plot_acf(differenced_df[1:])
plot_pacf(differenced_df[1:])

adf, pval, usedlag, nobs, crit_vals, icbest =  adfuller(differenced_df.dropna())
print('ADF test statistic:', adf)
print('ADF p-values:', pval)
print('ADF number of lags used:', usedlag)
print('ADF number of observations:', nobs)
print('ADF critical values:', crit_vals)
print('ADF best information criterion:', icbest)

print(value)
value = df[35]
values = np.array(value)
print(values)

for a in values:
    lists = [np.array(values[i:i + 50]) for i in range(0, 79)]
    print(lists)

print(range(0, 79))


nonseasonality = [pm.auto_arima((np.array(values[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(nonseasonality)

seasonality = [pm.auto_arima((np.array(values[i:i + 50]).reshape(-1, 1)), seasonal=True, m=12) for i in range(0, 79)]
print(seasonality)


predict = [seasonality[i].predict(1, return_conf_int=True, alpha=0.05) for i in range(0, 79)]
predict1 = ([nonseasonality[i].predict(1, return_conf_int=True, alpha=0.05) for i in range(0, 79)])

pre1 = pd.DataFrame(predict)
pre2 = pd.DataFrame(predict1)


Intervals = pd.DataFrame({"Seasonality_Intervals": pre1[1],
                        "NonSeasonality_Intervals":pre2[1],
                          "Sira": range(1, 80)})


predict = [seasonality[i].predict(1) for i in range(0, 79)]
print(predict)

predict1 = ([nonseasonality[i].predict(1) for i in range(0, 79)])

p0 = []
for i in range(0, 79):
    p0.append(float(str(predict[i].tolist()).replace("[", "").replace("]", "")))
    print(p0)

p1 = []
for i in range(0, 79):
    p1.append(float(str(predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(p1)

listpredict = pd.DataFrame({'Non-seasonality_Predict': nonseasonality,
                          'Seasonality_Predict': seasonality,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': p1,
                          'Seasonality': p0,
                          'Hit Ratio': df[35][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')
print(final)

print(listpredict)
print(list)
print(finallist)


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/final_1.35.xlsx")

