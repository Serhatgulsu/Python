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

Genel = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hususi.xlsx", sheet_name="1HO", header=0, index_col=0)
Transfer = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hususi.xlsx", sheet_name="1HO", header=0, index_col=0)
Yenileme = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hususi.xlsx", sheet_name="1HO", header=0, index_col=0)
Genel6 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="Genel", header=0, index_col=0)
Genel34 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="Genel", header=0, index_col=0)
Genel35 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="Genel", header=0, index_col=0)
Genel16 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="1", header=0, index_col=0)
Genel134 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="1", header=0, index_col=0)
Genel135 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="1", header=0, index_col=0)
Genel26 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="2", header=0, index_col=0)
Genel234 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="2", header=0, index_col=0)
Genel235 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="2", header=0, index_col=0)
Genel36 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="3", header=0, index_col=0)
Genel334 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="3", header=0, index_col=0)
Genel335 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="3", header=0, index_col=0)
Genel46 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="4", header=0, index_col=0)
Genel434 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="4", header=0, index_col=0)
Genel435 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="4", header=0, index_col=0)
Genel56 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="5", header=0, index_col=0)
Genel534 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="5", header=0, index_col=0)
Genel535 = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Hit2.xlsx", sheet_name="5", header=0, index_col=0)

pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)
df.head()



value = Genel[6]
values = np.array(value)


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


print(lists[1])
print(value[51])
print(nonseasonality[0])
print(seasonality)
print(nonseasonality[2].predict(1))
print(seasonality[2].predict(1))
print(nonseasonality[2].predict(1, return_conf_int=True, alpha=0.05))
print(seasonality[2].predict(1, return_conf_int=True, alpha=0.05))



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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel[6][49:],
                          'Sira': range(0,79)})


finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')
print(final)


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel6ho.xlsx")


