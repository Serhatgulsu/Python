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
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

Genel = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Tum.xlsx", sheet_name="Genel", header=0, index_col=0)
Altmis = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Tum.xlsx", sheet_name="Altmis", header=0, index_col=0)
Ellibes = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Tum.xlsx", sheet_name="Ellibes", header=0, index_col=0)
Elli = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Tum.xlsx", sheet_name="Elli", header=0, index_col=0)
Kirk = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Tum.xlsx", sheet_name="Kirk", header=0, index_col=0)
Otuz = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Tum.xlsx", sheet_name="Otuz", header=0, index_col=0)

pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)


value = Genel["Hit Ratio"]
values = np.array(value)
print(value)

for a in values:
    lists = [np.array(values[i:i + 50]) for i in range(0, 79)]
    print(lists)

model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/n1.xlsx")



model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="n").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="n").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="n").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="n").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="n").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="n").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="n").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="n").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="n").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="n").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model222 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,2,2), trend="n").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/n2.xlsx")


model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="n", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/n3.xlsx")



model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/c1.xlsx")



model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="c").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="c").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="c").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="c").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="c").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="c").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="c").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="c").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="c").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="c").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model222 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,2,2), trend="c").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/c2.xlsx")


model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="c", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/c3.xlsx")



model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/ct1.xlsx")



model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="ct").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="ct").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="ct").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="ct").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="ct").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="ct").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="ct").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="ct").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="ct").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="ct").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model222 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,2,2), trend="ct").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/ct2.xlsx")


model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="ct", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/ct3.xlsx")



model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).forecast(1) for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/t1.xlsx")



model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="t").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="t").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="t").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="t").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="t").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="t").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="t").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="t").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="t").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="t").fit(disp=0).get_forecast(1).summary_frame() for i in range(0, 79)]
model222 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,2,2), trend="t").fit(disp=0).get_forecast(1).summary_frame()  for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/t2.xlsx")


model100 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,0), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model010 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,0), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model001 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,0,1), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model110 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,0), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model101 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,0,1), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model011 = [SARIMAX(np.array(values[i:i +50 ]), order=(0,1,1), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model111 = [SARIMAX(np.array(values[i:i +50 ]), order=(1,1,1), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model211 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,1), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model202 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,0,2), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]
model212 = [SARIMAX(np.array(values[i:i +50 ]), order=(2,1,2), trend="t", seasonal_order=(0,0,0,0)).fit(disp=0).summary() for i in range(0, 79)]

yeni = pd.DataFrame({"model100": model100,
                     "model010": model010,
                     "model001": model001,
                     "model110": model110,
                     "model101": model101,
                     "model011": model011,
                     "model111": model111,
                     "model211": model211,
                     "model202": model202,
                     "model212": model212,
                     "model222": model222})


yeni.to_excel("/Users/serhatgulsu/Desktop/Time Series/t3.xlsx")









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
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX


Genel = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Tum.xlsx", sheet_name="Altmis", header=0, index_col=0)

pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)

value = Genel[6]
values = np.array(value)
print(value)

for a in values:
    lists = [np.array(values[i:i + 50]) for i in range(0, 79)]
    print(lists)

nonseasonality = [pm.auto_arima((np.array(values[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(nonseasonality)

predict1 = ([nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre2 = pd.DataFrame(predict1)

Intervals = pd.DataFrame({"NonSeasonality_Intervals":pre2[1],
                          "Sira": range(1, 80)})

LowerInterval = [(np.concatenate(Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval = [(np.concatenate(Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval = pd.DataFrame({"Lower": LowerInterval,
                        "Upper":UpperInterval,
                          "Sira": range(1, 80)})

predict1 = ([nonseasonality[i].predict(1) for i in range(0, 79)])

p1 = []
for i in range(0, 79):
    p1.append(float(str(predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(p1)

listpredict = pd.DataFrame({'Predict': p1,
                          'Lower': Confidence_Interval["Lower"],
                            'Upper': Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})

list = pd.DataFrame({ 'Genel %10' : 'Genel %10',
                       '50 aylik hit': lists,
                      'Non-Seasonality': nonseasonality,
                       'Hit Ratio': Genel[6][49:],
                     'Sira': range(0,79),})


finallist = pd.merge(list, listpredict, on='Sira', how='inner')
print(finallist)


finallist["Alert"]  = [0 if (finallist["Hit Ratio"][i]>finallist["Lower"][i]) & (finallist["Hit Ratio"][i]<finallist["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist)

