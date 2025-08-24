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

pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)

value = Genel["Hit Ratio"]
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
                       'Hit Ratio': Genel["Hit Ratio"][49:],
                     'Sira': range(0,79),})


finallist = pd.merge(list, listpredict, on='Sira', how='inner')
print(finallist)


finallist["Alert"]  = [0 if (finallist["Hit Ratio"][i]>finallist["Lower"][i]) & (finallist["Hit Ratio"][i]<finallist["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist[finallist["Alert"]==1])

Transfer = Genel["Transfer"]
Transfers = np.array(Transfer)


for a in Transfers:
    lists1 = [np.array(Transfers[i:i + 50]) for i in range(0, 79)]
    print(lists1)

nonseasonality1 = [pm.auto_arima((np.array(Transfers[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict11 = ([nonseasonality1[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre21 = pd.DataFrame(predict11)

Intervals1 = pd.DataFrame({"NonSeasonality_Intervals":pre21[1],
                          "Sira": range(1, 80)})

LowerInterval1 = [(np.concatenate(Intervals1["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval1 = [(np.concatenate(Intervals1["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval1 = pd.DataFrame({"Lower": LowerInterval1,
                        "Upper":UpperInterval1,
                          "Sira": range(1, 80)})

predict11 = ([nonseasonality1[i].predict(1) for i in range(0, 79)])

p11 = []
for i in range(0, 79):
    p11.append(float(str(predict11[i].tolist()).replace("[", "").replace("]", "")))
    print(p11)

listpredict1 = pd.DataFrame({'Predict': p11,
                          'Lower': Confidence_Interval1["Lower"],
                            'Upper': Confidence_Interval1["Upper"],
                         'Sira': range(1, 80)})

list1 = pd.DataFrame({ 'Transfer %10' : 'Transfer %10',
                       '50 aylik hit': lists1,
                      'Non-Seasonality': nonseasonality1,
                       'Hit Ratio': Genel["Transfer"][49:],
                     'Sira': range(0,79),})


finallist1 = pd.merge(list1, listpredict1, on='Sira', how='inner')
print(finallist1)


finallist1["Alert"]  = [0 if (finallist1["Hit Ratio"][i]>finallist1["Lower"][i]) & (finallist1["Hit Ratio"][i]<finallist1["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist1[finallist1["Alert"]==1])

Yenileme = Genel["Yenileme"]
Yenilemes = np.array(Yenileme)


for a in Yenilemes:
    lists2 = [np.array(Yenilemes[i:i + 50]) for i in range(0, 79)]
    print(lists2)

nonseasonality2 = [pm.auto_arima((np.array(Yenilemes[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict12 = ([nonseasonality2[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre22 = pd.DataFrame(predict12)

Intervals2 = pd.DataFrame({"NonSeasonality_Intervals":pre22[1],
                          "Sira": range(1, 80)})

LowerInterval2 = [(np.concatenate(Intervals2["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval2 = [(np.concatenate(Intervals2["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval2 = pd.DataFrame({"Lower": LowerInterval2,
                        "Upper":UpperInterval2,
                          "Sira": range(1, 80)})

predict12 = ([nonseasonality2[i].predict(1) for i in range(0, 79)])

p12 = []
for i in range(0, 79):
    p12.append(float(str(predict12[i].tolist()).replace("[", "").replace("]", "")))
    print(p12)

listpredict2 = pd.DataFrame({'Predict': p12,
                          'Lower': Confidence_Interval2["Lower"],
                            'Upper': Confidence_Interval2["Upper"],
                         'Sira': range(1, 80)})

list2 = pd.DataFrame({ 'Yenileme %10' : 'Yenileme %10',
                       '50 aylik hit': lists2,
                      'Non-Seasonality': nonseasonality2,
                       'Hit Ratio': Genel["Yenileme"][49:],
                     'Sira': range(0,79),})


finallist2 = pd.merge(list2, listpredict2, on='Sira', how='inner')
print(finallist2)


finallist2["Alert"]  = [0 if (finallist2["Hit Ratio"][i]>finallist2["Lower"][i]) & (finallist2["Hit Ratio"][i]<finallist2["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist2[finallist2["Alert"]==1])



Altmisss = Altmis[6]
Altmiss = np.array(Altmisss)


for a in Altmiss:
    lists3 = [np.array(Altmiss[i:i + 50]) for i in range(0, 79)]
    print(lists3)

nonseasonality3 = [pm.auto_arima((np.array(Altmiss[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict13 = ([nonseasonality3[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre23 = pd.DataFrame(predict13)

Intervals3 = pd.DataFrame({"NonSeasonality_Intervals":pre23[1],
                          "Sira": range(1, 80)})

LowerInterval3 = [(np.concatenate(Intervals3["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval3 = [(np.concatenate(Intervals3["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval3 = pd.DataFrame({"Lower": LowerInterval3,
                        "Upper":UpperInterval3,
                          "Sira": range(1, 80)})

predict13 = ([nonseasonality3[i].predict(1) for i in range(0, 79)])

p13 = []
for i in range(0, 79):
    p13.append(float(str(predict13[i].tolist()).replace("[", "").replace("]", "")))
    print(p13)

listpredict3 = pd.DataFrame({'Predict': p13,
                          'Lower': Confidence_Interval3["Lower"],
                            'Upper': Confidence_Interval3["Upper"],
                         'Sira': range(1, 80)})

list3 = pd.DataFrame({ 'Altmis-6 %10' : 'Altmis-6 %10',
                       '50 aylik hit': lists3,
                      'Non-Seasonality': nonseasonality3,
                       'Hit Ratio': Altmiss[49:],
                     'Sira': range(0,79),})


finallist3 = pd.merge(list3, listpredict3, on='Sira', how='inner')
print(finallist3)


finallist3["Alert"]  = [0 if (finallist3["Hit Ratio"][i]>finallist3["Lower"][i]) & (finallist3["Hit Ratio"][i]<finallist3["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist3[finallist3["Alert"]==1])

Altmis34 = Altmis[34]
Altmiss34 = np.array(Altmis34)


for a in Altmiss34:
    lists4 = [np.array(Altmiss34[i:i + 50]) for i in range(0, 79)]
    print(lists4)

nonseasonality4 = [pm.auto_arima((np.array(Altmiss34[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict14 = ([nonseasonality4[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre24 = pd.DataFrame(predict14)

Intervals4 = pd.DataFrame({"NonSeasonality_Intervals":pre24[1],
                          "Sira": range(1, 80)})

LowerInterval4 = [(np.concatenate(Intervals4["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval4 = [(np.concatenate(Intervals4["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval4 = pd.DataFrame({"Lower": LowerInterval4,
                        "Upper":UpperInterval4,
                          "Sira": range(1, 80)})

predict14 = ([nonseasonality4[i].predict(1) for i in range(0, 79)])

p14 = []
for i in range(0, 79):
    p14.append(float(str(predict14[i].tolist()).replace("[", "").replace("]", "")))
    print(p14)

listpredict4 = pd.DataFrame({'Predict': p14,
                          'Lower': Confidence_Interval4["Lower"],
                            'Upper': Confidence_Interval4["Upper"],
                         'Sira': range(1, 80)})

list4 = pd.DataFrame({ 'Altmis-34 %10' : 'Altmis-34 %10',
                       '50 aylik hit': lists4,
                      'Non-Seasonality': nonseasonality4,
                       'Hit Ratio': Altmis[34][49:],
                     'Sira': range(0,79),})


finallist4 = pd.merge(list4, listpredict4, on='Sira', how='inner')
print(finallist4)


finallist4["Alert"]  = [0 if (finallist4["Hit Ratio"][i]>finallist4["Lower"][i]) & (finallist4["Hit Ratio"][i]<finallist4["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist4[finallist4["Alert"]==1])


Altmis35 = Altmis[35]
Altmiss35 = np.array(Altmis35)


for a in Altmiss35:
    lists5 = [np.array(Altmiss35[i:i + 50]) for i in range(0, 79)]
    print(lists5)

nonseasonality5 = [pm.auto_arima((np.array(Altmiss35[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict15 = ([nonseasonality5[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre25 = pd.DataFrame(predict15)

Intervals5 = pd.DataFrame({"NonSeasonality_Intervals":pre25[1],
                          "Sira": range(1, 80)})

LowerInterval5 = [(np.concatenate(Intervals5["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval5 = [(np.concatenate(Intervals5["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval5 = pd.DataFrame({"Lower": LowerInterval5,
                        "Upper":UpperInterval5,
                          "Sira": range(1, 80)})

predict15 = ([nonseasonality5[i].predict(1) for i in range(0, 79)])

p15 = []
for i in range(0, 79):
    p15.append(float(str(predict15[i].tolist()).replace("[", "").replace("]", "")))
    print(p15)

listpredict5 = pd.DataFrame({'Predict': p15,
                          'Lower': Confidence_Interval5["Lower"],
                            'Upper': Confidence_Interval5["Upper"],
                         'Sira': range(1, 80)})

list5 = pd.DataFrame({ 'Altmis 35- %10' : 'Altmis 35- %10',
                       '50 aylik hit': lists5,
                      'Non-Seasonality': nonseasonality5,
                       'Hit Ratio': Altmis[35][49:],
                     'Sira': range(0,79),})


finallist5 = pd.merge(list5, listpredict5, on='Sira', how='inner')
print(finallist5)


finallist5["Alert"]  = [0 if (finallist5["Hit Ratio"][i]>finallist5["Lower"][i]) & (finallist5["Hit Ratio"][i]<finallist5["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist5[finallist5["Alert"]==1])

Ellibes = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Tum.xlsx", sheet_name="Ellibes", header=0, index_col=0)

Ellibes6 = Ellibes[6]
Ellibess6 = np.array(Ellibes6)


for a in Ellibess6:
    lists6 = [np.array(Ellibess6[i:i + 50]) for i in range(0, 79)]
    print(lists6)

nonseasonality6 = [pm.auto_arima((np.array(Ellibess6[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict16 = ([nonseasonality6[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre26 = pd.DataFrame(predict16)

Intervals6 = pd.DataFrame({"NonSeasonality_Intervals":pre26[1],
                          "Sira": range(1, 80)})

LowerInterval6 = [(np.concatenate(Intervals6["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval6 = [(np.concatenate(Intervals6["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval6 = pd.DataFrame({"Lower": LowerInterval6,
                        "Upper":UpperInterval6,
                          "Sira": range(1, 80)})

predict16 = ([nonseasonality6[i].predict(1) for i in range(0, 79)])

p16 = []
for i in range(0, 79):
    p16.append(float(str(predict16[i].tolist()).replace("[", "").replace("]", "")))
    print(p16)

listpredict6 = pd.DataFrame({'Predict': p16,
                          'Lower': Confidence_Interval6["Lower"],
                            'Upper': Confidence_Interval6["Upper"],
                         'Sira': range(1, 80)})

list6 = pd.DataFrame({ 'Ellibes 6- %10' : 'Ellibes 6- %10',
                       '50 aylik hit': lists6,
                      'Non-Seasonality': nonseasonality6,
                       'Hit Ratio': Ellibes[6][49:],
                     'Sira': range(0,79),})


finallist6 = pd.merge(list6, listpredict6, on='Sira', how='inner')
print(finallist6)


finallist6["Alert"]  = [0 if (finallist6["Hit Ratio"][i]>finallist6["Lower"][i]) & (finallist6["Hit Ratio"][i]<finallist6["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist6[finallist6["Alert"]==1])


Ellibes34 = Ellibes[34]
Ellibess34 = np.array(Ellibes34)


for a in Ellibess34:
    lists7 = [np.array(Ellibess6[i:i + 50]) for i in range(0, 79)]
    print(lists7)

nonseasonality7 = [pm.auto_arima((np.array(Ellibess6[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict17 = ([nonseasonality7[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre27 = pd.DataFrame(predict17)

Intervals7 = pd.DataFrame({"NonSeasonality_Intervals":pre27[1],
                          "Sira": range(1, 80)})

LowerInterval7 = [(np.concatenate(Intervals7["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval7 = [(np.concatenate(Intervals7["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval7 = pd.DataFrame({"Lower": LowerInterval7,
                        "Upper":UpperInterval7,
                          "Sira": range(1, 80)})

predict17 = ([nonseasonality7[i].predict(1) for i in range(0, 79)])

p17 = []
for i in range(0, 79):
    p17.append(float(str(predict17[i].tolist()).replace("[", "").replace("]", "")))
    print(p16)

listpredict7 = pd.DataFrame({'Predict': p17,
                          'Lower': Confidence_Interval7["Lower"],
                            'Upper': Confidence_Interval7["Upper"],
                         'Sira': range(1, 80)})

list7 = pd.DataFrame({ 'Ellibes 34- %10' : 'Ellibes 34- %10',
                       '50 aylik hit': lists7,
                      'Non-Seasonality': nonseasonality7,
                       'Hit Ratio': Ellibes[34][49:],
                     'Sira': range(0,79),})


finallist7 = pd.merge(list7, listpredict7, on='Sira', how='inner')
print(finallist6)


finallist7["Alert"]  = [0 if (finallist7["Hit Ratio"][i]>finallist7["Lower"][i]) & (finallist7["Hit Ratio"][i]<finallist7["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist7[finallist7["Alert"]==1])


Ellibes35 = Ellibes[35]
Ellibess35 = np.array(Ellibes35)


for a in Ellibess35:
    lists8 = [np.array(Ellibess35[i:i + 50]) for i in range(0, 79)]
    print(lists8)

nonseasonality8 = [pm.auto_arima((np.array(Ellibess35[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict18 = ([nonseasonality8[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre28 = pd.DataFrame(predict18)

Intervals8 = pd.DataFrame({"NonSeasonality_Intervals":pre28[1],
                          "Sira": range(1, 80)})

LowerInterval8 = [(np.concatenate(Intervals8["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval8 = [(np.concatenate(Intervals8["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval8 = pd.DataFrame({"Lower": LowerInterval8,
                        "Upper":UpperInterval8,
                          "Sira": range(1, 80)})

predict18 = ([nonseasonality8[i].predict(1) for i in range(0, 79)])

p18 = []
for i in range(0, 79):
    p18.append(float(str(predict18[i].tolist()).replace("[", "").replace("]", "")))
    print(p16)

listpredict8 = pd.DataFrame({'Predict': p18,
                          'Lower': Confidence_Interval8["Lower"],
                            'Upper': Confidence_Interval8["Upper"],
                         'Sira': range(1, 80)})

list8 = pd.DataFrame({ 'Ellibes 35- %10' : 'Ellibes 35- %10',
                       '50 aylik hit': lists8,
                      'Non-Seasonality': nonseasonality8,
                       'Hit Ratio': Ellibes[35][49:],
                     'Sira': range(0,79),})


finallist8 = pd.merge(list8, listpredict8, on='Sira', how='inner')
print(finallist8)


finallist8["Alert"]  = [0 if (finallist8["Hit Ratio"][i]>finallist8["Lower"][i]) & (finallist8["Hit Ratio"][i]<finallist8["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist8[finallist8["Alert"]==1])

Elli = pd.read_excel("/Users/serhatgulsu/Desktop/Time Series/Tum.xlsx", sheet_name="Elli", header=0, index_col=0)

Elli6 = Elli[6]
Ellis = np.array(Elli6)


for a in Ellis:
    lists9 = [np.array(Ellis[i:i + 50]) for i in range(0, 79)]
    print(lists9)

nonseasonality9 = [pm.auto_arima((np.array(Ellis[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict19 = ([nonseasonality9[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre29 = pd.DataFrame(predict19)

Intervals9 = pd.DataFrame({"NonSeasonality_Intervals":pre29[1],
                          "Sira": range(1, 80)})

LowerInterval9 = [(np.concatenate(Intervals9["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval9 = [(np.concatenate(Intervals9["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval9 = pd.DataFrame({"Lower": LowerInterval9,
                        "Upper":UpperInterval9,
                          "Sira": range(1, 80)})

predict19 = ([nonseasonality9[i].predict(1) for i in range(0, 79)])

p19 = []
for i in range(0, 79):
    p19.append(float(str(predict19[i].tolist()).replace("[", "").replace("]", "")))
    print(p16)

listpredict9 = pd.DataFrame({'Predict': p19,
                          'Lower': Confidence_Interval9["Lower"],
                            'Upper': Confidence_Interval9["Upper"],
                         'Sira': range(1, 80)})

list9 = pd.DataFrame({ 'Elli 6- %10' : 'Elli 6- %10',
                       '50 aylik hit': lists9,
                      'Non-Seasonality': nonseasonality9,
                       'Hit Ratio': Elli[6][49:],
                     'Sira': range(0,79),})


finallist9 = pd.merge(list9, listpredict9, on='Sira', how='inner')
print(finallist9)


finallist9["Alert"]  = [0 if (finallist9["Hit Ratio"][i]>finallist9["Lower"][i]) & (finallist9["Hit Ratio"][i]<finallist9["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist9[finallist9["Alert"]==1])

Elli34 = Elli[34]
Ellis34 = np.array(Elli34)


for a in Ellis34:
    lists10 = [np.array(Ellis34[i:i + 50]) for i in range(0, 79)]
    print(lists10)

nonseasonality10 = [pm.auto_arima((np.array(Ellis34[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict20 = ([nonseasonality10[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre30 = pd.DataFrame(predict20)

Intervals10 = pd.DataFrame({"NonSeasonality_Intervals":pre30[1],
                          "Sira": range(1, 80)})

LowerInterval10 = [(np.concatenate(Intervals10["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval10 = [(np.concatenate(Intervals10["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval10 = pd.DataFrame({"Lower": LowerInterval10,
                        "Upper":UpperInterval10,
                          "Sira": range(1, 80)})

predict20 = ([nonseasonality10[i].predict(1) for i in range(0, 79)])

p20 = []
for i in range(0, 79):
    p20.append(float(str(predict20[i].tolist()).replace("[", "").replace("]", "")))
    print(p20)

listpredict10 = pd.DataFrame({'Predict': p20,
                          'Lower': Confidence_Interval10["Lower"],
                            'Upper': Confidence_Interval10["Upper"],
                         'Sira': range(1, 80)})

list10 = pd.DataFrame({ 'Elli 34- %10' : 'Elli 34- %10',
                       '50 aylik hit': lists10,
                      'Non-Seasonality': nonseasonality10,
                       'Hit Ratio': Elli[34][49:],
                     'Sira': range(0,79),})


finallist10 = pd.merge(list10, listpredict10, on='Sira', how='inner')
print(finallist10)


finallist10["Alert"]  = [0 if (finallist10["Hit Ratio"][i]>finallist10["Lower"][i]) & (finallist10["Hit Ratio"][i]<finallist10["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist10[finallist10["Alert"]==1])


Elli35 = Elli[35]
Ellis35 = np.array(Elli35)


for a in Ellis35:
    lists11 = [np.array(Ellis35[i:i + 50]) for i in range(0, 79)]
    print(lists11)

nonseasonality11 = [pm.auto_arima((np.array(Ellis35[i:i + 50]).reshape(-1, 1)), seasonal=False) for i in range(0, 79)]


predict21 = ([nonseasonality11[i].predict(1, return_conf_int=True, alpha=0.10) for i in range(0, 79)])

pre31 = pd.DataFrame(predict21)

Intervals11 = pd.DataFrame({"NonSeasonality_Intervals":pre31[1],
                          "Sira": range(1, 80)})

LowerInterval11 = [(np.concatenate(Intervals11["NonSeasonality_Intervals"]).astype(None)).tolist()[i][0] for i in range(0, 79)]
UpperInterval11 = [(np.concatenate(Intervals11["NonSeasonality_Intervals"]).astype(None)).tolist()[i][1] for i in range(0, 79)]

Confidence_Interval11 = pd.DataFrame({"Lower": LowerInterval11,
                        "Upper":UpperInterval11,
                          "Sira": range(1, 80)})

predict21 = ([nonseasonality11[i].predict(1) for i in range(0, 79)])

p21 = []
for i in range(0, 79):
    p21.append(float(str(predict21[i].tolist()).replace("[", "").replace("]", "")))
    print(p21)

listpredict11 = pd.DataFrame({'Predict': p21,
                          'Lower': Confidence_Interval11["Lower"],
                            'Upper': Confidence_Interval11["Upper"],
                         'Sira': range(1, 80)})

list11 = pd.DataFrame({ 'Elli 35- %10' : 'Elli 35- %10',
                       '50 aylik hit': lists11,
                      'Non-Seasonality': nonseasonality11,
                       'Hit Ratio': Elli[35][49:],
                     'Sira': range(0,79),})


finallist11 = pd.merge(list11, listpredict11, on='Sira', how='inner')
print(finallist11)


finallist11["Alert"]  = [0 if (finallist11["Hit Ratio"][i]>finallist11["Lower"][i]) & (finallist11["Hit Ratio"][i]<finallist11["Upper"][i])
          else 1 for i in range(0, 78)]

print(finallist[finallist["Alert"]==1])
print(finallist1[finallist1["Alert"]==1])
print(finallist2[finallist2["Alert"]==1])
print(finallist3[finallist3["Alert"]==1])
print(finallist4[finallist4["Alert"]==1])
print(finallist5[finallist5["Alert"]==1])
print(finallist6[finallist6["Alert"]==1])
print(finallist7[finallist7["Alert"]==1])
print(finallist8[finallist8["Alert"]==1])
print(finallist9[finallist9["Alert"]==1])
print(finallist10[finallist10["Alert"]==1])
print(finallist11[finallist11["Alert"]==1])


print(finallist2[70:])

x = finallist2["Hit Ratio"]
y = finallist2["Lower"]
z = finallist2["Upper"]

print(x)
print(y)
print(z)

plt.plot(x, color='green', label="Hit Ratio")
plt.plot(y, linestyle='--', color='red', label="Lower Confidence Interval")
plt.plot(z, linestyle='--', color='red', label="Lower Confidence Interval")
plt.title('Time Series - Hit Ratio')
plt.legend()
plt.show()