value = Genel[34]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel[34][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel34ho.xlsx")

value = Genel[35]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel[35][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel35ho.xlsx")

value = Genel[6]
values = np.array(value)


for a in values:
    lists = [np.array(values[i:i + 50]) for i in range(0, 79)]
    print(lists)

print(range(0, 79))

nonseasonality = [pm.auto_arima((np.array(values[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(nonseasonality)

seasonality = [pm.auto_arima((np.array(values[i:i + 50]).reshape(-1, 1)), seasonal=True, m=12) for i in range(0, 79)]
print(seasonality)


predict = [seasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)]
predict1 = ([nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel[6][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel6ho10.xlsx")

value = Genel[34]
values = np.array(value)


for a in values:
    lists = [np.array(values[i:i + 50]) for i in range(0, 79)]
    print(lists)

print(range(0, 79))

nonseasonality = [pm.auto_arima((np.array(values[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(nonseasonality)

seasonality = [pm.auto_arima((np.array(values[i:i + 50]).reshape(-1, 1)), seasonal=True, m=12) for i in range(0, 79)]
print(seasonality)


predict = [seasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)]
predict1 = ([nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel[34][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel34ho10.xlsx")









value = Genel[6]
values = np.array(value)


for a in values:
    lists = [np.array(values[i:i + 30]) for i in range(0, 99)]
    print(lists)

print(range(0, 99))

nonseasonality = [pm.auto_arima((np.array(values[i:i + 30]).reshape(-1, 1)), seasonal=False) for i in range(0, 99)]
print(nonseasonality)

seasonality = [pm.auto_arima((np.array(values[i:i + 30]).reshape(-1, 1)), seasonal=True, m=12) for i in range(0, 99)]
print(seasonality)

print(pd.DataFrame(seasonality).shape)




predict = [seasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 99)]
predict1 = ([nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 99)])

pre1 = pd.DataFrame(predict)
pre2 = pd.DataFrame(predict1)


Intervals = pd.DataFrame({"Seasonality_Intervals": pre1[1],
                        "NonSeasonality_Intervals":pre2[1],
                          "Sira": range(1, 100)})


predict = [seasonality[i].predict(1) for i in range(0, 99)]
print(predict)

predict1 = ([nonseasonality[i].predict(1) for i in range(0, 99)])

p0 = []
for i in range(0, 99):
    p0.append(float(str(predict[i].tolist()).replace("[", "").replace("]", "")))
    print(p0)

p1 = []
for i in range(0, 99):
    p1.append(float(str(predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(p1)

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 100)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel[6][29:],
                          'Sira': range(0,99)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel6ho109.xlsx")

value = Genel[34]
values = np.array(value)


for a in values:
    lists = [np.array(values[i:i + 30]) for i in range(0, 99)]
    print(lists)

print(range(0, 99))

nonseasonality = [pm.auto_arima((np.array(values[i:i + 30]).reshape(-1, 1)), seasonal=False) for i in range(0, 99)]
print(nonseasonality)

seasonality = [pm.auto_arima((np.array(values[i:i + 30]).reshape(-1, 1)), seasonal=True, m=12) for i in range(0, 99)]
print(seasonality)


predict = [seasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 99)]
predict1 = ([nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 99)])

pre1 = pd.DataFrame(predict)
pre2 = pd.DataFrame(predict1)


Intervals = pd.DataFrame({"Seasonality_Intervals": pre1[1],
                        "NonSeasonality_Intervals":pre2[1],
                          "Sira": range(1, 100)})


predict = [seasonality[i].predict(1) for i in range(0, 99)]
print(predict)

predict1 = ([nonseasonality[i].predict(1) for i in range(0, 99)])

p0 = []
for i in range(0, 99):
    p0.append(float(str(predict[i].tolist()).replace("[", "").replace("]", "")))
    print(p0)

p1 = []
for i in range(0, 99):
    p1.append(float(str(predict1[i].tolist()).replace("[", "").replace("]", "")))
    print(p1)

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 100)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel[34][29:],
                          'Sira': range(0,99)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel34ho109.xlsx")











value = Genel[35]
values = np.array(value)


for a in values:
    lists = [np.array(values[i:i + 50]) for i in range(0, 79)]
    print(lists)

print(range(0, 79))

nonseasonality = [pm.auto_arima((np.array(values[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]
print(nonseasonality)

seasonality = [pm.auto_arima((np.array(values[i:i + 50]).reshape(-1, 1)), seasonal=True, m=12) for i in range(0, 79)]
print(seasonality)


predict = [seasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)]
predict1 = ([nonseasonality[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel[35][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel35ho10.xlsx")

value = Genel16[6]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel16.xlsx")

value = Genel134[34]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel134.xlsx")

value = Genel135[35]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel135.xlsx")



value = Genel26[6]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel26.xlsx")

value = Genel234[34]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel234.xlsx")

value = Genel235[35]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel235.xlsx")



value = Genel36[6]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel36.xlsx")

value = Genel334[34]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel334.xlsx")

value = Genel335[35]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel335.xlsx")


value = Genel46[6]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel46.xlsx")

value = Genel434[34]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel434.xlsx")

value = Genel435[35]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel435.xlsx")


value = Genel56[6]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel56.xlsx")

value = Genel534[34]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel534.xlsx")

value = Genel535[35]
values = np.array(value)


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

listpredict = pd.DataFrame({'Non-seasonality_Predict': p0,
                          'Seasonality_Predict': p1,
                         'Sira': range(1, 80)})

list = pd.DataFrame({'50 aylik hit': lists,
                          'Non-Seasonality': nonseasonality,
                          'Seasonality': seasonality,
                          'Hit Ratio': Genel["Hit Ratio"][49:],
                          'Sira': range(0,79)})

finallist = pd.merge(list, listpredict, on='Sira', how='inner')
final = pd.merge(finallist,  Intervals, on='Sira', how='inner')


final.to_excel("/Users/serhatgulsu/Desktop/Time Series/Genel535.xlsx")