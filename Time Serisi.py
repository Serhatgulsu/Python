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

df = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit.xlsx", sheet_name="Genel")
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)
df.head()
df.shape

sira = np.arange(1,129)
for i in sira:
    column3 = [sira[0:40] for i in range(len(sira))]
    print(column3)

columnx = list(column3)
print(columnx)

ylist = df['Hit Ratio']
ylisty = np.array(ylist)
print(ylisty)

for a in ylisty:
    columny = [ylisty[i-39:i + 1] for i in range(len(ylisty))]
    print(columny)

comb = list(zip(columnx, columny))
yeni1 = pd.DataFrame(comb)
print(yeni1)

yeni1 = yeni1.iloc[39:]
yeni2 = pd.DataFrame(yeni1)
print(yeni2)

print(yeni2)

x = yeni2[0]
y = yeni2[1]
print(x)
print(y)



su=[sum(i) for i in x]
print (su)

sy=[sum(i) for i in y]
print (sy)

squared_numbers = [i ** 2 for i in x]
print(squared_numbers)

x21 = squared_numbers

su2=[sum(i) for i in x21]
print (su2)

a = x * y
xysum=[sum(i) for i in a]
print (xysum)

nadet = [40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 40, 40, 40, 40, 40, 40, 40]

yeni2['n'] = nadet
yeni2['sumx'] = su
yeni2['sumy'] = sy
yeni2['x2'] = su2
yeni2['xy'] = xysum
yeni2['b0'] = (yeni2['sumy']*yeni2['x2']-yeni2['sumx']*yeni2['xy'])/(yeni2['n']*yeni2['x2']-yeni2['sumx']**2)
yeni2['b1'] = (yeni2['n']*yeni2['xy']-yeni2['sumy']*yeni2['sumx'])/(yeni2['n']*yeni2['x2']-yeni2['sumx']**2)
yeni2['ytahmin'] = yeni2['b0'] + yeni2['b1']*x
ytahmin = yeni2['b0'] + yeni2['b1'] * yeni2['n']
yeni2['hata'] = yeni2[1] - ytahmin

print(yeni2)

rank = np.arange(2,89)
print(rank)
print(yeni2['b0'])
print(yeni2['b1'])

check = pd.DataFrame({"intercept": yeni2['b0'],
                      "slope": yeni2['b1']})
print(check)

check["period"] = np.arange(2,91)
print(check)

final = pd.DataFrame({"period": yeni2['n'],
                      "intercept": yeni2['b0'],
                      "slope": yeni2['b1'],
                      "Gercek_Deger": df['Hit Ratio'],
                      "Tahmini_Deger": ytahmin,
                      "Hata": df['Hit Ratio'] -ytahmin})

final1 = pd.merge(final, check, on='period', how='left')

print(final1)

final1.to_excel(r"C:\Users\U00979\Desktop\kontrol5.xlsx")


#########################################################33

from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from datetime import datetime
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import adfuller
import pmdarima as pm
from statsmodels.tsa.api import SimpleExpSmoothing

df = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit.xlsx", sheet_name="Genel", header=0, index_col=0)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)
df.head()

df.plot()

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

adf, pval, usedlag, nobs, crit_vals, icbest =  adfuller(differenced_df.dropna())
print('ADF test statistic:', adf)
print('ADF p-values:', pval)
print('ADF number of lags used:', usedlag)
print('ADF number of observations:', nobs)
print('ADF critical values:', crit_vals)
print('ADF best information criterion:', icbest)

train = df[: 120]
test= df[120:]
print(train)
print(test)

model = pm.auto_arima(train, seasonal=True)
preds = model.predict(test.shape[0])

plt.plot(model)

train.shape

model = pm.auto_arima(train, seasonal=True, m=12)
preds = model.predict(test.shape[0])



print(model)
print(preds)
print(train)

xx = train["Hit Ratio"]
print(xx)

x = np.arange(train.shape[0])
plt.plot(xx[:120], train)
plt.plot(xx[120:], preds)
plt.show()

print(x)

value = df['Hit Ratio']
values = np.array(value)
print(values)

for a in values:
    lists = [values[i-50:i + 1] for i in range(len(values))]
    print(lists)

lists = pd.DataFrame(lists)
lists1 = lists.iloc[50:]
print(lists1)

lists1.shape
c = range(len(lists1)
print(c)

for i in lists1:
    model1 = pm.auto_arima(lists1[i], seasonal=True, m=12)
    print(model1)


for i in values:
    lists2 = [pm.auto_arima([values[i-50:i + 1], seasonal=True, m=12) for i in range(len(values))]
    print(lists2)


print(lists2)



output = pd.DataFrame({"listeler": lists1,
                       "Sarima": model1})










es = SimpleExpSmoothing(df.values)
es.fit(smoothing_level=0.05)
plt.plot(df.values)
plt.plot(es.predict(es.params, start=0, end=None))
plt.show()