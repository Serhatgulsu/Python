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


Yenileme55 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Yenileme55", header=0, index_col=0)
Yenileme50 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Yenileme50", header=0, index_col=0)
Yenileme40 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Veri202209.xlsx", sheet_name="Yenileme40", header=0, index_col=0)



#Ultimate_34Yenileme55

GenelHitRatio34Yenileme55 = np.array(Yenileme55[34])
print(GenelHitRatio34Yenileme55)
for a in GenelHitRatio34Yenileme55:
    GenelHitRatio34Yenileme55lists = [np.array(GenelHitRatio34Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio34Yenileme55lists)
GenelHitRatio34Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio34Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio34Yenileme55nonseasonality)
GenelHitRatio34Yenileme55predict1 = ([GenelHitRatio34Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio34Yenileme55pre2 = pd.DataFrame(GenelHitRatio34Yenileme55predict1)
GenelHitRatio34Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio34Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio34Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio34Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio34Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio34Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio34Yenileme55LowerInterval,
                        "Upper": GenelHitRatio34Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio34Yenileme55predict1 = ([GenelHitRatio34Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio34Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio34Yenileme55p1.append(float(str(GenelHitRatio34Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio34Yenileme55p1)
GenelHitRatio34Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio34Yenileme55p1,
                          'Lower': GenelHitRatio34Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio34Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio34Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio34Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio34Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio34Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[34][49:],
                     'Sira': range(0,79),})
GenelHitRatio34Yenileme55finallist = pd.merge(GenelHitRatio34Yenileme55list, GenelHitRatio34Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio34Yenileme55finallist)
GenelHitRatio34Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio34Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio34Yenileme55finallist["Lower"][i]) & (GenelHitRatio34Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio34Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio34Yenileme55finallist[GenelHitRatio34Yenileme55finallist["Alert"]==1])



#Ultimate_35Yenileme55

GenelHitRatio35Yenileme55 = np.array(Yenileme55[35])
print(GenelHitRatio35Yenileme55)
for a in GenelHitRatio35Yenileme55:
    GenelHitRatio35Yenileme55lists = [np.array(GenelHitRatio35Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio35Yenileme55lists)
GenelHitRatio35Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio35Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio35Yenileme55nonseasonality)
GenelHitRatio35Yenileme55predict1 = ([GenelHitRatio35Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio35Yenileme55pre2 = pd.DataFrame(GenelHitRatio35Yenileme55predict1)
GenelHitRatio35Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio35Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio35Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio35Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio35Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio35Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio35Yenileme55LowerInterval,
                        "Upper": GenelHitRatio35Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio35Yenileme55predict1 = ([GenelHitRatio35Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio35Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio35Yenileme55p1.append(float(str(GenelHitRatio35Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio35Yenileme55p1)
GenelHitRatio35Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio35Yenileme55p1,
                          'Lower': GenelHitRatio35Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio35Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio35Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio35Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio35Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio35Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[35][49:],
                     'Sira': range(0,79),})
GenelHitRatio35Yenileme55finallist = pd.merge(GenelHitRatio35Yenileme55list, GenelHitRatio35Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio35Yenileme55finallist)
GenelHitRatio35Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio35Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio35Yenileme55finallist["Lower"][i]) & (GenelHitRatio35Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio35Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio35Yenileme55finallist[GenelHitRatio35Yenileme55finallist["Alert"]==1])

#Ultimate_55Yenileme55

GenelHitRatio55Yenileme55 = np.array(Yenileme55[55])
print(GenelHitRatio55Yenileme55)
for a in GenelHitRatio55Yenileme55:
    GenelHitRatio55Yenileme55lists = [np.array(GenelHitRatio55Yenileme55[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio55Yenileme55lists)
GenelHitRatio55Yenileme55nonseasonality = [pm.auto_arima((np.array(GenelHitRatio55Yenileme55[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio55Yenileme55nonseasonality)
GenelHitRatio55Yenileme55predict1 = ([GenelHitRatio55Yenileme55nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio55Yenileme55pre2 = pd.DataFrame(GenelHitRatio55Yenileme55predict1)
GenelHitRatio55Yenileme55Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio55Yenileme55pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme55LowerInterval = [(np.concatenate(GenelHitRatio55Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio55Yenileme55UpperInterval = [(np.concatenate(GenelHitRatio55Yenileme55Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio55Yenileme55Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio55Yenileme55LowerInterval,
                        "Upper": GenelHitRatio55Yenileme55UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio55Yenileme55predict1 = ([GenelHitRatio55Yenileme55nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio55Yenileme55p1 = []
for i in range(0, 79):
    GenelHitRatio55Yenileme55p1.append(float(str(GenelHitRatio55Yenileme55predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio55Yenileme55p1)
GenelHitRatio55Yenileme55listpredict = pd.DataFrame({'Predict': GenelHitRatio55Yenileme55p1,
                          'Lower': GenelHitRatio55Yenileme55Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio55Yenileme55Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio55Yenileme55list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio55Yenileme55’',
                       'Yenileme55 aylik hit': GenelHitRatio55Yenileme55lists,
                      'Non-Seasonality': GenelHitRatio55Yenileme55nonseasonality,
                       'Hit Ratio': Yenileme55[55][49:],
                     'Sira': range(0,79),})
GenelHitRatio55Yenileme55finallist = pd.merge(GenelHitRatio55Yenileme55list, GenelHitRatio55Yenileme55listpredict, on='Sira', how='inner')
print(GenelHitRatio55Yenileme55finallist)
GenelHitRatio55Yenileme55finallist["Alert"]  = [0 if (GenelHitRatio55Yenileme55finallist['Hit Ratio'][i]> GenelHitRatio55Yenileme55finallist["Lower"][i]) & (GenelHitRatio55Yenileme55finallist['Hit Ratio'][i]< GenelHitRatio55Yenileme55finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio55Yenileme55finallist[GenelHitRatio55Yenileme55finallist["Alert"]==1])

#Ultimate_16Yenileme50

GenelHitRatio16Yenileme50 = np.array(Yenileme50[16])
print(GenelHitRatio16Yenileme50)
for a in GenelHitRatio16Yenileme50:
    GenelHitRatio16Yenileme50lists = [np.array(GenelHitRatio16Yenileme50[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio16Yenileme50lists)
GenelHitRatio16Yenileme50nonseasonality = [pm.auto_arima((np.array(GenelHitRatio16Yenileme50[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio16Yenileme50nonseasonality)
GenelHitRatio16Yenileme50predict1 = ([GenelHitRatio16Yenileme50nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio16Yenileme50pre2 = pd.DataFrame(GenelHitRatio16Yenileme50predict1)
GenelHitRatio16Yenileme50Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio16Yenileme50pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme50LowerInterval = [(np.concatenate(GenelHitRatio16Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio16Yenileme50UpperInterval = [(np.concatenate(GenelHitRatio16Yenileme50Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio16Yenileme50Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio16Yenileme50LowerInterval,
                        "Upper": GenelHitRatio16Yenileme50UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio16Yenileme50predict1 = ([GenelHitRatio16Yenileme50nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio16Yenileme50p1 = []
for i in range(0, 79):
    GenelHitRatio16Yenileme50p1.append(float(str(GenelHitRatio16Yenileme50predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio16Yenileme50p1)
GenelHitRatio16Yenileme50listpredict = pd.DataFrame({'Predict': GenelHitRatio16Yenileme50p1,
                          'Lower': GenelHitRatio16Yenileme50Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio16Yenileme50Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio16Yenileme50list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio16Yenileme50’',
                       'Yenileme50 aylik hit': GenelHitRatio16Yenileme50lists,
                      'Non-Seasonality': GenelHitRatio16Yenileme50nonseasonality,
                       'Hit Ratio': Yenileme50[16][49:],
                     'Sira': range(0,79),})
GenelHitRatio16Yenileme50finallist = pd.merge(GenelHitRatio16Yenileme50list, GenelHitRatio16Yenileme50listpredict, on='Sira', how='inner')
print(GenelHitRatio16Yenileme50finallist)
GenelHitRatio16Yenileme50finallist["Alert"]  = [0 if (GenelHitRatio16Yenileme50finallist['Hit Ratio'][i]> GenelHitRatio16Yenileme50finallist["Lower"][i]) & (GenelHitRatio16Yenileme50finallist['Hit Ratio'][i]< GenelHitRatio16Yenileme50finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio16Yenileme50finallist[GenelHitRatio16Yenileme50finallist["Alert"]==1])

#Ultimate_7Yenileme40

GenelHitRatio7Yenileme40 = np.array(Yenileme40[7])
print(GenelHitRatio7Yenileme40)
for a in GenelHitRatio7Yenileme40:
    GenelHitRatio7Yenileme40lists = [np.array(GenelHitRatio7Yenileme40[i:i + 50]) for i in range(0, 79)]
    print(GenelHitRatio7Yenileme40lists)
GenelHitRatio7Yenileme40nonseasonality = [pm.auto_arima((np.array(GenelHitRatio7Yenileme40[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(GenelHitRatio7Yenileme40nonseasonality)
GenelHitRatio7Yenileme40predict1 = ([GenelHitRatio7Yenileme40nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])
GenelHitRatio7Yenileme40pre2 = pd.DataFrame(GenelHitRatio7Yenileme40predict1)
GenelHitRatio7Yenileme40Intervals = pd.DataFrame({"NonSeasonality_Intervals": GenelHitRatio7Yenileme40pre2[1],
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme40LowerInterval = [(np.concatenate(GenelHitRatio7Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
GenelHitRatio7Yenileme40UpperInterval = [(np.concatenate(GenelHitRatio7Yenileme40Intervals["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]
GenelHitRatio7Yenileme40Confidence_Interval = pd.DataFrame({"Lower": GenelHitRatio7Yenileme40LowerInterval,
                        "Upper": GenelHitRatio7Yenileme40UpperInterval,
                          "Sira": range(1, 80)})
GenelHitRatio7Yenileme40predict1 = ([GenelHitRatio7Yenileme40nonseasonality[i].predict(1) for i in range(0, 79)])
GenelHitRatio7Yenileme40p1 = []
for i in range(0, 79):
    GenelHitRatio7Yenileme40p1.append(float(str(GenelHitRatio7Yenileme40predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(GenelHitRatio7Yenileme40p1)
GenelHitRatio7Yenileme40listpredict = pd.DataFrame({'Predict': GenelHitRatio7Yenileme40p1,
                          'Lower': GenelHitRatio7Yenileme40Confidence_Interval["Lower"],
                            'Upper': GenelHitRatio7Yenileme40Confidence_Interval["Upper"],
                         'Sira': range(1, 80)})
GenelHitRatio7Yenileme40list = pd.DataFrame({ 'Genel %10' : 'GenelHitRatio7Yenileme40’',
                       'Yenileme40 aylik hit': GenelHitRatio7Yenileme40lists,
                      'Non-Seasonality': GenelHitRatio7Yenileme40nonseasonality,
                       'Hit Ratio': Yenileme40[7][49:],
                     'Sira': range(0,79),})
GenelHitRatio7Yenileme40finallist = pd.merge(GenelHitRatio7Yenileme40list, GenelHitRatio7Yenileme40listpredict, on='Sira', how='inner')
print(GenelHitRatio7Yenileme40finallist)
GenelHitRatio7Yenileme40finallist["Alert"]  = [0 if (GenelHitRatio7Yenileme40finallist['Hit Ratio'][i]> GenelHitRatio7Yenileme40finallist["Lower"][i]) & (GenelHitRatio7Yenileme40finallist['Hit Ratio'][i]< GenelHitRatio7Yenileme40finallist["Upper"][i])
          else 1 for i in range(0, 78)]
print(GenelHitRatio7Yenileme40finallist[GenelHitRatio7Yenileme40finallist["Alert"]==1])


x = GenelHitRatio7Yenileme40finallist["Hit Ratio"]
y = GenelHitRatio7Yenileme40finallist["Lower"]
z = GenelHitRatio7Yenileme40finallist["Upper"]

print(x)
print(y)
print(z)

plt.plot(x, color='green', label="Antalya - Yenileme (%40)")
plt.plot(y, linestyle='--', color='red', label="Lower Confidence Interval")
plt.plot(z, linestyle='--', color='red', label="Upper Confidence Interval")
plt.title('Time Series - Hit Ratio')
plt.legend()
plt.show()